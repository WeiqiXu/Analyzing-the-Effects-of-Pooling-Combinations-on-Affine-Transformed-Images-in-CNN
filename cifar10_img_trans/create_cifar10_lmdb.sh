#!/bin/bash
# convert images to lmdb

DATA=/home/meringue/DataBase/cifar-10-batches-py
IMGDIRNAME=train_train_with_rat6_limit
IMGLIST=img_name_list/train_train_with_rat6_limit.txt
LMDBNAME=train_train_with_rat6_limit_lmdb

rm -rf $DATA/$LMDBNAME
echo 'start converting train_valid_with_rat6_limit...'
/home/meringue/Softwares/caffe-master/build/tools/convert_imageset --shuffle=true \
$DATA/$IMGDIRNAME/ $DATA/$IMGLIST $DATA/$LMDBNAME

