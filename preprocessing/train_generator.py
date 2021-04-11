import os

image_files = []
os.chdir('custom_data')
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("custom_data/" + filename)
        
txt_files = []
        
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        txt_files.append("custom_data/" + filename)
        
os.chdir("..")
with open("train.txt", "w") as outfile:
    for image in image_files:
    	if image.split('.')[0]+'.txt' in txt_files:
        	outfile.write(image)
        	outfile.write("\n")
    outfile.close()
os.chdir("..")
