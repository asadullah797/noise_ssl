import sys
import math
import os
import shutil
import glob
import random
import librosa
import numpy as np
from scipy.io.wavfile import write

source = "/home/people/22204840/scratch/22204840/data/data/LibriSpeech/train-clean-100"
dest   = "/home/people/22204840/scratch/22204840/data/data/LibriSpeech/train_clean25_aug75"
sampling_rate=16000
noises= glob.glob("musan/noise/free-sound/*.wav")

def add_noise(x, s, snr_db):

  # First let's match the length of the two signals
  x_len = x.shape[0]
  s_len = s.shape[0]

  if x_len > s_len:
    # Calculate how many times we need to repeat the signal and round up to the nearest integer
    reps = math.ceil(x_len/s_len)

    # Use the function np.tile to repeat an array
    s = np.tile(s, reps)

  # Truncate the background signal
  s = s[:x_len]

  # Check if the lengths are the same
  assert x_len == s.shape[0]

  # Convert SNRdb to linear
  snr = 10**(snr_db/10)

  # Estimate noise and signal power
  sp = np.sqrt(np.mean(s**2))
  xp = np.sqrt(np.mean(x**2))

  # Calculate desired noise power based on the SNR value
  sp_target = xp/snr

  # Scale factor noise signal
  alpha = sp_target/sp
  print(f'alpha={alpha}')
  # Sum speech and background noise
  y = x + alpha*s
  return y

i=0
count=0
counter = 0
for readers in os.listdir(source):
  for chapters in os.listdir(os.path.join(source,readers)):
    for wav_file in os.listdir(os.path.join(source, readers, chapters)):
      if not os.path.exists(os.path.join(dest,readers,chapters)): 
       os.makedirs(os.path.join(dest, readers, chapters))
      if wav_file.endswith('.flac'):
          x, _ = librosa.load(os.path.join(source, readers, chapters, wav_file), sr=sampling_rate, mono=True)
          if counter < 14270:
              noise_filename = noises[count%len(noises)]
              count = count+1
              #counter = counter+1
              s, _ = librosa.load(noise_filename, sr=sampling_rate, mono=True)
              snr_dbs = [5, 10, 15]
              y = add_noise(x, s, snr_db=snr_dbs[i%len(snr_dbs)])
              i=i+1       
              new_wav_file= wav_file.split('/')[-1].split('.')[0]+"-aug1"+".flac"
              write(os.path.join(dest, readers, chapters, new_wav_file), sampling_rate, y) 

              noise_filename = noises[count%len(noises)]
              count = count+1
              #counter = counter+1
              s, _ = librosa.load(noise_filename, sr=sampling_rate, mono=True)
              snr_dbs = [5, 10, 15]
              y = add_noise(x, s, snr_db=snr_dbs[i%len(snr_dbs)])
              i=i+1
              new_wav_file= wav_file.split('/')[-1].split('.')[0]+"-aug2"+".flac"
              write(os.path.join(dest, readers, chapters, new_wav_file), sampling_rate, y)

              noise_filename = noises[count%len(noises)]
              count = count+1
              #counter = counter+1
              s, _ = librosa.load(noise_filename, sr=sampling_rate, mono=True)
              snr_dbs = [5, 10, 15]
              y = add_noise(x, s, snr_db=snr_dbs[i%len(snr_dbs)])
              i=i+1
              new_wav_file= wav_file.split('/')[-1].split('.')[0]+"-aug3"+".flac"
              write(os.path.join(dest, readers, chapters, new_wav_file), sampling_rate, y)

          shutil.copy(os.path.join(source, readers, chapters, wav_file), os.path.join(dest, readers, chapters))
      shutil.copy(os.path.join(source, readers, chapters, readers+"-"+chapters+".trans.txt"), os.path.join(dest, readers, chapters))

print('i=', i)
print('count=', count)
print('counter=', counter)

