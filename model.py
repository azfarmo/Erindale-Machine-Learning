import pickle
import sys
import numpy as np
noise_level = float(open('noise.txt','r').read())
model = pickle.load(open('finalized_model.sav', 'rb'))
def predict(temp,humidity,lat,lng):
    nh = [temp,humidity,noise_level,lat,lng]
    return model.predict(np.array(nh).reshape(-1, 5))[0]