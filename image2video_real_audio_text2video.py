import cv2
import numpy as np
import glob
import moviepy.editor as mpe
import sys

#input
import re
import string
from zhon.hanzi import punctuation

img_array = []

person=sys.argv[2]
# person='henan'
# test='weather'

input = sys.argv[1]
stripped_space = re.sub(' ', '', input)
# print('stripped_space', stripped_space)
stripped_input = re.sub(r'[%s]+' %punctuation, '', stripped_space)
file_name = stripped_input[:10]

fps=25

# # smooth interpolation version
anamelist=glob.glob('./results/{person}/test_latest/tmp/fake_B*.jpg'.format(person=person))
anamelist.sort()

out = []
for a_name in anamelist:
    a_img = cv2.imread(a_name)
    a_height, a_width, layers = a_img.shape

    if out==[]:
        out=cv2.VideoWriter('./results/{person}/video.mp4'.format(person=person),
                        cv2.VideoWriter_fourcc(*'MP4V'), fps, (a_width, a_height))
    out.write(a_img)

if out != []:
    out.release()

#add audio
my_clip = mpe.VideoFileClip('./results/{person}/video.mp4'.format(person=person))

# my_clip.write_videofile('./results/{person}/{person}_{test}.mp4'.format(person=person, test=test),
my_clip.write_videofile('./results/{person}/shared_video_output/{person}_{audio}_real_audio.mp4'.format(person=person, audio=file_name),
                        audio='../Text2Video/input_audio_real/{person}/{audio}.mp3'.format(person=person,audio=file_name))

# interpolation + smooth version
# bnamelist=glob.glob('./results/{person}/test_latest/tmp_smooth/fake_B*.jpg'.format(person=person))
# bnamelist.sort()

# out = []
# for b_name in bnamelist:
#     b_img = cv2.imread(b_name)
#     b_height, b_width, layers = b_img.shape

#     if out==[]:
#         out=cv2.VideoWriter('./results/{person}/video_smooth.mp4'.format(person=person),
#                         cv2.VideoWriter_fourcc(*'MP4V'), fps, (b_width, b_height))
#     out.write(b_img)

# if out != []:
#     out.release()

# #add audio
# my_clip = mpe.VideoFileClip('./results/{person}/video_smooth.mp4'.format(person=person))

# # my_clip.write_videofile('./results/{person}/{person}_{test}.mp4'.format(person=person, test=test),
# my_clip.write_videofile('./results/{person}/shared_video_output/{person}_smooth_{audio}_real_audio.mp4'.format(person=person, audio=file_name),
#                         audio='../VisualVirtualCharacter/input_audio_real/{person}/{audio}.mp3'.format(person=person,audio=file_name))
