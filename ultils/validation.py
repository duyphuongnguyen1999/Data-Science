def check_consistent_length(*array):
    """Check that all arrays have consistent first dimensions.

    Checks whether all objects in arrays have the same shape or length.

    Parameters
    ----------
    *arrays : list or tuple of input objects.
        Objects that will be checked for consistent length.

    Examples
    --------
    >>> from ..utils.validation import check_consistent_length
    >>> a = [1, 2, 3]
    >>> b = [2, 3, 4]
    >>> check_consistent_length(a, b)
    """
