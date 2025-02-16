#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

top10 = []
i = 0
while i < 10:
    top10.append((items[i][0], items[i][1]))
    i += 1
#print(top10)
asc_top10 = sorted(top10, key=lambda x: x[1])
#print("printing ascending order...\n", asc_top10)
xkeys = [x[0] for x in asc_top10]
yvals = [x[1] for x in asc_top10]
#print("printing x keys:", xkeys)
#print("printing y vals:", yvals)

plt.bar(xkeys, yvals)
plt.savefig("plot1-test.png")
