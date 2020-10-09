import tensorflow as tf
# import tensorflow_hub as hub
import numpy as np

def gelu_fast(_x):
    return 0.5 * _x * (1 + tf.tanh(tf.sqrt(2 / np.pi) * (_x + 0.044715 * tf.pow(_x, 3))))

with tf.Graph().as_default():
    vector_placeholder = tf.placeholder(tf.float32, shape=[None, 512])
    x = vector_placeholder
    x = tf.layers.dense(x, 256, activation=gelu_fast, trainable=True, name="l1",
      reuse=tf.AUTO_REUSE)
    x = tf.layers.dense(x, 64, activation=gelu_fast, trainable=True, name="l2",
      reuse=tf.AUTO_REUSE)
    logits = tf.layers.dense(x, 8, activation=None, trainable=True, name="fc",
      reuse=tf.AUTO_REUSE)
    probs = tf.nn.softmax(logits, axis=-1)
    saver = tf.train.Saver(max_to_keep=5)
    init_op = tf.group([tf.global_variables_initializer()])
    with tf.Session() as session:
      session.run(init_op)
      saver.restore(session, "DisasterNet-6")
      tf.saved_model.simple_save(
        session,
        "/models/serving_saved_model/1",
        inputs = {"vector": vector_placeholder},
        outputs = {"disaster": probs},
        legacy_init_op = tf.tables_initializer()
      )
