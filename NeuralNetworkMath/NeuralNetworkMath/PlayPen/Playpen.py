import numpy as np
from NeuralNetworkMath import NeuralNetwork

if __name__ == '__main__':
    inputs = [1.0, 2.0, 3.0]
    nn = NeuralNetwork(3, 4, 4, 2, inputs)

    
    x = np.array([[1,2,3], [4,5,6]])
    print(x)
    print(x.shape)
    print(x.ndim)
    print(x[:, 2])
    print(x[::-1]) # get the array reverse order (last row first) 

    a = np.array([
                   [0, 1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10, 11],
                   [12, 13, 14, 15, 16, 17],
                   [18, 19, 20, 21, 22, 23],
                   [24, 25, 26, 27, 28, 29],
                   [30, 31, 32, 33, 34, 35]
                 ])
    print("\n")
    print(a[:, 3])
    print("\n")
    print(a[0:2, 4:]) #from: row 0 to row 2 & from: col 4 to col end
    print("\n")
    print(a[2::2, ::2]) #from: row 2 to: row end, give me every 2nd number & from: col start to: col end, give me every 2nd number
    
    print(a.flags)

    d = np.zeros(shape=(10,10), dtype=np.float32)
    print(d)


    ###### Vectorized Operations  ######

    # + one to each element in the array
    d = d + 1
    print("\n")
    print(d)

    # * 2 to each element in the array
    v = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    d = v * d
    print(d)

    ###### Vector Math ######
    #numpy.dot()

    x = np.array([
                    [1, 2],
                    [3, 4]
            ])
    y = np.array([
                    [10, 20], 
                    [30, 40]
                ])

    print(np.dot(x, y))
    print(np.vdot(x, y)) # 1 * 10 + 2 * 20 + 3 * 30 + 4 * 40 = 300 



