from base_layer import Layer
from base_layer import sigmoid
import numpy as np  

class FClayer(Layer):

    # Initializing layer with num inputs and num outputs
    def __init__(self, input_size, output_size): 
        
        self.weights = np.random.rand(input_size, output_size) - 0.5
        self.bias = np.random.rand(1, output_size) - 0.5

    #inheriting from base_layer and actually defining the forward propogation of layer inputs.
    def forward_prop(self, input):
        
        self.input = input
        self.output = np.add(np.matmul(input, self.weights), self.bias)
        
        for i in range(len(self.output)):
            self.output[i] = sigmoid(self.output[i])

        return self.output