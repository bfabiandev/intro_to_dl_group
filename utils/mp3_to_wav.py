#!/usr/local/bin/python3
import os
import argparse

import pydub
from tqdm import tqdm


FROM_DIR="mp3_input/"
TO_DIR="wav_output/"

def main(input_dir, output_dir):

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    mp3s, m4as = [], []
    print("Scanning Songs...")
    for path, dirs, files in tqdm(os.walk(input_dir)):
        for f in files:
            if f.endswith(".mp3") or f.endswith(".m4a"):
                 mp3s.append(os.path.join(path,f))

    print("Converting Songs...")
    for song in tqdm(mp3s):
        filename = os.path.split(song)[-1]
        s = filename[:-4] + ".wav"
        pydub.AudioSegment.from_file(song).export(os.path.join(output_dir,s), format="wav")

    print("Done.")

def parse_args():
    p = argparse.ArgumentParser(description='Convert mp3s/m4as to wav files')
    p.add_argument(
            '--from-dir', '-f',
            dest='input_dir',
            required=True,
            help='Directory containing mp3\'s and/or m4a\'s')
    p.add_argument(
            '--output-dir', '-o',
            dest='output_dir',
            default="output_wav",
            help='Directory to output wav files')
    return vars(p.parse_args())

if __name__=='__main__':
    main(**parse_args())

