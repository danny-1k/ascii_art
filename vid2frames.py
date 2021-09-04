import cv2 
import os
import argparse

def save_frames(f):
    cam = cv2.VideoCapture(f)
    if not os.path.exists('frames'):
        os.makedirs('frames') 

    currentframe = 0
    while(True):
        ret,frame = cam.read()
        if ret:
            name = 'frames/' + str(currentframe) + '.jpg'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)
            currentframe += 1
        else: 
            break

    cam.release() 
    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video',help='Video file')
    args = parser.parse_args()

    f = args.video

    save_frames(f)