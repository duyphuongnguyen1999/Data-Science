import numbers
import numpy as np


class LinearRegression_:
    """
    Parameters:
    -----------
        optimizer (str):
            Specify optimization method for linear regression
                - 'gd': Gradient Descent (Default)
                - 'ols': Ordinary Least Square
                - 'sgd': Stochastics Gradient Descent
                - 'mgd': Mini-Batch Gradient Descent

        loss (str):
            Specify loss function for optimization
                - 'mse': Mean Squared Error (Default)
                - 'mae': Mean Absolute Error
                - 'huber': Huber Loss
                - 'l1': Lasso Loss (L1 Regularization)
                - 'l2': Ridge Loss (L2 Regularization)

        fit_intercept (bool), default True
            Whether to calculate the intercept for this model.
            If set to False, no intercept will be used in calculations
            (i.e. data is expected to be centered).

    Attributes:
    -----------
        coef_ (array of shape (n_features, ) or (n_targets, n_features)):
            Estimated coefficients for the linear regression problem.
            If multiple targets are passed during the fit (y 2D), this is a 2D
            array of shape (n_targets, n_features) while if only one target is
            passed, this is a 1D array of length n_features.

        intercept_ (float or array of shape (n_targets, )):
            Independent term in the linear model.
            Set to 0.0 if fit_intercept = False.

        n_features_in_ (int):
            Number of features seen during fit().

        feature_names_in_ (ndarray of shape (n_features_in_,)):
            Names of features seen during fit.
            Defined only when X has feature names that are all strings.

    Methods:
    --------
        fit(X, y, [sample_weight]):
            Fit linear model.

        predict(X):
            Predict using the linear model.

        score(X, y[, sample_weight]):
            Return the coefficient of determination of the prediction.

    """

    def __init___(self, optimizer="gd", loss="mse", fit_intercept=True):
        pass

    def num_samples(self, X):
        X = np.asarray(X)
        return X.shape[0]

    def _create_dataset(
        self, X, y, fit_intercept=True, sample_weight=None, random_state=None
    ):
        if isinstance(sample_weight, numbers.Number):
            sample_weight = np.ranom.normal()
        else:
            sample_weight = np.asarray(sample_weight)

        if fit_intercept:
            pass

        return X, y, sample_weight

    def fit(self, X, y, *sample_weight):
        pass
