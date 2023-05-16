import sys
import os

file_name = sys.argv[1]
root = "/home/people/22204840/APC_pert/data/LibriSpeech/train-clean-2_25"
file_name=file_name.split('.')[0]
reader, chapter, _ = file_name.split('-')

if not os.path.exists(os.path.join(root,reader)):
 os.makedirs(os.path.join(root,reader))
if not os.path.exists(os.path.join(root, reader,chapter)):
 os.makedirs(os.path.join(root, reader, chapter))

print("Done")

