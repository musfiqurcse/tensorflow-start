import tensorflow as tf
hello =tf.constant('Hellow, TensorFlow!')
sess=tf.Session()
print(sess.run(hello))