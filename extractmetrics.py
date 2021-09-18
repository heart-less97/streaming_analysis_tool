from time import time
import os
import functionsWin as win

ori = str("video12sec.mp4")
folderTest = str("folderTest/")
testName = str("concat_")
start_time = time()

for i in range(1,21):
    win.extractMetricsFromFiles(ori, folderTest + testName + str(i) + ".mp4", i)

elapsed_time = time() - start_time

print("Ha tardat en executar: " + str(elapsed_time))
