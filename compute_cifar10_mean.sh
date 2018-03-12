#!/usr/bin/env sh
# This script compute the mean file of cifar10 training data in lmdb format.
set -e
CAFFEROOT=/home/meringue/Softwares/caffe-master
CIFAR10ROOT=/home/meringue/DataBase/cifar-10-batches-py
LMDBNAME=train_train_with_crat6_lmdb
DBTYPE=lmdb

echo "Computing image mean..."

$CAFFEROOT/build/tools/compute_image_mean -backend=$DBTYPE \
  $CIFAR10ROOT/$LMDBNAME $CIFAR10ROOT/$LMDBNAME/mean.binaryproto

echo "Done."
