#!/bin/zsh
export LD_LIBRARY_PATH=~/openpose/3rdparty/caffe/build/lib:$LD_LIBRARY_PATH
alias openpose='~/openpose/build/examples/openpose/openpose.bin' # set your own openpose directory
dir='interaction_data'

for folder in $(ls $dir); do
    subfolder=${dir}"/$folder"
    for action_clip in $(ls $subfolder);do 
        echo $action_clip|grep -Eo '*[0-9]+.avi'|grep -Eo '[0-9]+'
        newfolder=$(echo $action_clip|grep -Eo '*[0-9]+.avi'|grep -Eo '[0-9]+')
        mkdir ${subfolder}"/$newfolder"
        openpose --video ${subfolder}"/$action_clip" -write_json ${subfolder}"/$newfolder" --display 0 --render_pose 0
    done
done

