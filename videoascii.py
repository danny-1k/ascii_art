import os
from main import AsciiGenerator
import time
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--fps',help='Fps to play video. Eg 25, 30')
args = parser.parse_args()
fps = int(args.fps)
ext = os.listdir('frames')[0][-4:]
for i in sorted([int(i[:-4]) for i in os.listdir('frames')]):
    Gen = AsciiGenerator('frames'+f'/{i}{ext}',size=(120,50))
    Gen.to_ascii()
    print(Gen.ascii_img,end='')
    time.sleep(1/fps)
