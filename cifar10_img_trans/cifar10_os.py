# coding: utf-8
# cifar10_os
# Meringue
# 5/4/2017

import numpy as np
import random
import os
import matplotlib.pyplot as plt

## get the total num of images in a directory
def get_img_num(img_path):
    return len(os.listdir(img_path))


## show some images in a directory
def random_show_cifar10(cifar10_path, samples_per_class):
    classes = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    num_classes = len(classes)   
    img_list = os.listdir(cifar10_path)

    for index1, class_name in enumerate(classes):
        img_index_name = [img for img in img_list if(int(img.split('_')[1].split('.')[0])==index1)]
        # print img_index_name
        img_choice = random.sample(img_index_name,samples_per_class)
        # print img_choice
        for index2,img_name in enumerate(img_choice):
            # print index2, img_name
            img = plt.imread(cifar10_path+img_name)
            plt_index = index2*num_classes+index1+1
            plt.subplot(samples_per_class,num_classes,plt_index)
            # plt.figure
            plt.imshow(img)
            plt.axis('off')
            if index2==0:
                plt.title(class_name)
    plt.show()

    ## show some images in a directory
def random_show_specified_cifar10(cifar10_path, classes=['car','cat','dog'],samples_per_class=3):
    # classes = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    num_classes = len(classes)   
    img_list = os.listdir(cifar10_path)

    for index1, class_name in enumerate(classes):
        img_index_name = [img for img in img_list if(int(img.split('_')[1].split('.')[0])==index1)]
        # print img_index_name
        img_choice = random.sample(img_index_name,samples_per_class)
        # print img_choice
        for index2,img_name in enumerate(img_choice):
            # print index2, img_name
            img = plt.imread(cifar10_path+img_name)
            plt_index = index2*num_classes+index1+1
            plt.subplot(samples_per_class,num_classes,plt_index)
            # plt.figure
            plt.imshow(img)
            plt.axis('off')
            # if index2==0:
            #     plt.title(class_name)
    plt.show()