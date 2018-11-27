#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from view import linear_res

def estimate(x, t0, t1):
	return t0 + x * t1

def normalize(x, x_min, x_max):
	return (x - x_min) / (x_max - x_min)

def standardize(x):
	return (x - np.mean(x)) / np.std(x)

def destandardize(x, x_ref):
	return x * np.std(x_ref) + np.mean(x_ref)

def get_normalized_datas(x, y):
	nx = normalize(x, min(x), max(x))
	ny = normalize(y, max(x), max(y))
	return (nx, ny)

def train(x, y):
	t0 = 0
	t1 = 0
	learning_rate = 0.3
	for i in range(100):
		h = estimate(x, t0, t1)
		tmp0 = learning_rate * np.mean(h - y)
		tmp1 = learning_rate * np.mean((h - y) * x)
		t0 -= tmp0
		t1 -= tmp1
	return (t0, t1)


def main():
	data = np.loadtxt("data.csv", dtype = np.longdouble, delimiter = ',', skiprows = 1)
	x = (data[:, 0])
	y = (data[:, 1])
	# nx, ny = get_normalized_datas(x, y)
	nx = standardize(x)
	ny = standardize(y)
	t0, t1 = train(nx, ny)
	linear_res(nx, ny, t0, t1)
	# linear_res(x, y, t0 * max(y), t1 * max(y))

if __name__ == "__main__":
	main()