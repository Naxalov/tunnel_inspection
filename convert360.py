import argparse
import numpy as np
from PIL import Image
import cv2
import py360convert
import pathlib

def getPerspective(img):
    h_fov = 95
    v_fov = 95
    u_deg = 0
    v_deg = 0
    in_rot_deg = 0
    h,w = 512,512
    ceiling = py360convert.e2p(img, fov_deg=(h_fov, v_fov), u_deg=u_deg, v_deg=v_deg+90,
                            out_hw=(h, w), in_rot_deg=in_rot_deg, mode='bilinear')
                     
    left_wall = py360convert.e2p(img, fov_deg=(h_fov, v_fov), u_deg=u_deg, v_deg=v_deg+180,
                            out_hw=(h, w), in_rot_deg=in_rot_deg-180, mode='bilinear')  
    right_wall = py360convert.e2p(img, fov_deg=(h_fov, v_fov), u_deg=u_deg, v_deg=v_deg+0,
    out_hw=(h, w), in_rot_deg=in_rot_deg, mode='bilinear')      
    return ceiling,left_wall,right_wall

DIR = list(pathlib.Path('data/hallway').iterdir())
for idx,p in enumerate(sorted(DIR)):
    img = cv2.imread(str(p))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# Output image

# Output for list

    out = getPerspective(img)

    Image.fromarray(out[0].astype(np.uint8)).save(f'output/ceiling/{idx}.jpg')
    Image.fromarray(out[1].astype(np.uint8)).save(f'output/left/{idx}.jpg')
    Image.fromarray(out[2].astype(np.uint8)).save(f'output/right{idx}.jpg')