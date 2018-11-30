#! /usr/bin/env python3

import numpy as np
import argparse
from plot import linear_res, plot_costs

def estimate(x, t0, t1):
	return t0 + x * t1

def standardize(x):
	return (x - np.mean(x)) / np.std(x)

def destandardize(sx, x):
	return sx * np.std(x) + np.mean(x)

def cost(h, y):
	m = len(y)
	return sum([e**2 for e in (h - y)]) * (1 / (2 * m))

def train(x, y, args):
	t0 = 0
	t1 = 0
	learning_rate = args.learning_rate
	costs = []
	for i in range(args.iterations):
		h = estimate(x, t0, t1)
		costs.append(cost(h, y))
		tmp0 = learning_rate * np.mean(h - y)
		tmp1 = learning_rate * np.mean((h - y) * x)
		t0 -= tmp0
		t1 -= tmp1
	if args.debug:
		plot_costs(costs)
	return (t0, t1)

def parse():
	parser = argparse.ArgumentParser()

	parser.add_argument("name", nargs="?", help="Name of the file to open")
	parser.add_argument("-d", "--debug", action="store_true", help="Debug tag to try different learning rate")
	parser.add_argument("-lr", "--learning_rate", type=float, default=1, help="choose a learning rate")
	parser.add_argument("-i", "--iterations", type=int, default=200, help="choose a number of iterations")
	parser.add_argument("-v", "--view",  action="store_true", help="Plot the result")

	return parser.parse_args()

def unscale_thetas(estimations, x):
	t1 = (estimations[0] - estimations[1]) / (x[0] - x[1])
	t0 = estimations[0] - (t1 * x[0])
	return (t0, t1)

def save_thetas(t0, t1):
	np.savetxt("thetas.csv", np.array([t0, t1]), delimiter=',')

def main():
	args = parse()
	data = np.loadtxt("data.csv", dtype = np.longdouble, delimiter = ',', skiprows = 1)
	x = (data[:, 0])
	y = (data[:, 1])
	nx = standardize(x)
	ny = standardize(y)
	t0, t1 = train(nx, ny, args)
	estimations = destandardize(estimate(nx, t0, t1), y)
	t0, t1 = unscale_thetas(estimations, x)
	save_thetas(t0, t1)
	if args.view:
		linear_res(x, y, t0, t1)

if __name__ == "__main__":
	main()