---
title: "Instructions on Collecting a Dataset for Facial Recognition"
---

A major component of the "A Face inthe Crowd" module is creating a facial recognition system using the Eigenfaces algorithm.  This challenge serves as an integration point for almost all of the fundamental linear algebra concepts convered in the module.  We have found that students enjoy using a dataset composed of images of their peers to train and test with.  This document will walk you through how to easily create such a dataset.  The provided pipeline will give you a ``.mat`` file with labeled, face-cropped images of each student's face.

***Note regarding sensitivity***

* While to some the collection of images of one's face for inclusion in such a dataset may seem innocuous, to others this act might be hugely anxiety provoking (e.g., students with gender dysphoria who are self-conscious about their appearance).  We strongly advise you to allow students to opt out of this dataset.
* In the workflow below we show how to collect and label images for smiling / not smiling.  We think that this is a relatively benign category to label (if we are wrong, we'd love to hear why), but there are other categories that we would avoid labeling without careful consideration (e.g., gender, race, age).

## Photobooth and Camera Setup

We recommend setting up the photobooth environment according to the following guidelines.
* Choose a spot with a clean background (e.g., a solid white wall).  While it may be interesting to have students think about how to get good performance on this task with varied backgronds, as a first experience with computer vision we recommend making the task fairly controlled.
* Make sure the spot you choose has good lighting (avoid backlighting of the subject's face).
* Consider using a chair with adjustable height to get a consistent angle on each subject's face regardless of their height.

For the camera, we recommend an external webcam and a tripod to make sure you have a upright, frontal view of the subject's face.

## Setup of Image Capture Computer

1. Make sure that OpenCV and Python3 are both installed.  The easiest way we have found to do this is by using the [Anaconda distribution of Python](https://www.anaconda.com/products/individual).  Once you have installed it, you can use ``conda`` to [install the opencv package](https://anaconda.org/conda-forge/opencv).

2. Download the [image capture Python script](supporting_files/capturephotos2020.py) and [supporting face detector](supporting_files/haarcascade_frontalface_alt.xml) (make sure to download them to the same directory).

## Collecting the Photos

Detailed instructions on running the photo collection script are included as comments in the script itself.  Here are those comments reproduced for convenience sake.

```python
# This code captures photos from a webcam by finding faces and storing them as 256x256 pngs
# Prior to taking photos, empty folder named as photodir (search below)
# Photo set up:
#   Ensure white background with no other facial images (webcam will otherwise capture images from posters)
#
# Overview of image capture procedure
#   Once webcam image is in view, put cursor in the webcam window and
#   Press SPACE to take the photo:
#   Press q to quit
# The default is to save the photos with in a subfolder relative to the capture code, name stored in photodir
#
# To run: You need python (version 3.x)
#     Open a command window and navigate to this folder
#     1. Type python capturephotos2020.py firstname_lastinitial_smile
#     2. Make sure the name has no spaces
#     3. Put cursor in image window; Capture 4 images of smiling
#     4. With cursor in window, press "q"
#     5. Use UP arrow at the command line, delete "smile" from firstname_lastinitial_smile
#     6. Repeat steps 3 & 4 to capture 4 non-smiling photos
```

## Assembling the Dataset

We have provided a [MATLAB script](supporting_files/createclassdata2020.m) for taking the photos generated using the Python script and assembling them into a single .mat file to allow students to access the images more easily.
