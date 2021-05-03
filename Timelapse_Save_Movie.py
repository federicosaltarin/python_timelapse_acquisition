import cv2
import time
import pause
import datetime
import glob

# Define the path for images and video saving
path = "D:/Video_RPI/Windows/"
# Define the frames per second for final timelapse movie
fps_movie = 15
# Define here the date and time for timelapse start
day = 18
month = 4
year = 2021
hour = 6
minute = 30
seconds = 00
# Define here the duration of the timelapse (hours, minutes and seconds)
tl_h = 0
tl_m = 0
tl_s = 30
# Frames Per Seconds of the timelapse
fps = 6
# Calculate the total number of frames to acquire
nframes = int(round(tl_h * 3600 + tl_m * 60 + tl_s) * fps)
# Define the address of the IP Camera and capture it
address = "http://192.168.x.xxx:8080/video"
camera = cv2.VideoCapture(address)
#0 or 1 is needed if a camera is directly accessible from the device (e.g. webcam or other camera)
#camera = cv2.VideoCapture(0)
# Pause until it's exactly the date/time defined before
start_time = datetime.datetime(year, month, day, hour, minute, seconds)
#start_time = datetime.datetime.now()
pause.until(start_time)
# Start timelapse acquisition and save on external drive
for i in range(nframes):
    ret, img = camera.read()
    cv2.imwrite(path + "img_" + str(i).zfill(4) + ".jpg", img)
    time.sleep(1 / fps)
# Release camera to end acquisition
camera.release()
# Define images array for assembling the timelapse video
images = []
# Assemble the timelapse movie
for filename in glob.glob(path + "*.jpg"):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    framesize = (width, height)
    images.append(img)
# Save the assembled timelapse
out = cv2.VideoWriter('D:/Video_RPI/Windows/video.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps_movie, framesize)
for i in range(len(images)):
    out.write(images[i])
out.release()