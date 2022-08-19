from __future__ import division
from deshadower import *
import argparse
import glob
import numpy as np
import os
import sys
 
def prepare_image_from_filename(image_filename):
    img = cv2.imread(image_filename, cv2.IMREAD_ANYCOLOR)
    return prepare_image(img)
 
def prepare_image(img, test_w = -1, test_h = -1):
    if test_w >0 and test_h > 0:
        if img.shape[-1] == 4:
            img = cv2.cvtColor(img , cv2.COLOR_BGRA2BGR)
        img = cv2.resize( np.float32(img), (test_w, test_h), cv2.INTER_CUBIC)
    return img/255.0        
 
if __name__ == '__main__':
 
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", help="path to folder containing the model", required=True)
    parser.add_argument("--vgg_19_path", help="path to vgg 19 path model", required=True)
    parser.add_argument("--input_dir", default='./Samples', help="path to sample images")
    parser.add_argument("--use_gpu", default=0, type=int, help="which gpu to use")
    parser.add_argument("--is_hyper", default=1, type=int, help="use hypercolumn or not")
    parser.add_argument("--result_dir", default='results', help="path to the result dir")
 
    ARGS = parser.parse_args()
    test_w,test_h = 512,512
 
    deshadower = Deshadower( ARGS.model, ARGS.vgg_19_path, ARGS.use_gpu, ARGS.is_hyper)
 
    if not os.path.isdir(ARGS.result_dir):
        os.makedirs(ARGS.result_dir)
        
    for image_filename in sorted(glob.glob(ARGS.input_dir+'/*.png')):
        img = cv2.imread( image_filename, -1)
        img = prepare_image(img, test_w, test_h)
        oimg = deshadower.run(img)
        if not os.path.isdir(ARGS.result_dir):
            os.makedirs(ARGS.result_dir)
        output_filename = "%s/%s.png"%(ARGS.result_dir, os.path.splitext(os.path.basename(image_filename))[0])
        # output-image
        cv2.imwrite(output_filename, oimg[0]) 