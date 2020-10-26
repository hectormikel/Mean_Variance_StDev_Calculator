# Mean-Variance-Standard Deviation Calculator
import numpy as np

def calculate(list):
    try:
        methods = {'mean': 'np.mean', 'variance': 'np.var', 'standard deviation': 'np.std', 'max': 'np.max',
                   'min': 'np.min', 'sum': 'np.sum'}
        x = np.array(list).reshape((3, 3))

        calculations = dict()
        for key, value in methods.items():
            calculations[key] = [eval(value + '(x, axis = 0)').tolist(), eval(value + '(x, axis = 1)').tolist(),
                                 eval(value + '(x)')]

        return calculations

    # raise exception
    except:
        raise ValueError("List must contain nine numbers.")