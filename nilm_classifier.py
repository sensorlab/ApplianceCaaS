from flask import *
import json
import requests
import numpy as np
import scipy.stats
import pickle

app = Flask(__name__)
clf=pickle.load(open("nilm_classifier.pkl", "rb"))


@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json
    raw_data = json.loads(json_)

    def n_turns(array_input):
        count=0
        sign0=np.sign(array_input[1]-array_input[0])
        for i in range(len(array_input)-1):
          tmpsign=np.sign(array_input[i+1]-array_input[i])
          if tmpsign != sign0:
            count+=1
            sign0=tmpsign
        return count

    def abs_derivative(array_input):
        sum=0
        for i in range(len(array_input)-1):
          sum+=np.abs(array_input[i+1]-array_input[i])
        return sum


    data_avg=[np.mean(i) for i in raw_data]
    data_skew=[scipy.stats.skew(i) for i in raw_data]
    data_kurt=[scipy.stats.kurtosis(i) for i in raw_data]
    data_std=[np.std(i) for i in raw_data]
    data_min=[min(i) for i in raw_data]
    data_max=[max(i) for i in raw_data]
    data_p2p=[max(i)-min(i) for i in raw_data]
    data_var=[np.var(i) for i in raw_data]
    data_nturns=[n_turns(i) for i in raw_data]
    data_d_abs=[abs_derivative(i) for i in raw_data]

    X=np.vstack([data_avg, data_skew, data_kurt, data_p2p, data_var, data_nturns, data_d_abs, data_std])
    X=np.transpose(X)

    y=clf.predict(X)
    
    
    return json.dumps(np.ndarray.tolist(y))


if __name__ == '__main__':
     app.run(port=2524, debug=True, host="0.0.0.0")