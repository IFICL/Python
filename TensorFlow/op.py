#!/usr/bin/python2.7
#Filename:op.py

import tensorflow as tf
# create an op to get a 2x1 matrix
matrix1 = tf.constant([[3., 3.]])

# create a another op and get a new 2x1 matrix
matrix2 = tf.constant([[2.],[2.]])

# create a new matrix product: matmul op , set 'matrix1' and 'matrix2' as input.
# return 'product' represents the outcome.
product = tf.matmul(matrix1, matrix2)

# start the pic.
sess = tf.Session()


result = sess.run(product)
print result

sess.close()