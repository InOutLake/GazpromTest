import numpy as np

def find_median(data):
    if not data.any():
        return None
    data.sort()
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    
def medians(data):
    medians = {}
    for key in data[0].keys():
        medians.setdefault(key, find_median(np.array([d[key] for d in data])))
    return medians

def summs(data: list):
    return {key: sum(d[key] for d in data) for key in data[0].keys()}

def min_values(data: list):
    return {key: min(d[key] for d in data) for key in data[0].keys()}

def max_values(data: list):
    return {key: max(d[key] for d in data) for key in data[0].keys()}

def counts(data: list):
    return len(data)
