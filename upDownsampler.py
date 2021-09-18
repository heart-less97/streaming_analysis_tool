import os
import functionsWin as win

# Creem les diferents carpetes necessaries
folderTest = win.createFolder("folderTest\\")   #format Windows
folder4k = win.createFolder("folder4k\\")
folder2k = win.createFolder("folder2k\\")
folder1k = win.createFolder("folder1k\\")

#Creem els noms dels vídeosi les qualitats
inputVideo12sec = str("video12sec.mp4")
down12sec = str("down12sec.mp4")
down60sec = str("down60sec.mp4")
up1k12s = str("video12s_1kto4k.mp4")
up2k12s = str("video12s_2kto4k.mp4")
up1k60s = str("video60s_1kto4k.mp4")
up2k60s = str("video60s_2kto4k.mp4")
inputVideo12sec = str("video12sec.mp4")

quality1k = str("1k")
quality2k = str("2k")

# ESCENARI 1
# Downsampling
# 12 sec
win.doDownsampling(inputVideo12sec, quality1k, down12sec)
win.doDownsampling(inputVideo12sec, quality2k, down12sec)
# Upsampling
# 12 sec
win.doUpsampling(down12sec, folderTest, up1k12s, folder1k)
win.doUpsampling(down12sec, folderTest, up2k12s, folder2k)

# ESCENARI 2
# Downsampling
# 60 sec
win.doDownsampling(inputVideo12sec, quality1k, down60sec)
win.doDownsampling(inputVideo12sec, quality2k, down60sec)
# Upsampling
# 60 sec
win.doUpsampling(down12sec, folderTest, up1k60s, folder1k)
win.doUpsampling(down12sec, folderTest, up2k60s, folder2k)

os.system("python3 videoCutter.py")

