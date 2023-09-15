import numpy as np


def service_time():
    """
    the `service_time` method draws a random sample from a normal
    distribution with the mean of 10 and the std deviation of 2.
    """
    return np.random.normal(10, 2)


def customer_entry(size: int, arrival_rate=2):
    inter_arrivals = np.random.exponential(1 / arrival_rate, size)
    result = [round(inter_arrivals[0], 2)]
    for i in range(1, size):
        result.append(round(result[-1] + inter_arrivals[i], 2))
    return result
