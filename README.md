#__Face Mask Detection with darknet YOLOv3 and NMS(non-max suppression)__

*  Downloaded dataset from Kaggle-[dataset](https://www.kaggle.com/ivandanilovich/medical-masks-dataset-images-tfrecords)
*  And then extracted that in my local ubuntu system
*  I have written a program to convert label file a YOLO format from XML format [convert.py](https://github.com/perses08/Face_Mask_Detect/blob/main/preprocessing/convert.py)
*  And the then i written a program to paste all text label files on train image directory and genarated dataset with [train_generator.py](https://github.com/perses08/Face_Mask_Detect/blob/main/preprocessing/train_generator.py)[train.txt](https://github.com/perses08/Face_Mask_Detect/blob/main/other/train.txt)
*  There after i created a directory in my google drive and uploaded the custom dataset which i created
*  And then i created a [obj.data](https://github.com/perses08/Face_Mask_Detect/blob/main/other/obj.data), [obj.names](https://github.com/perses08/Face_Mask_Detect/blob/main/other/obj.names)
*  obj.data which contains information about how many classes we have and training and test set files details
*  obj.names which contains object names
*  After i uploaded three of the files to google drive which are obj.data, obj.names and train.txt from loccal system
*   
*  

