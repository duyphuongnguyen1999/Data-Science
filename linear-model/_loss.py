def MeanSquaredError(y_true, y_pred):
    assert len(y_true) == len(y_pred), "y_true and y_pred have different lenght"

    m = shape(y_true)[0]

    mean_squared_error = 1 / 2 * m * (y_true - y_pred) ** 2

    return mean_squared_error
