import tensorflow as tf
hello =tf.constant('Hellow, TensorFlow!')
a =tf.constant([2,3,4,5,6])
b =tf.constant([3,4,5,6,7])
c= tf.add(a,b)

sess=tf.Session()
with tf.Session() as session:
    result =session.run(c)
    print(result)
# print(sess.run(hello))