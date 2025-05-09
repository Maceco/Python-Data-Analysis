import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(list)
    resArr = arr.reshape(3,3)
    meanAxis1 = np.ndarray.tolist(np.mean(resArr, axis=0))
    meanAxis2 = np.ndarray.tolist(np.mean(resArr, axis=1))
    meanFlat = np.mean(resArr)
    varAxis1 = np.ndarray.tolist(np.var(resArr, axis=0))
    varAxis2 = np.ndarray.tolist(np.var(resArr, axis=1))
    varFlat = np.var(resArr)
    stddevAxis1 = np.ndarray.tolist(np.std(resArr, axis=0))
    stddevAxis2 = np.ndarray.tolist(np.std(resArr, axis=1))
    stddevFlat = np.std(resArr)
    maxAxis1 = np.ndarray.tolist(np.max(resArr, axis=0))
    maxAxis2 = np.ndarray.tolist(np.max(resArr, axis=1))
    maxFlat = np.max(resArr)
    minAxis1 = np.ndarray.tolist(np.min(resArr, axis=0))
    minAxis2 = np.ndarray.tolist(np.min(resArr, axis=1))
    minFlat = np.min(resArr)
    sumAxis1 = np.ndarray.tolist(np.sum(resArr, axis=0))
    sumAxis2 = np.ndarray.tolist(np.sum(resArr, axis=1))
    sumFlat = np.sum(resArr)

    calculations = {'mean': [meanAxis1, meanAxis2, meanFlat],
        'variance': [varAxis1, varAxis2, varFlat],
        'standard deviation': [stddevAxis1, stddevAxis2, stddevFlat],
        'max': [maxAxis1, maxAxis2, maxFlat],
        'min': [minAxis1, minAxis2, minFlat],
        'sum': [sumAxis1, sumAxis2, sumFlat]
    }
    return calculations
