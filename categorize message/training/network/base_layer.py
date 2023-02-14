from ast import Not
import numpy as np

def sigmoid(x):
    y = (1/(1+np.exp(-x)))
    return y

class Layer:

    def __init__(self):
        self.input = None
        self.output = None
    
    def forward_prop(self, input):
        raise NotImplementedError

    def backward_prop(self, output_error, learning_rate):
        raise NotImplementedError