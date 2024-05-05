import numbers
import numpy as np
import pandas as pd


def get_shape(array):
    if isinstance(array, numbers.Number):
        return ()

    elif type(array) in [list, tuple]:
        shape = ()
        while not isinstance(array, numbers.Number):
            shape += (len(array),)
            array = array[0]
        return shape

    elif type(array) in [np.ndarray, pd.core.frame.DataFrame]:
        return array.shape


df = pd.DataFrame([[1, 2, 3], [1, 2, 3]])
np_arr = np.array([[1, 2, 3], [1, 2, 3]])
lst = [[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]]

print(get_shape(lst))
