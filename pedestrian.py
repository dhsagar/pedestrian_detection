#import libraries
from function import *

#load fullbody cascade to a fullbody classifier
fullbody_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

def main():
    videopipeline('input.avi')

if __name__ == "__main__":
    main()
