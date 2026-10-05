import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    sv = float(np.var(x, ddof=1))
    sd = float(np.std(x, ddof=1))
    return {
        "variance": sv,
        "standard_deviation": sd
    }
    pass