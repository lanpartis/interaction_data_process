#conding=utf-8
'''
this script is to split the raw video data to video clips that contain one interaction.

Input:
video data is in folder 'video_data'
'labeled_clips.data' contains many rows, in each row there are <file name> <start_point> <duration> <label>

Output:
output is a folder 'interaction_data',
inside are folders of each label.
These sub folders contain video clips of the same label.
'''
import ffmpy
import pandas as pd
import os
import sys
fps =11
video_dir = 'video_data'
output_dir = 'interaction_data'
label_dir = 'labeled_clips.data'
label_table = pd.read_table(label_dir,encoding='utf-8',delim_whitespace=True,verbose=True)
counter = {}
for index,row in label_table.iterrows():
    cmd = '-r %d -ss %d -t %d'%(fps,row['start'],row['duration'])
    file_dir='%s/%s'%(video_dir,row['name'])
    out_dir='%s/%s'%(output_dir,row['label'])
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    out_dir=out_dir+'/'+str(counter.get(row['label'],1))
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    clip=ffmpy.FFmpeg(
        inputs={file_dir:None},
        outputs={out_dir+'/'+'%03d.png':cmd}
    )
    counter[row['label']] = counter.get(row['label'],1)+1
    clip.run()
