#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Demonstrates web detection using the Google Cloud Vision API.

Example usage:
  python web_detect.py https://goo.gl/X4qcB6
  python web_detect.py ../detect/resources/landmark.jpg
  python web_detect.py gs://your-bucket/image.png
"""
# [START full_tutorial]
# [START imports]
import argparse
import io
import cv2
import time
from google.cloud import vision
from google.cloud.vision import types
# [END imports]
word=['cigarette','Smoking','smoking']


def annotate(path):
    """Returns web annotations given the path to an image."""
    # [START get_annotations]
    client = vision.ImageAnnotatorClient()

    if path.startswith('http') or path.startswith('gs:'):
        image = types.Image()
        image.source.image_uri = path

    else:
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

    web_detection = client.web_detection(image=image).web_detection
    # [END get_annotations]

    return web_detection


def report(annotations):
    """Prints detected features in the provided web annotations."""
    # [START print_annotations]
    # if annotations.pages_with_matching_images:
    #     print('\n{} Pages with matching images retrieved'.format(
    #         len(annotations.pages_with_matching_images)))

    #     for page in annotations.pages_with_matching_images:
    #         print('Url   : {}'.format(page.url))

    # if annotations.full_matching_images:
    #     print ('\n{} Full Matches found: '.format(
    #            len(annotations.full_matching_images)))

    #     for image in annotations.full_matching_images:
    #         print('Url  : {}'.format(image.url))

    # if annotations.partial_matching_images:
    #     print ('\n{} Partial Matches found: '.format(
    #            len(annotations.partial_matching_images)))

    #     for image in annotations.partial_matching_images:
    #         print('Url  : {}'.format(image.url))

    if annotations.web_entities:
        print ('\n{} Web entities found: '.format(
            len(annotations.web_entities)))
        state = False
        for entity in annotations.web_entities:
            # if entity.description in word1:
            # 	print 'cigarette'
            # if entity.description in word2:
            # 	print 'Smoking'
            for x in xrange(0,len(word)):
            	
            	if word[x] in entity.description :
            		print word[x]
            		state =True
			#print('Score      : {}'.format(entity.score))
            #print('Description: {}'.format(entity.description))
        return state
    # [END print_annotations]


if __name__ == '__main__':
    # [START run_web]
    # parser = argparse.ArgumentParser(
    #     description=__doc__,
    #     formatter_class=argparse.RawDescriptionHelpFormatter)
    # path_help = str('The image to detect, can be web URI, '
    #                 'Google Cloud Storage, or path to local file.')
    # parser.add_argument('image_url', help=path_help)
    # args = parser.parse_args()
    # print args.image_url
#     t0 = time.time() # start time in seconds
#     cap1 = cv2.VideoCapture(1)

# i=0
# j=0
# d=1
# while(1):
#     ret,frame1 = cap1.read()
#     cv2.imshow('Live Feed',frame1)
#     filename = "/home/rubesh/gcloud/test/img%d.jpg"%d
#     if i%1 == 0:
#         #cv2.imwrite(os.path.join(path , 'a{:>05}.jpg'.format(j)),frame1)
#         cv2.imwrite(filename, frame1)
#     j+=1
#     t1 = time.time() # current time
#     num_seconds = t1 - t0 # diff
#     if num_seconds > 5:  # e.g. break after 30 seconds
#       break
#     d+=1
#     i+=1

#cap1.release()
#      ap = argparse.ArgumentParser()
#      ap.add_argument("-v", "--video",
#            help="path to the (optional) video file")
#      ap.add_argument("-b", "--buffer", type=int, default=32,
#         help="max buffer size")
#      args = vars(ap.parse_args())
#      # if a video path was not supplied, grab the reference
# # to the webcam
#     if not args.get("video", False):
#         camera = cv2.VideoCapture(0)

# # otherwise, grab a reference to the video file
#     else:
        t0 = time.time()
        camera = cv2.VideoCapture("/home/rubesh/gcloud/smoking.mp4")
i=0
j=0
d=1
while(1):
    ret,frame1 = camera.read()
    #cv2.imshow('Live Feed',frame1)
    filename = "/home/rubesh/gcloud/test/img%d.jpg"%d
    #if i%30 == 0:
    #     #cv2.imwrite(os.path.join(path , 'a{:>05}.jpg'.format(j)),frame1)
    
    # j+=1
    t1 = time.time() # current time
    num_seconds = t1 - t0 # diff
    if num_seconds > 2:  # e.g. break after 30 seconds
      break
    cv2.imwrite(filename, frame1)
    d+=1
     #i+=1
camera.release()
for i in range (1,15):

	       image = cv2.imread('test/img{}.jpg'.format(i))
	       condition=report(annotate('test/img{}.jpg'.format(i)))
	       print condition
	       if condition == True :
		      cv2.putText(image, "Smoking detected", (10,40), cv2.FONT_HERSHEY_SIMPLEX,
					 0.9, (0, 255, 0), 2)
		      cv2.imshow("Image1", image) 
	       else:
		       cv2.putText(image, "Smoking detected", (10,40), cv2.FONT_HERSHEY_SIMPLEX,
		 			                       0.9, (0, 255, 0), 2)
		       cv2.imshow("Image1", image)
	       cv2.waitKey(0)
	    
    
    # [END run_web]
# [END full_tutorial]
