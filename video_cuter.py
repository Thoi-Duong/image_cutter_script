import cv2
import numpy as np
print(cv2.__version__)
count = 1
for index in range(1, 12):
  vidcap = cv2.VideoCapture('manato_card_raw_data_set/masato_%d.mp4' % index)
  success,image = vidcap.read()
  success = True

  fps = vidcap.get(cv2.CAP_PROP_FPS)
  est_video_length_minutes = round(1)     # Round up if not sure.
  est_tot_frames = est_video_length_minutes * 24 * fps  # Sets an upper bound # of frames in video clip

  n = 10                  # Desired interval of frames to include
  # get frame by skip n frame
  desired_frames = n * np.arange(est_tot_frames) 
  for i in desired_frames:
    if i%9==0:
      vidcap.set(1,i-1)                      
      success,image = vidcap.read(1) 
      if success != True:
        break
      height, width = image.shape[:2]        # image is an array of array of [R,G,B] values
      img_resize = cv2.resize(image, (width/5, height/5), interpolation = cv2.INTER_AREA)
      
      cv2.imwrite("data_sets/masato/masato%d.jpg" % count , img_resize)
      count += 1

  # get frame by frame

  # while success:
  #   height, width = image.shape[:2]        # image is an array of array of [R,G,B] values
  #   img_resize = cv2.resize(image, (width/5, height/5), interpolation = cv2.INTER_AREA)
  #   cv2.imwrite("data_sets/kondo/kondo%d.jpg" % count, img_resize)     # save frame as JPEG file
  #   success,image = vidcap.read()
  #   print 'Read a new frame: ', success
  #   count += 1

  vidcap.release()
  
