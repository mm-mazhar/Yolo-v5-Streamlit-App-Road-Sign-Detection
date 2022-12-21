import os
from random import choice
import shutil
import zipfile
import tarfile


def main():
    #arrays to store file names
    imgs =[]
    txts =[]

    IMAGES_PATH = os.path.join('.', 'dataset', 'images')
    print(IMAGES_PATH)
    
    print("Spliting into Test and Train Dirs...........")
    #SETUP DIRECTORIES FOR TRAIN, TEST
    trainPath = os.path.join(IMAGES_PATH, 'train')
    if not os.path.exists(trainPath):
        os.makedirs(trainPath)
        
    testPath = os.path.join(IMAGES_PATH, 'test')
    if not os.path.exists(testPath):
        os.makedirs(testPath)
                
    crsPath = IMAGES_PATH #dir where images and annotations stored

    #setup ratio (val ratio = rest of the files in origin dir after splitting into train and test)
    train_ratio = 0.8
    test_ratio = 0.2 
    
    #total count of imgs
    totalImgCount = len(os.listdir(crsPath))/2
    #totalImgCount

    #sorting files to corresponding arrays
    for (dirname, dirs, files) in os.walk(crsPath):
        for filename in files:
            if filename.endswith('.txt'):
                txts.append(filename)
            else:
                imgs.append(filename)
                

    #counting range for cycles
    countForTrain = int(len(imgs)*train_ratio)
    countForTest = int(len(imgs)*test_ratio)


    #cycle for train dir
    for x in range(countForTrain):

        imagFile = choice(imgs) # get name of random image from origin dir
        fileTxt = imagFile[:-4] +'.txt' # get name of corresponding annotation file

        #move both files into train dir
        shutil.move(os.path.join(crsPath, imagFile), os.path.join(trainPath, imagFile))
        shutil.move(os.path.join(crsPath, fileTxt), os.path.join(trainPath, fileTxt))

        #remove files from arrays
        imgs.remove(imagFile)
        txts.remove(fileTxt)


    #cycle for test dir   
    for x in range(countForTest):

        imagFile = choice(imgs) # get name of random image from origin dir
        fileTxt = imagFile[:-4] +'.txt' # get name of corresponding annotation file

        #move both files into train dir
        shutil.move(os.path.join(crsPath, imagFile), os.path.join(testPath, imagFile))
        shutil.move(os.path.join(crsPath, fileTxt), os.path.join(testPath, fileTxt))

        #remove files from arrays
        imgs.remove(imagFile)
        txts.remove(fileTxt)

    # #move remaining files to test folder
    txts = []
    imgs = []
    for files in os.listdir(crsPath):
        if files[-4:] == ".txt":
            txts.append(files)
        if files[-4:] == ".png" or files[-4:] == ".jpg":
            imgs.append(files)
        
      
    if len(txts) == len(imgs):
        for i in range(len(txts)):
            EX_PATH = os.path.join(IMAGES_PATH, txts[i])
            NEW_PATH = os.path.join(IMAGES_PATH, 'test', txts[i])
            os.replace(EX_PATH, NEW_PATH)
            EX_PATH = os.path.join(IMAGES_PATH, imgs[i])
            NEW_PATH = os.path.join(IMAGES_PATH, 'test', imgs[i])
            os.replace(EX_PATH, NEW_PATH)

    #summary information after splitting
    print('Total images: ', totalImgCount)
    print('Images in train dir:', len(os.listdir(trainPath))/2)
    print('Images in test dir:', len(os.listdir(testPath))/2)
    
    newTrainPathImages = os.path.join('.', 'dataset', 'train', 'images')
    newTrainPathLabels = os.path.join('.', 'dataset', 'train', 'labels')
    newTestPathImages = os.path.join('.', 'dataset', 'test', 'images')
    newTestPathLabels = os.path.join('.', 'dataset', 'test', 'labels')
    
    if not os.path.exists(newTrainPathImages):
        os.makedirs(newTrainPathImages)
        
    if not os.path.exists(newTrainPathLabels):
        os.makedirs(newTrainPathLabels)
    
    if not os.path.exists(newTestPathImages):
        os.makedirs(newTestPathImages)
    
    if not os.path.exists(newTestPathLabels):
        os.makedirs(newTestPathLabels)
        
    for files in os.listdir(os.path.join('.', 'dataset', 'images', 'train')):
        if files[-4:] == ".png" or files[-4:] == ".jpg":
            os.replace(os.path.join('.', 'dataset', 'images', 'train', files), os.path.join(newTrainPathImages, files))
        if files[-4:] == ".txt":
            os.replace(os.path.join('.', 'dataset', 'images', 'train', files), os.path.join(newTrainPathLabels, files))
            
    for files in os.listdir(os.path.join('.', 'dataset', 'images', 'test')):
        if files[-4:] == ".png" or files[-4:] == ".jpg":
            os.replace(os.path.join('.', 'dataset', 'images', 'test', files), os.path.join(newTestPathImages, files))
        if files[-4:] == ".txt":
            os.replace(os.path.join('.', 'dataset', 'images', 'test', files), os.path.join(newTestPathLabels, files))
            
    shutil.rmtree(os.path.join('.', 'dataset', 'images'))
        
    #Compressing
    print("Compressing....................")
    ARCHIVE_PATH = os.path.join('.', 'dataset', 'archive.tar.gz')
    testPath = os.path.join('dataset', 'test')
    trainPath = os.path.join('dataset', 'train')
    
    with tarfile.open(ARCHIVE_PATH, "w:gz") as tarhandle:
        tarhandle.add(testPath)
        tarhandle.add(trainPath)
    
if __name__ == '__main__':
    main() 