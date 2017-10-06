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
        self.inBiases = np.zeros(shape=[self.nHidden], dtype=np.float32)

        # create the array for the output nodes
        self.outArray = np.zeros(shape=[self.nOut], dtype=np.float32) # 1 X 2
        self.outBiases =  np.zeros(shape=[self.nOut], dtype=np.float32) # create a biase for each output node

        self.activationArray = np.zeros(shape=[self.nHidden, self.hiddenLayers], dtype=np.float32) # 5 X 5                        
        self.hiddenWeights = np.zeros(shape=[self.nHidden, self.nHidden, self.hiddenLayers],  dtype=np.float32) # 5 X 4
        
        self.InputArray = arrInputs
        
        self.initializeNodes()
        self.InitializeWeights()
        print(self.activationArray)
        print(self.hiddenWeights)
      
        print("Done")


    
    def calculateActivationNodes():
        for i in range(len(self.activationArray)):
            if (i == 0):
                layer1Nodes = self.hiddenNodesArray[:i]
                weights = (self.hiddenWeights[:i])[0:] 

    def initializeNodes(self):
        #set all the biases to 1.0
        for i in range(len(self.activationArray)):
            self.activationArray[0][i] = 1.0

        # now lets add all the input values form the array to the input layer of the matirx [layer 0]
        for j in range(len(self.InputArray)):
            self.activationArray[j+1][0] = self.InputArray[j]

       

    def InitializeWeights(self):
        # set the weights for the first row to 1 since these are the biases.
        for i in range(len(self.hiddenWeights)-1):
            self.hiddenWeights[0][i] = 1.0

        lo = -0.01; hi = 0.01
        for idxRow in range(1, self.hiddenWeights.shape[0]):
            for idxCol in range(self.hiddenWeights.shape[1]):
                self.hiddenWeights[idxRow][idxCol] = (hi - lo) * self.rnd.random() + lo

                if (idxRow == (self.hiddenWeights.shape[0] -1) and len(self.InputArray) < self.nHidden):
                    self.hiddenWeights[idxRow][idxCol] = 0.0
        
