from  PIL import Image
import argparse
import numpy as np
class AsciiGenerator:
    def __init__(self,filename,size:tuple=(100,100)):
        self.filename=filename
        self.size = size
    def read(self):
        try:
            img = Image.open(self.filename)
            img = img.resize(self.size)
            img = img.convert('L')
            return img
        except Exception as e:
            print(f'[!] An Error occured-> {e}')

    def to_ascii(self,f=None,chars="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "):
        img = self.read()
        w,h = self.size
        ascii_img_chars = [chars[int(i)] for i in (np.array(list(img.getdata()))//3.7)-1]
        ascii_img = ''
        for i in range(h):
            ascii_img+=''.join(ascii_img_chars[:w])+'\n'
            ascii_img_chars = ascii_img_chars[w:]
        self.ascii_img = ascii_img
        if f:
            self.save(f)

    def save(self,f):
        f = open(f,'w')
        f.write(self.ascii_img)
        f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A program to convert Images to ascii art'
    )

    parser.add_argument('img',help='Image filepath')
    parser.add_argument('w',help='Output Width')
    parser.add_argument('h',help='Output Height')
    parser.add_argument('s',help='Output file')
    
    args = parser.parse_args()
    
    f,w,h,s = args.img,args.w,args.h,args.s

    Gen = AsciiGenerator(f,size=(int(w),int(h)))
    Gen.to_ascii(s)