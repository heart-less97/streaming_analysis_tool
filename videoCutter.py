import os
import functionsWin as win
from time import time

start_time = time()

# Folders were the videos will be send
folderTest = "folderTest/"
folder4k = "folder4k/"
folder2k = "folder2k/"
folder1k = "folder1k/"

# Duration in seconds of our video 
duration = 12

# Name of each video
videoList = []
video1k = str("video12s_1kto4k.mp4")
video2k = str("video12s_2kto4k.mp4")
video4k = str("video12sec.mp4")

videoList.append(video1k)
videoList.append(video2k)
videoList.append(video4k)

qualityList = ["1k", "2k", "4k"]
segmentList = [1, 2, 3, 4, 6]

txtList = []

# Process single video
q = 1
for v in videoList:
    for s in segmentList:
        txtList.append(win.processVideo(v, s, q, 12))
    q = q + 1            

# Process random video
nRandList = ["1", "2", "3", "4", "6"]
s = 0
for v in nRandList:
    s = s + 1
    if s == 5:
        s = s + 1
    txtList.append(win.processRandom(s, duration, v))

# Join every video
num = 1
for txt in txtList:
    win.joinWithConcat(txt, "concat_" + str(num) + ".mp4", folderTest)
    num = num + 1

elapsed_time = time() - start_time

print("Ha tardat en executar: " + str(elapsed_time))




