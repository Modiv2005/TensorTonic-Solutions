import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value of a discrete random variable.
    """
    x = np.asarray(x, dtype=float)
    p = np.asarray(p, dtype=float)

    return float(np.dot(x, p))