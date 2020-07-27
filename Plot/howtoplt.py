import argparse
import pyrealsense2 as rs
import numpy as np
import cv2
import os
import pickle
import time
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, Normalize
from scipy.io import wavfile
import scipy.signal as signal
import imageio
import glob
import seaborn as sns
sns.set()

def add_border(img, color, border_size):
    top, bottom, left, right = [border_size]*4
    img_with_border = cv2.copyMakeBorder(
        img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    return img_with_border

def audio_vis(args, wave=False):
    datapath = 'Audio3D-Dataset/Processed'
    audio_path = os.path.join(datapath, args.input, 'sound.wav')
    samplingFrequency, signalData = wavfile.read(audio_path)
    signalData = np.mean(signalData, axis=1)
    plt.figure(figsize=(10,1))

    if wave:
        # color="#ff726f" c='#6495ed'
        plt.plot(signalData, color='#ff726f', linewidth=1, markersize=1)
    else:
        plt.specgram(signalData, Fs=samplingFrequency, cmap='plasma')
        plt.ylim(0, 1000)
        plt.xlim(1, 18)
    plt.axis('off')
    plt.savefig('audio.png', dpi=500)


def get_gray_cmap(N=10, start=180, end=80):
    rtn = []
    offset = (end-start)//(N-1)
    for i in range(N):
        rtn.append(np.ones(3)*(start+offset*i)/255)
    return np.array(rtn)



def depth_vis(args):
    datapath = 'Audio3D-Dataset/Processed'
    depth_path = os.path.join(datapath, args.input, 'depth')
    depth_frame = glob.glob('%s/*.png' % depth_path)
    depth_frame.sort()
    
    fig, ax = plt.subplots(nrows=1, ncols=8, figsize=(10, 1))
    for i in range(1, 9):
        img_path = depth_frame[i*28]
        img = imageio.imread(img_path) / 255 * 10
        img[img > 0.7] = img.mean()
        # print(img.min())
        # print(img.max())
        # print('---')
        #pdb.set_trace()
        #img = np.log(img)
        # color = [255, 114, 111]
        # img = add_border(img, color, border_size=20)
        #cmap = ListedColormap(get_gray_cmap())
        ax[i-1].imshow(img, cmap='rainbow', norm=Normalize(0, 0.85, clip=True))
        ax[i-1].axis('off')
    fig.tight_layout(pad=0.2)
    plt.savefig('depth.png', dpi=500)



def rgb_vis(args):
    datapath = 'Audio3D-Dataset/Processed'
    rgb_path = os.path.join(datapath, args.input, 'rgb')
    rgb_frame = glob.glob('%s/*.jpg' % rgb_path)
    rgb_frame.sort()

    fig, ax = plt.subplots(nrows=1, ncols=8, figsize=(10, 1))
    for i in range(1, 9):
        img_path = rgb_frame[i*28]
        img = imageio.imread(img_path)
        # color = [100, 149, 237]
        color = [94, 98, 99]

        img = add_border(img, color, border_size=15)
        ax[i-1].imshow(img)
        ax[i-1].axis('off')
    fig.tight_layout(pad=0.2)
    plt.savefig('rgb.png', dpi=500)


if __name__ == "__main__":
    
    # cmap = get_gray_cmap()
    # sns.palplot(cmap)
    # exit()
    parser = argparse.ArgumentParser(description="Scene Selection.")

    # Add argument which takes path to a bag file as an input
    parser.add_argument("-i", "--input", type=str,
                        help="Path to the scene path", required=True)

    # Parse the command line arguments to an object
    args = parser.parse_args()
    audio_vis(args, wave=True)
    depth_vis(args)
    rgb_vis(args)
