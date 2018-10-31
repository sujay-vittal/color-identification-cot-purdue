import cv2
from color_recognition_api import color_histogram_feature_extraction
from color_recognition_api import knn_classifier
import os
import os.path
import numpy as np
from matplotlib import pyplot as plt

# read the test image
source_image = cv2.imread('/Users/sujayvittal/Documents/color_recognition-master/src/black_cat.jpg')
prediction = 'n.a.'

# checking whether the training data is ready
PATH = './training.data'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print ('training data is ready, classifier is loading...')
else:
    print ('training data is being created...')
    open('training.data', 'w')
    color_histogram_feature_extraction.training()
    print ('training data is ready, classifier is loading...')

#masking the image
#mask = np.zeros(source_image.shape[:2], np.uint8)
#mask[100:300, 100:400] = 255
#masked_img = cv2.bitwise_and(source_image,source_image,mask = mask)

#histogram with mask
#hist_mask = cv2.calcHist([source_image],[0],mask,[256],[0,256])


#plt.subplot(221), plt.imshow(source_image, 'gray')
#plt.subplot(222), plt.imshow(mask,'gray')
#plt.subplot(223), plt.imshow(masked_img, 'gray')
#plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
#plt.xlim([0,256])

#plt.show()

# get the prediction
color_histogram_feature_extraction.color_histogram_of_test_image(source_image)
prediction = knn_classifier.main('training.data', 'test.data')
cv2.putText(
    source_image,
    ' ' + prediction,
    (15, 45),
    cv2.FONT_HERSHEY_PLAIN,
    3,
    200,
    )

# Display the resulting frame
cv2.imshow('color classifier', source_image)
cv2.waitKey(0)		
