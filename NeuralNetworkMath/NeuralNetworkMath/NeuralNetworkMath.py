import numpy as np
import random 
import math

class NeuralNetwork:
    

    def __init__ (self, nInputNodes, nHiddenNodes, nHiddenLayers, nOutputNodes, arrInputs):
        self.rnd = random.Random(0)
        self.nIn = nInputNodes # 3  
        self.nOut = nOutputNodes # 2
        self.nHidden = nHiddenNodes # 4 * 1
        self.hiddenLayers = nHiddenLayers # 1

        # input nodes
        self.inArray = np.zeros(shape=[self.nIn], dtype=np.float32) # 1 X 3
        self.inWeights = np.zeros(shape=[self.nIn, self.nHidden],  dtype=np.float32) # 5 X 4
        
        # create the array for the output nodes
        self.outArray = np.zeros(shape=[self.nOut], dtype=np.float32) # 1 X 2
        self.outBiases =  np.zeros(shape=[self.nOut], dtype=np.float32) # create a biase for each output node

        self.hiddenNodes = np.zeros(shape=[self.nHidden, self.hiddenLayers], dtype=np.float32) # 5 X 5                        
        self.hiddenWeights = np.zeros(shape=[self.nHidden, self.nHidden, self.hiddenLayers -1],  dtype=np.float32) # 5 X 4
        self.hBiases = np.zeros(shape=[self.nHidden, self.hiddenLayers], dtype=np.float32)

        self.inputNodes = arrInputs
        
        self.InitializeWeights()
        
        print("Input Nodes")
        print(self.inputNodes)

        print("Input Weights")
        print(self.inWeights)

        print("hidden Baises")
        print(self.hBiases)
      
        print("Done")


    
    def calculateActivationNodes():
        for i in range(len(self.hiddenNodes)):
            if (i == 0):
                layer1Nodes = self.hiddenNodes[:i]
                weights = (self.hiddenWeights[:i])[0:] 

           

    def InitializeWeights(self):
        lo = -0.01; hi = 0.01
        for idx in range (len(self.inWeights)):
            self.inWeights[idx] = (hi - lo) * self.rnd.random() + lo

        for idxRow in range (self.hBiases.shape[0]):
            for idxCol in range (self.hBiases.shape[1]):
                self.hBiases[idxRow][idxCol] = (hi - lo) * self.rnd.random() + lo

        for idxRow in range (self.hiddenWeights.shape[0]):
            for idxCol in range (self.hBiases.shape[1]):
                self.hBiases[idxRow][idxCol] = (hi - lo) * self.rnd.random() + lo

       
        