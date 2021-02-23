import numpy as np

def calculate(list_of_9_number):
    """This function uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and
    elements in a 3 x 3 matrix. 
    Input: a list containing 9 digits. 
    Output: a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the 
    flattened matrix in the following format:
    {
    'mean': [axis1, axis2, flattened],
    'variance': [axis1, axis2, flattened],
    'standard deviation': [axis1, axis2, flattened],
    'max': [axis1, axis2, flattened],
    'min': [axis1, axis2, flattened],
    'sum': [axis1, axis2, flattened]
    }
    """
    
    if type(list_of_9_number) == list and len(list_of_9_number) == 9:
        x = np.array(list_of_9_number).reshape((3, 3))
        calculations = {
            'mean': [list(np.mean(x, axis=0)), list(np.mean(x, axis=1)), np.mean(x.flatten())],
            'variance': [list(np.var(x, axis=0)), list(np.var(x, axis=1)), np.var(x.flatten())],
            'standard deviation': [list(np.std(x, axis=0)), list(np.std(x, axis=1)), np.std(x.flatten())],
            'max': [list(np.max(x, axis=0)), list(np.max(x, axis=1)), np.max(x.flatten())],
            'min': [list(np.min(x, axis=0)), list(np.min(x, axis=1)), np.min(x.flatten())],
            'sum': [list(np.sum(x, axis=0)), list(np.sum(x, axis=1)), np.sum(x.flatten())]
            }
        return calculations
    else:
        raise ValueError("List must contain nine numbers.")