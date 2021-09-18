import os
import functionsWin as win

# ESCENARI 1 - Video de 12 segons
# Ajustem els paràmetres d'entrada
videoOriginal = str("dron4K.mp4")
fps = 25
duration = 12
video12sec = str("video12sec.mp4")
win.filterVideo(videoOriginal, fps, duration, video12sec)
os.system("python3 upDownsampler.py")

# ESCENARI 2 - Video de 1 min (60 segons)
# Ajustem els paràmetres d'entrada
videoOriginal = str("dron4K.mp4")
fps = 25
duration = 60
video1min = str("video60sec.mp4")

win.filterVideo(videoOriginal, fps, duration, video1min)
os.system("python3 upDownsampler.mp4")