import os
import xml.etree.ElementTree as ET

classes = []
 
dirpath = '/home/pselvakumar24/Documents/FaceMask/dataset/labels' # xml file storage directory of the original
newdir = '/home/pselvakumar24/Documents/FaceMask/dataset/label1' #txt directory formed after the modified label 
 
if not os.path.exists(newdir):
    os.makedirs(newdir)
 
for fp in os.listdir(dirpath):
 
    root = ET.parse(os.path.join(dirpath,fp)).getroot()
 
    xmin, ymin, xmax, ymax = 0,0,0,0
    
    sz = root.find('size')
    
    width = float(sz[0].text)
    height = float(sz[1].text)
    
    filename = root.find('filename').text
    
    for child in root.findall ( 'object'):
       
        sub = child.find ( 'bndbox') 
        label = child.find('name').text
        if label not in classes:
            classes.append(label)
        label = classes.index(label)
         
        xmin = float(sub[0].text)
        ymin = float(sub[1].text)
        xmax = float(sub[2].text)
        ymax = float(sub[3].text)
        
        x_center = (xmin + xmax) / (2 * width)
        y_center = (ymin + ymax) / (2 * height)
        
        w = (xmax - xmin) / width
        h = (ymax - ymin) / height
        
        with open(os.path.join(newdir, fp.split('.')[0]+'.txt'), 'a+') as f:
            f.write(' '.join([str(label), str(x_center), str(y_center), str(w), str(h) + '\n']))
 
print('ok')