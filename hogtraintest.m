%% SVM training with hog features,1 VS 1
%% data set, for training and testing
imdsTrain = imageDatastore('D:\EC601\garbageclaasification\image\svm_images\dataset-resized\dataset-resized',...  
   'IncludeSubfolders',true,...  
   'LabelSource','foldernames');
imdsTest = imageDatastore('D:\EC601\garbageclaasification\image\svm_images\newtest');


%% display training pics with their labels and count
Train_disp = countEachLabel(imdsTrain);
disp(Train_disp);

%% extract hog features of every training pic and testing pic
% preprocess, to get the size of the features, which is relevent to Hog features parameters   
imageSize = [256,256];% resize every image into this size
image1 = readimage(imdsTrain,1);
scaleImage = imresize(image1,imageSize);
[features, visualization] = extractHOGFeatures(scaleImage);
imshow(scaleImage);hold on; plot(visualization) 

% extracting features of training pics 
numImages = length(imdsTrain.Files);
featuresTrain = zeros(numImages,size(features,2),'single'); % featuresTrain single accuracy 
for i = 1:numImages 
   imageTrain = readimage(imdsTrain,i); 
   imageTrain = imresize(imageTrain,imageSize); 
   featuresTrain(i,:) = extractHOGFeatures(imageTrain); 
end 

% labels of all the training pics
trainLabels = imdsTrain.Labels;

% svm multi-classification: fitcsvm-dichotomous data, fitcecoc-multi classification, 1VS1 method   
classifer = fitcecoc(featuresTrain,trainLabels); 

%% classification and display 
numTest = length(imdsTest.Files); 
for i = 1:numTest
   testImage = readimage(imdsTest,i);
   scaleTestImage = imresize(testImage,imageSize); 
   featureTest = extractHOGFeatures(scaleTestImage); 
   [predictIndex,score] = predict(classifer,featureTest); 
   figure;imshow(testImage); 
   title(['predictresult: ',char(predictIndex)]); 
end
