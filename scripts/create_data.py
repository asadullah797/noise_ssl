import sys
import os
import shutil

file_name = sys.argv[1]
source = "/home/people/22204840/APC_pert/data/LibriSpeech/train-clean-100"
dest   = "/home/people/22204840/APC_pert/data/LibriSpeech/train-clean-50"

file_name=file_name.split('/')[-1].split('.')[0]
read, chap, _ = file_name.split('-')
new_file = file_name+'.flac'
print('file_name', file_name)

for readers in os.listdir(source):
 if read == readers:
  for chapters in os.listdir(os.path.join(source,readers)):
   if chap == chapters:
    for wav_file in os.listdir(os.path.join(source, readers, chapters)):
     if new_file == wav_file:
      if not os.path.exists(os.path.join(dest,readers,chapters)): 
       os.makedirs(os.path.join(dest, readers, chapters))
      shutil.copy(os.path.join(source, readers, chapters, wav_file), os.path.join(dest, readers, chapters))
      shutil.copy(os.path.join(source, readers, chapters, readers+"-"+chapters+".trans.txt"), os.path.join(dest, readers, chapters))
