#!/usr/bin/env sh
set -e
CAFFEROOT=/home/meringue/Softwares/caffe-master
CIFAR10PY=/home/meringue/Documents/CaffePy/cifar10py
TOOLS=$CAFFEROOT/build/tools
echo 'start training...'
# GLOG_logtostderr=0 GLOG_log_dir=$CIFAR10PY/cifar10_caffemodels/model_pooling_method/LOG/ \
$TOOLS/caffe train \
  --solver=$CIFAR10PY/cifar10_caffemodels/model_pooling_method/cifar10_quick_solver.prototxt $@

# reduce learning rate by factor of 10 after 8 epochs
# GLOG_logtostderr=0 GLOG_log_dir=$CIFAR10PY/cifar10_caffemodels/model_pooling_method/LOG/ \
$TOOLS/caffe train \
  --solver=$CIFAR10PY/cifar10_caffemodels/model_pooling_method/cifar10_quick_solver_lr1.prototxt \
  --snapshot=$CIFAR10PY/cifar10_caffemodels/model_pooling_method/cifar10_quick_iter_4000.solverstate.h5 $@
