# Coronavirus Twitter Analysis

**Project Overview:**

This project utilizes geotagged twitter data provided by Professor Mike Izbicki.
The goal of this project was to use large scale data processing and analyzing techniques to get information from tweets regarding coronavirus in 2020.

**About the Data:**

Approximately 500 million tweets are sent everyday.
Of those tweets, about 2% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
In total, there are about 1.1 billion tweets in this dataset.

**Data Processing Algorithm:**

In this project, I analyzed this data using the MapReduce algorithm. The data was already partitioned, so I created the mapper, reducer, and visualizer.

*Mapper*

This file is located in `/src/map.py`.
I modified this code so that it could also keep track of the country in which the tweet came from. So, this mapper takes each zip file and counts the number of tweets for each hashtag, in groups of the origin language and country separately.

*Reducer*

This file is located in `/src/reduce.py`.
This code takes each output from the mapper and then combines the values from each hashtag into one total value. Since each file from the mapper corresponds to the day, the reducer combines all of the data into the tweet data for one whole year.

*Visualizer*

This file is located in `/src/visualize.py`.
This code uses matplotlib to plot bar graphs of the json formatted data. This was completed by creating separate lists for the x and y axes and then plotting them together.

Below are some bar plots I created using these functions:

1. Number of times "#coronavirus" was used by country in 2020
<img src=plot-coronavirus-reduced.country.png width=100% />

2. Number of times "#coronavirus" was used by language in 2020
<img src=plot-coronavirus-reduced.lang.png width=100% />

3. Number of times "#코로나바이러스" was used by country in 2020
<img src=plot-코로나바이러스-reduced.country.png width=100% />

4. Number of times "#코로나바이러스" was used by language in 2020
<img src=plot-코로나바이러스-reduced.lang.png width=100% />

Overall, we see that #coronavirus was mostly frequently used in tweets that came from the United States and were in English. On the other hand, the #코로나바이러스 was mostly used in Korea from tweets that were in Korean as expected.

**Alternate-Reduce:**

I also created another way to reduce and visualize the data. In this new visualizer, it creates a line graph of user chosen hashtags.
To do this, I had to scan each file and extract the frequency of each hashtag and stored them separately within a dictionary where each key was the hashtag and each value was a list of lists which corresponded to the days.

Below is the line plot I created using this alternate reduce and visualizer:

1. Number of tweets by day with a hashtag in 2020
<img src=alt-reduce-plot-example.png width=100% />

Here, we see that #coronavirus and #corona peaked in usage around day 70 (around mid March), which makes sense because that is when the pandemic happened.

On the other hand, we see #doctor and #virus are low in frequency compared to the other two. However, #virus also has a spike around the same time as #coronavirus and #corona.

Overall, this project taught me how to work with large scale datasets, multilingual text, and use the MapReduce divide-and-conquer paradigm to create parallel code.
