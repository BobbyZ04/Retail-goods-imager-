## Background
Environmental issues are gaining concern of the whole society. 
To make the our home and life better, many efforts have been made to protect environment from different kinds of pollution.
Garbage Classification is one of the most efficient way to improve the situation and has been being implemented through the nation.
Many people are still not aware of the exact classification of different kinds of garbage, for example, toxic, recycle, kitchen...
As the department of the environmental protection, we want to build a garbage classifier so that people can classify the garbage more easily.
<br/>So that we could improve the accuracy of garbage classification and reduce the workload for urrban cleaning department.

## Possible Solutions
1.SVM
2.RNN
3.RCNN
4.YOLO

## SVM
# 1.hop features extraction
<br/>parameters selection
<br/>CellSize： A 2-element vector that specifies the size of a HOG cell in pixels. Select larger cell sizes to capture large scale spatial information at the cost of loosing small scale detail.
<br/>BlockSize： A 2-element vector that specifies the number of cells in a block. Large block size values reduce the ability to minimize local illumination changes.
<br/>BlockOverlap： A 2-element vector that specifies the number of overlapping cells between adjacent blocks. Select an overlap of at least half the block size to ensure adequate contrast normalization. Larger overlap values can capture more information at the cost of increased feature vector size. This property has no effect when extracting HOG features around point locations.
<br/>NumBins: A positive scalar that specifies the number of bins in the orientation histograms. Increase this value to encode finer orientation details.
<br/>UseSignedOrientation: A logical scalar. When true, orientation values are binned into evenly spaced bins between -180 and 180 degrees. Otherwise, the orientation values are binned between 0 and 180 where values of theta less than 0 are placed into theta + 180 bins. Using signed orientations can help differentiate light to dark vs. dark to light transitions within an image region.

## Setting up environment
`pip install Tensorflow`Download package for CPU only for more stable performance.
<br/>`pip install tf-nightly`Download package built for CPU/GPU.
<br/>`docker pull tensorflow/tensorflow`use Docker to run tensorflow.`docker run -it -p 8888:8888 tensorflow/tensorflow`Start a Jupyter notebook serve.
<br/>Linux setup `wget http://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.243_418.87.00_linux.run`
<br/>`sudo sh cuda_10.1.243_418.87.00_linux.run`

