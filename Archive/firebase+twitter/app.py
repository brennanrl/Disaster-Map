import time
from flask import Flask, request, jsonify
import pickle
import numpy as np
import re
from nltk.tokenize import word_tokenize

# Communication to TensorFlow server via gRPC
from grpc.beta import implementations
import tensorflow as tf

# TensorFlow serving stuff to send messages
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2
from tensorflow.contrib.util import make_tensor_proto

app = Flask(__name__)

crash_vocab = ['Crash', 'Earthquake', 'Explosion', 'Fire', 'Floods', 'Terrorism', 'Typhoon', 'None']

vector_channel = implementations.insecure_channel('35.184.14.40', 80)
disaster_channel = implementations.insecure_channel('0.0.0.0', 8500)

vector_stub = prediction_service_pb2.beta_create_PredictionService_stub(vector_channel)
disaster_stub = prediction_service_pb2.beta_create_PredictionService_stub(disaster_channel)

def sendVectorRequest(sents):
    req = predict_pb2.PredictRequest()
    req.model_spec.name = 'serving_saved_model'
    req.model_spec.signature_name = 'serving_default'
    req.inputs['text'].CopyFrom(make_tensor_proto(sents, shape=[len(sents)], dtype=tf.string))
    result = vector_stub.Predict(req, 60.0)

    predictions = np.reshape(result.outputs['embedding'].float_val, [len(sents), 512])
    return predictions

def sendDisasterRequest(vectors):
    req = predict_pb2.PredictRequest()
    req.model_spec.name = 'serving_saved_model'
    req.model_spec.signature_name = 'serving_default'
    req.inputs['vector'].CopyFrom(make_tensor_proto(vectors, shape=[len(vectors), 512], dtype=tf.float32))
    result = disaster_stub.Predict(req, 60.0)

    predictions = np.reshape(result.outputs['disaster'].float_val, [len(vectors), -1])
    return predictions

@app.route('/ping')
def ping():
        try:
            sendDisasterRequest(sendVectorRequest("This is a disaster tweet. #MaKaBhosda"))
        except:
            return "model not working", 500
        return "pong"

@app.route('/calculate', methods=['POST'])
def api():
    content = request.get_json()
    sents = content["texts"]
    start = time.time()
    vectors = sendVectorRequest(sents)
    outputs = sendDisasterRequest(vectors)
    preds = np.argmax(outputs, axis=-1)
    
    end = time.time()
    time_diff = end - start
    # print("time_taken:",time_diff)
    # TODO: Log time taken and errors to elastic
    return jsonify({"disasters": [crash_vocab[x] if outputs[i, x] >= 0.9 else 'None' for i, x in enumerate(preds)]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=443)