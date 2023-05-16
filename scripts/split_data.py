import sys
import os
import shutil


source = "/home/people/22204840/APC/APC_50/data/LibriSpeech/train-clean-100"
dest   = "/home/people/22204840/APC/APC_50/data/LibriSpeech/train-clean-african"
count=0
def copy_data():
 count = 0
 for readers in os.listdir(source):
   for chapters in os.listdir(os.path.join(source,readers)):
     for wav_file in os.listdir(os.path.join(source, readers, chapters)):
       if wav_file.endswith('.flac'):
         count = count + 1
       #if count == 14270:
       # return count
       if not os.path.exists(os.path.join(dest,readers,chapters)): 
        os.makedirs(os.path.join(dest, readers, chapters))
       if wav_file.endswith('.txt'):
         shutil.copy(os.path.join(source, readers, chapters, wav_file), os.path.join(dest, readers, chapters))

count = copy_data()
print('count', count)
