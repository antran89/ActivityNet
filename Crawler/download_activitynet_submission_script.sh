#!/bin/sh
#PBS -N download_ActivityNet
#PBS -l select=1:ncpus=24:mem=32GB
#PBS -l walltime=24:00:00
#PBS -q normal
#PBS -j oe
#PBS -o log_job.txt
#PBS -M tranlaman@gmail.com
#PBS -m "e"


#cd /home/users/nus/a0081742/Downloads/opencv-new
#git clone https://github.com/opencv/opencv.git
#git clone https://github.com/opencv/opencv_contrib.git

#cd /home/users/nus/a0081742/Desktop/caffe-workspace/my-very-deep-caffe
#git clone https://github.com/antran89/my-very-deep-caffe.git
cd /home/users/nus/a0081742/Desktop/workspace/ActivityNet/Crawler
./fetch_activitynet_videos.sh /home/users/nus/a0081742/data/ActivityNet_v1.3_res128 activity_net.v1-3.min.json 24

