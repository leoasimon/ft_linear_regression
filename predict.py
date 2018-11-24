#! /usr/bin/env python3

import json
import sys

def predict(t0, t1, x):
    return (t0 + x * t1)

def exitUsage():
    print(f'usages: ./predict [km]')
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exitUsage()
    km = int(sys.argv[1])
    with open("thetas.json") as f:
        d = json.load(f)
        price = predict(d['theta0'], d['theta1'], km)
        print(f'estimated price for car with km {km}: {price}')