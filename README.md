# COLOR RECOGNITION
This project focuses on color classifying by K-Nearest Neighbors Classifier which is trained by R, G, B Color Histogram. It can classify White, Black, Red, Green, Blue, Orange, Yellow and Violet. If you want to classify more color or improve the accuracy you should work on the [training data](https://github.com/sujay-vittal/color-identification-cot-purdue/tree/master/src/training_dataset).

You can also use the [color_recognition_api](https://github.com/sujay-vittal/color-identification-cot-purdue/tree/master/src/color_recognition_api) to perform real-time color recognition in your projects.

## Possible Errors while Executing

***When you run [color_classification_webcam.py](https://github.com/sujay-vittal/color-identification-cot-purdue/blob/master/src/color_classification_webcam.py) to perform real-time color recognition on a webcam stream, you might face issues with the camera lauch. Especially if you're executing it on a mac environment. Please change the cap = cv2.VideoCapture(1) to cap = cv2.VideoCapture(0) (line 9; color_classification_webcam.py) and it should work. What happens is sometimes you might not have a built in camera. '0' is for built in cameras. You put '1' for external cameras that you might attach***

---

## Citation
If you use this code for your publications, please cite it as:

@ONLINE{cr,
author = "Sujay Vittal",
title  = "Color Identification - Python and OpenCV",
year   = "2018",
url    = "https://github.com/sujay-vittal/color-identification-cot-purdue"
}

## Author
Sujay Vittal

## License
This system is available under the MIT license. See the LICENSE file for more info.
