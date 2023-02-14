from FClayer import FClayer
import base_layer
import numpy as np
from ast import Not


class fcnetwork(FClayer):
    
    def __init__(self, num_inputs, num_neurons, num_outputs, num_layers):
        
        self.num_layers = num_layers
        self.num_inputs = num_inputs
        self.num_neurons = num_neurons
        self.num_outputs = num_outputs
        self.layers = [FClayer(num_inputs, num_neurons)] # creating first hidden layer
        
        for i in range(num_layers - 1): # Creating num_layers hidden layers
            self.layers.append(FClayer(num_neurons, num_neurons))
        
        self.layers.append(FClayer(num_neurons, num_outputs)) #creating output layer

    def run(self, inputs):

        self.feed = self.layers[0].forward_prop(inputs)
        
        for i in range(1, self.num_layers-1):
            self.feed = self.layers[i].forward_prop(self.feed)

        self.output = self.layers[self.num_layers].forward_prop(self.feed)
        