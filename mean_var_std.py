import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    array = np.array(list).reshape(3, 3)
    
    mean = [array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), array.mean()]
    variance = [array.var(axis=0).tolist(), array.var(axis=1).tolist(), array.var()]
    std = [array.std(axis=0).tolist(), array.std(axis=1).tolist(), array.std()]
    amax = [array.max(axis=0).tolist(), array.max(axis=1).tolist(), array.max()]
    amin = [array.min(axis=0).tolist(), array.min(axis=1).tolist(), array.min()]
    asum = [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), array.sum()]
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std,
        'max': amax,
        'min': amin,
        'sum': asum
    }


    return calculations