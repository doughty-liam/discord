from FClayer import FClayer
import numpy as np  
from network import fcnetwork

num_inputs = 12
num_hidden_neurons = 8
num_outputs = 6
num_layers = 4
input_vals = [15, 1, 4, 3, 3, 12, 20, 7, 8, 4, 5, 6]


testNetwork = fcnetwork(num_inputs, num_hidden_neurons, num_outputs, num_layers)


testNetwork.run(input_vals)

print(testNetwork.output)