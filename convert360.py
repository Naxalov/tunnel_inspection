import argparse
import numpy as np
from PIL import Image
import cv2
import py360convert
import pathlib
img = cv2.imread('example/00000.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
h_fov = 95
v_fov = 95
u_deg = 0
v_deg = 90+180
in_rot_deg = -5
h,w = 1024,1024
out = py360convert.e2p(img, fov_deg=(h_fov, v_fov), u_deg=u_deg, v_deg=v_deg,
                           out_hw=(h, w), in_rot_deg=in_rot_deg, mode='bilinear')


# Output image

# Output for list

Image.fromarray(out.astype(np.uint8)).save('test.jpg')