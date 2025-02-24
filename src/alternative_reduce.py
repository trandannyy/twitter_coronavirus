#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_hashtags', nargs='+',required=True)
parser.add_argument('--input_paths',nargs='+',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt
import numpy as np

# create dictionary where keys are hashtags
yvals = {}
for hashtag in args.input_hashtags:
    yvals[hashtag] = []

    # get frequency (value) for each file within each hashtag
    for file in args.input_paths:
        with open(file) as f:
            tmp = json.load(f)
            # add all amounts for total hashtag frequency
            if tmp.get(hashtag):
                yvals[hashtag].append(sum(tmp.get(hashtag).values()))
            else:
                yvals[hashtag].append(0)
    # plot
    plt.plot(np.arange(366), yvals[hashtag], label=hashtag)
plt.legend()
plt.ylabel("Number of Tweets")
plt.xlabel("Day of Year")
#print(yvals)
plt.savefig(f"alt-reduce-plot-example.png")
