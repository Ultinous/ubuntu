#!/usr/bin/env python
'''
Caffe Python Module Testsuite for Debian Package
Copyright (C) 2016 Zhou Mo

Reference:
http://nbviewer.jupyter.org/github/BVLC/caffe/blob/master/examples/01-learning-lenet.ipynb
http://nbviewer.jupyter.org/github/BVLC/caffe/blob/master/examples/net_surgery.ipynb
'''

import numpy
import caffe

def test_lenet_benchmark():
  # load lenet deploy network
  model_definition = "examples/mnist/lenet.prototxt"
  caffe.set_mode_cpu()
  model = caffe.Net(model_definition, caffe.TEST)
  # populate random data and copy it to network
  batch = numpy.random.randn(64, 1, 28, 28)
  model.blobs['data'].reshape(64, 1, 28, 28)
  model.blobs['data'].data[...] = batch
  # randomly fill parameter into network
  model.params['conv1'][0].data.shape # access test, this should be (20, 1, 5, 5)
  model.params['conv1'][0].flat = numpy.random.randn(20, 1, 5, 5).flat
  model.params['conv1'][1].flat = numpy.random.randn(20,).flat
  model.params['conv2'][0].flat = numpy.random.randn(50, 20, 5, 5).flat
  model.params['conv2'][1].flat = numpy.random.randn(50,).flat
  model.params['ip1'][0].flat = numpy.random.randn(500, 800).flat
  model.params['ip1'][1].flat = numpy.random.randn(500,).flat
  model.params['ip2'][0].flat = numpy.random.randn(10, 500).flat
  model.params['ip2'][1].flat = numpy.random.randn(10,).flat
  # forward this network, here we don't care neither the network parameters nor the result.
  output = model.forward()
  output_prob = output['prob'][0] # prob vector for the first image in batch
  prediction = output_prob.argmax()
  print ('This mindless benchmark ends up with an arbitary output {}'.format(prediction))

def main():
  test_lenet_benchmark()

if __name__ == "__main__":
  main()
