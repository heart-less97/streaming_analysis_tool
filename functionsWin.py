import os
from subprocess import *
import random
import ffmpeg_quality_metrics

def cutVideoDuration(filename, duration):
    videoCut = "videoCut.mp4"
    os.system("ffmpeg -i " + str(filename) + " -t " + str(duration) + videoCut)
    return videoCut

def deleteAudio(filename):
    videoRes = "withoutAudio.mp4"
    os.system("ffmpeg -i " + str(filename) + " -an " + videoRes)
    return videoRes

def extractDuration(filename):
    extDuration = Popen(['ffprobe', '-v', 'error', '-show_entries', 'stream=duration','-of', 'default=nw=1:nk=1', filename], stdout=PIPE, stderr=STDOUT)
    resDuration = str(extDuration.stdout.readlines())
    duration = str(resDuration[3:resDuration.find('\\')])
    return duration

def extractFps(filename):
    extFps = Popen(['ffprobe', '-v', 'error', '-show_entries', 'stream=r_frame_rate','-of', 'default=nw=1:nk=1', filename], stdout=PIPE, stderr=STDOUT)
    resFps= str(extFps.stdout.readlines())
    fps = resFps[3:resFps.find("/")]
    return fps

def extractBitRate(filename):
    extBitrate = Popen(['ffprobe', '-v', 'error', '-show_entries', 'stream=bit_rate','-of', 'default=nw=1:nk=1', filename], stdout=PIPE, stderr=STDOUT)
    resBitRate= str(extBitrate.stdout.readlines())
    bitrate = resBitRate[3:resBitRate.find("/")]
    return bitrate

def changeFPS(filename):
    os.system("ffmpeg -i " + str(filename) + " -filter:v fps=fps=25 parsed.mp4")
    print("Your new video is parsed.mp4")

def deleteVideo(filename):
    os.system("DEL /F /A " + str(filename))
    print("Video deleted")

def showFrames(filename):
    os.system("ffprobe -v error -hide_banner -of default=noprint_wrappers=0 -print_format flat -select_streams v:0 -show_entries frame=pict_type " + filename)

def createFolder(folderName): 
    os.system("md " + str(folderName))
    return str(folderName)

def copyFile(file, destination, newName):
    os.system("copy "+ str(file) + " " + str(destination) + str(newName) )
    print("Copied succesfully")


def processVideo(videoName, tamSeg, qualitat, duration):

    # Inicialitzem els directoris de recepció 
    folder4k = str("folder4k/")
    folder2k = str("folder2k/")
    folder1k = str("folder1k/")

    # Obrim un fitxer per a guardar les traces
    segmentTrace = open("video_" + str(qualitat) + "_" + str(tamSeg) + ".txt", "w+")

    for i in range(0,duration, tamSeg):
        if i < duration:
            if qualitat == 1:
                os.system("ffmpeg -i " + videoName + " -ss " + str(i) + ".0 -to " + str(i+tamSeg) + ".0 -g 25 -map 0 " + folder1k + "segment_" + str(qualitat) + "_" + str(tamSeg) + "_" + str(i) + ".mp4")
                segmentTrace.write("file " + folder1k + "segment_" + str(qualitat) + "_" + str(tamSeg) +"_" + str(i) + ".mp4" + "\n")
            if qualitat == 2:
                os.system("ffmpeg -i " + videoName + " -ss " + str(i) + ".0 -to " + str(i+tamSeg) + ".0 -g 25 -map 0 " + folder2k + "segment_" + str(qualitat) + "_" + str(tamSeg) + "_" + str(i) + ".mp4")
                segmentTrace.write("file " + folder2k + "segment_" + str(qualitat) + "_" + str(tamSeg) +"_" + str(i) + ".mp4" + "\n")
            if qualitat == 3:
                os.system("ffmpeg -i " + videoName + " -ss " + str(i) + ".0 -to " + str(i+tamSeg) + ".0 -g 25 -map 0 " + folder4k + "segment_" + str(qualitat) + "_" + str(tamSeg) + "_" + str(i) + ".mp4")
                segmentTrace.write("file " + folder4k + "segment_" + str(qualitat) + "_" + str(tamSeg) + "_" + str(i) + ".mp4" + "\n")

    segmentTrace.close()

    return str("video_" + str(qualitat) + "_" + str(tamSeg) + ".txt")


def processRandom(tamSeg, duration, num):
    segmentTrace = open("random_" + str(tamSeg) + ".txt", "w+")

    folder4k = str("folder4k/")
    folder2k = str("folder2k/")
    folder1k = str("folder1k/")

    listQualities = ["1", "2", "4"]

    for i in range(0, duration, tamSeg):
        quality = random.randint(0,2)
        if i < duration:
            if listQualities[quality] == "1":
                segmentTrace.write("file " + str(folder1k) + "segment_1_" + str(num) + "_" + str(i) +  ".mp4 " + "\n")
            elif listQualities[quality] == "2":
                segmentTrace.write("file " + str(folder2k) + "segment_2_" + str(num) + "_" + str(i) + ".mp4 " + "\n")
            elif listQualities[quality] == "4":
                segmentTrace.write("file " + str(folder4k) + "segment_3_" + str(num) + "_" + str(i) + ".mp4 " + "\n")

    segmentTrace.close()
    return str("random_" + str(tamSeg) + ".txt")

# Funció per a filtrar el video amb diferents FPS
# Paràmetres d'entrada:
# video -> Nom del vídeo
# fpsToConvert -> valor actual dels fps del vídeo

def filterVideo(video, fpsToConvert, duration, finalName):
    fpsOri = int(extractFps(video))

    if fpsOri < fpsToConvert or fpsOri > fpsToConvert:
        # Change the FPS 
        changeFPS(video)
        newName = "parsed.mp4"

        # Erase the Audio and return a video
        # named withoutAudio.mp4
        deleteAudio(newName)

        # Erase the last parsed video
        deleteVideo(newName)
        newName = str("withoutAudio.mp4")
    else:
        # Erase the Audio and return a video
        # named withoutAudio.mp4
        deleteAudio(video)
        newName = str("withoutAudio.mp4")
    
    cutVideo(newName, duration, finalName)



# Funció per a tallar un video
# Paràmetres d'entrada:
# video -> Nom del vídeo
# duration -> duració en segons que es vol tallar
# newName -> nom del video tallat

def cutVideo(video, duration, newName):
    os.system("ffmpeg -i " + str(video) + " -ss 00.0 -to " + str(duration) + ".0 -g 25 -map 0 " + newName)


def doDownsampling(video, qualitat, newName):
    folder1k = str("folder1k/")
    folder2k = str("folder2k/")

    if qualitat == "1k":
        os.system("ffmpeg -y -i " + video + " -vf scale=1920x1080 -c:a copy " + folder1k + newName)
        print("Downsampling done")
        
    elif qualitat == "2k":
        os.system("ffmpeg -y -i " + video + " -vf scale=2048x1080 -c:a copy " + folder2k + newName)
        print("Downsampling done")
    

def doUpsampling(video, videoUpsampled, originalFolder = ""):
    os.system("ffmpeg -y -i " + originalFolder + video + " -vf scale=3840x2160 -c:a copy " + videoUpsampled)


def joinWithConcat(inputTxt, outputVideo, folder):
    os.system("ffmpeg -f concat -safe 0 -i " + inputTxt + " -c copy " + folder + outputVideo)

def extractMetricsFromFiles(oriVideo, distVideo, index):
    options = " -m ssim psnr vmaf"
    folderTest = "folderTest/"
    os.system("ffmpeg_quality_metrics " + oriVideo + " " + distVideo + options + " > " + folderTest + "res_" + str(index) + ".txt")
