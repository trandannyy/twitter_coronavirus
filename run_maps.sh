#!/bin/sh

path="/data/Twitter dataset/geoTwitter20-"

for file in "$path"*.zip; do
    ./src/map.py --input_path="$file" &
done
