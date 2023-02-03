#this code unpacks and repacks data from:
#16 bit stereo wav file at 44100hz sampling rate
#to:
##16 bit mono wav file at 44100hz sampling rate

import wave
import struct

bitDepth = 8 # target bitDepth
frate = 44100 # target frame rate

fileName = "space.wav" # file to be imported (change this)
#read file and get data

w = wave.open(fileName, "rb")
numframes = w.getnframes()

frame = w.readframes(numframes) # w.getnframes()

frameInt = list(struct.unpack("<" + "h" * int(len(frame) / 2), frame))
#separate left and right channels and merge bytes

frameOneChannel = [0] * numframes # initialize list of one channel of wave
for i in range(numframes):
frameOneChannel[i] = frameInt[2 * i + 1] * 2 ** 8 + frameInt[2 * i]
if frameOneChannel[i] > 2 ** 15:
frameOneChannel[i] = frameOneChannel[i] - 2 ** 16
elif frameOneChannel[i] == 2 ** 15:
frameOneChannel[i] = 0
else:
frameOneChannel[i] = frameOneChannel[i]
#convert to string

audioStr = ",".join(map(str, frameOneChannel))

fileName = fileName[:-4] # remove .wav extension
with open(fileName + ".txt", "w") as text_file:
