# extract_face_parts
extract face part on an image.
## How to use
+ change line 64 and line 65 on main.py
``` python
start = extract() # write path of the image file (line 64)
start.dectect_face_part() # write one of the face part / True or False to show the detected face (default=False) / True or False to save file which is part of the face (defalut=False) (line 65)

# exmple
# start = extract('./images/image.jpg') 
# start.detect_face_part('lips',True,True)
```
+ run main.py

## Requirements
+ [download pre-trained data](https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2)
+ dlib
+ opencv

## Face parts
+ left_eye
+ right_eye
+ lips
+ left_eyebrow
+ right_eyebrow

### Reference
+ https://github.com/davisking/dlib-models
+ http://blog.dlib.net/2016/10/easily-create-high-quality-object.html
+ http://dlib.net/
+ https://youtu.be/V2gmgkSqyi8
