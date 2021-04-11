#__Face Mask Detection with darknet YOLOv3 and NMS(non-max suppression)__

*  Downloaded dataset from Kaggle-[dataset](https://www.kaggle.com/ivandanilovich/medical-masks-dataset-images-tfrecords)
*  And then extracted that in my local ubuntu system
*  I have written a program to convert label file a YOLO format from XML format [convert.py](https://github.com/perses08/Face_Mask_Detect/blob/main/preprocessing/convert.py)
*  And the then i written a program to paste all text label files on train image directory and genarated dataset with [train_generator.py](https://github.com/perses08/Face_Mask_Detect/blob/main/preprocessing/train_generator.py)[train.txt](https://github.com/perses08/Face_Mask_Detect/blob/main/other/train.txt)
*  There after i created a directory in my google drive and uploaded the custom dataset which i created
*  And then i created a [obj.data](https://github.com/perses08/Face_Mask_Detect/blob/main/other/obj.data), [obj.names](https://github.com/perses08/Face_Mask_Detect/blob/main/other/obj.names)
*  obj.data which contains information about how many classes we have and training and test set files details
*  obj.names which contains object names
*  After i uploaded three of the files to google drive which are obj.data, obj.names and train.txt from local system
*  Then I created a colab notebook with gpu [Notebook](https://github.com/perses08/Face_Mask_Detect/blob/main/Training_with_darknet.ipynb)
*  Initialized(Cloned) a darknet repository to create custom YOLOv3 [darknet](https://github.com/AlexeyAB/darknet)
*  Downloaded pretrained yolov3 weights [YOLOv3 pretrained weights](http://pjreddie.com/media/files/darknet53.conv.74)
*  I then i did some dependencies like yolov3.cfg customization fro my custom dataset and edited makefile set gpu=1 and opencv=1 to run on colab GPU
*  I set batch size as 16 and iteration = 6000
*  And trained model by initializing pretrained weights. 
*  It took 8+ hours to train even though, it was not running upto 6000 iteration. It runned upto 2300+ iterations
*  And i taken a model of first 2000 iterations to test 
*  After I written a program to test model. In that i have used NMS to avoid multiple anchor boxces[Task_Video](https://drive.google.com/file/d/1_LPjQZc3-WGc303ldQrRII1iv7Ohc7gx/view)
*  Extracted a frame after drawing bounding box and detection
*  With that frames i created a video [Task_completed](https://drive.google.com/file/d/1Q9yTmaeDrgrNHm0XIl_CdnCe5asMj66V/view?usp=sharing)

