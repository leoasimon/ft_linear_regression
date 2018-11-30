#! /usr/bin/env python3

import matplotlib.pyplot as plt

def estimate(x, t0, t1):
	return t0 + x * t1

def linear_res(x, y, t0, t1):
    min_km = min(x)
    max_km = max(x)
    fig, ax = plt.subplots()
    ax.set_xlabel("Km")
    ax.set_ylabel("Price")
    ax.scatter(x, y)
    ax.plot([min_km, max_km], [estimate(min_km, t0, t1), estimate(max_km, t0, t1)])
    plt.show()

def plot_costs(costs):
    x = range(len(costs))
    fig, ax = plt.subplots()
    ax.set_xlabel("Iterations")
    ax.set_ylabel("Costs")
    ax.plot(x, costs)
    plt.show()

