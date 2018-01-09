import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# OS import is done to curb warning messages to appear
# TF environment variable TF_CPP_MIN_LOG_LEVEL.

# It defaults to 0, showing all logs
# To filter out INFO set to 1
# WARNINGS, additionally 2
# and to additionally filter out ERROR logs set to 3

constant_graph = tf.Graph()
variable_graph = tf.Graph()
placeholder_graph = tf.Graph()

# This will returned default unnamed graph object
print(tf.get_default_graph())

# <node_name>.graph can be used to identify node belongs to which graph

with constant_graph.as_default():
    a = tf.constant(2)
    b = tf.constant(3)

    d = tf.add(a,b)
    c = tf.multiply(a,b)

    f = tf.add(c,d)
    e = tf.subtract(c,d)

    g = tf.divide(e,f)

    with tf.Session() as sess:
        print("Output of constant block : ", sess.run(g))

    # This will return constant graph object
    print(tf.get_default_graph())

# When using variables, they need to be initialized before use
with variable_graph.as_default():
    a = tf.constant(5)
    b = tf.Variable(a*2)

    c = tf.add(a,b)

    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
        print("Output of variable block : ", sess.run(c))

    # This will return variable graph object
    print(tf.get_default_graph())


# When using placeholder, value is not known at the time of defining the node
# Value is passed on using "feed_dict" at the time of execution
# Note when there are node dependencies, if a placeholder exist in a graph
# value needs to be provided or else an exception with be raised
with placeholder_graph.as_default():
    a = tf.constant(7)
    b = tf.placeholder(dtype='int32')

    c = tf.add(a,b)

    with tf.Session() as sess:
        print("Output of placeholder block : ", sess.run(c,feed_dict={b:2}))

    # This will return placeholder graph object
    print(tf.get_default_graph())

