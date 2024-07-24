import numpy as np

def getMax(array:np.ndarray):
    y = np.max(array.mean(axis=2), axis=0)
    x = range(array.shape[1])

    return x, y