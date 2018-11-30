#! /usr/bin/env python3

import sys
import numpy as np
import argparse

def estimate(x, t0, t1):
    return (t0 + x * t1)

def exitUsage():
    print(f'usages: ./predict [km]')
    sys.exit(1)

def km_range(x):
    try:
        x = int(x)
        if x < 0:
            raise argparse.ArgumentTypeError("km must be a positive value")
    except ValueError:
        raise argparse.ArgumentTypeError("km must be a number")
    return x

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("km", type=km_range, help="km (must be > 0)")
    args = parser.parse_args()

    t0, t1 = np.loadtxt("thetas.csv", delimiter=',')
    e = estimate(args.km, float(t0), float(t1))
    print(f'Estimate price for a car with {args.km} km: {int(e)}$')