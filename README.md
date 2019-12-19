## Background
Environmental issues are gaining concern of the whole society. 
To make the our home and life better, many efforts have been made to protect environment from different kinds of pollution.
Garbage Classification is one of the most efficient way to improve the situation and has been being implemented through the nation.
Many people are still not aware of the exact classification of different kinds of garbage, for example, toxic, recycle, kitchen...
As the department of the environmental protection, we want to build a garbage classifier so that people can classify the garbage more easily.
<br/>So that we could improve the accuracy of garbage classification and reduce the workload for urrban cleaning department.

## Possible Solutions
1.SVM
2.CNN

## Folders in this Project 
<br/>data-resized is for the data training data
<br/>architecture is the input and output for the whole system.
<br/>hogsvm is the SVM algorithm in MATLAB.
<br/>tensorflow-CNN is the CNN algorithm in python. 
<br/>results-example shows the result of the two methods we implemented.
<br/>confusion matrix is the confusion matrix of our method. Showing the result of the prediction.


## SVM
### 1.hop features extraction
parameters selection
<br/>CellSize： A 2-element vector that specifies the size of a HOG cell in pixels. Select larger cell sizes to capture large scale spatial information at the cost of loosing small scale detail.
<br/>BlockSize： A 2-element vector that specifies the number of cells in a block. Large block size values reduce the ability to minimize local illumination changes.
<br/>BlockOverlap： A 2-element vector that specifies the number of overlapping cells between adjacent blocks. Select an overlap of at least half the block size to ensure adequate contrast normalization. Larger overlap values can capture more information at the cost of increased feature vector size. This property has no effect when extracting HOG features around point locations.
<br/>NumBins: A positive scalar that specifies the number of bins in the orientation histograms. Increase this value to encode finer orientation details.
<br/>UseSignedOrientation: A logical scalar. When true, orientation values are binned into evenly spaced bins between -180 and 180 degrees. Otherwise, the orientation values are binned between 0 and 180 where values of theta less than 0 are placed into theta + 180 bins. Using signed orientations can help differentiate light to dark vs. dark to light transitions within an image region.
### 2.1-v-1 SVMs
number = k(k-1)/2



## cnn
### Setting up environment
`pip install Tensorflow`Download package for CPU only for more stable performance.
<br/>`pip install tf-nightly`Download package built for CPU/GPU.
<br/>`docker pull tensorflow/tensorflow`use Docker to run tensorflow.`docker run -it -p 8888:8888 tensorflow/tensorflow`Start a Jupyter notebook serve.

<br/>Docker is a platform for developers and sysadmins to build, share, and run applications with containers. 
Fundamentally, a container is nothing but a running process, with some added encapsulation features applied to it in order to keep it isolated from the host and from other containers.

<br/>Linux setup `wget http://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.243_418.87.00_linux.run`
<br/>`sudo sh cuda_10.1.243_418.87.00_linux.run`

![avatar](/user/desktop/docker.png)
<br/>after setting up the docker container, start the machine we need `$ docker-machine start`
<br/>start the tensorflow`$ docker run -it tensorflow/tensorflow bash`
<br/>download jupyter notebook as coding environment.`docker run --remove -P jupyter/base-notebook`
<br/>run tensorflow from jupyter.`docker run -it -p 8888:8888 tensorflow/tensorflow:nightly-py3-jupyter`
<br/>got http://127.0.0.1:8888/?token=xxx from the docker container, enter into it to run the jupyter for NN algorithms.
<br/>To get a quick show of our thoughts, we decided to import `kera` which is an api developed by tensorflow supporting neural networks and GPU/CPU modes.
<br/>
<br/>To enter the folders and programs we added before, use `$ docker start bold_bhabha`, `$ docker attach bold_bhabha` which is the name of our container. Then use `root@996b36841914:/tf# jupyter notebook --ip 0.0.0.0 --allow-root --port 8888 --no-browser` to check the token of our jupyter notebook so we can use it in the browser.

### main function
</br> the main function is uploaded, also with the dataset.

</br> We just followed the tutorial of Tensorflow, in Jupyternotebook, which includes a MIT liscense. The tutorial document is easy to understand but too simple, so I graded it for 3. We modified the model by adding 3 convolution layrs and pooling. Changed the dense, batch, imagesize and epoch attributes. We also added our own dataset to train and test rather than using the dataset in Kera API. Finally we output our presiction results in images with labels which is not accomplished in the original document.
https://www.tensorflow.org/tutorials/keras/classification
</br> totally 2391 images in 5 categories: cardboard, glass, metal, paper and plastic. The quality of photos is good with different kinds and different angles of objects.
https://github.com/zhangb96/Retail-goods-imager-/tree/master/dataset-resized/dataset-resized 
</br> SVM in Matlab and CNN(kera model) in Tensorflow, run by jupyter in Docker Container in Win10.
For SVM, the key part is the feature extraction, to exract color, shape of different objects. Then we applied the function 'fitcecoc(featuresTrain,trainLabels)' in MATLAB, and had our results printed out. For this part we did not use any additional open resources. The result is good with clean background images but had problem recognizing objects in noisy background.
For CNN in Tensorflow, we did a huge amount of work setting up environments in Windows like Docker, Jupyter, Tensorflow etc. We ran the tensorflow tutorial and find the classification result of CNN was pretty good and had high efficiency. So we modified the model in Tensorflow(kera API), added 3 convolution and pooling layers, parameters, dataset of our own and achieved an accuracy over 0.94 and loss less then 0.15, which is quite exciting. We tested images with noisy background and it successfully classified them. The whole classification process is short even we cannot notice it, quite efficient for our work. So the model is good to choose in our opinion.  

