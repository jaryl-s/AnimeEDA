# import the relevant packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections
import operator
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, words
import requests
import time
from bs4 import BeautifulSoup
import re
nltk.download("words")
english_words = words.words()

# read dataset from csv  file to a DataFrame
anime_df = pd.read_csv('anime.csv')
rating_df = pd.read_csv('rating.csv')
display(anime_df.head(10))
anime_df.describe()

# visualise distribution of rating scores from anime dataset using a KDE plot
rating_skewness = anime_df['rating'].skew()
print('The skewness of the "rating" column is: ' + str(rating_skewness))
# Define figure size
fig1 = plt.figure(figsize=(10, 6))
# Plot graph
ax1 = fig1.add_subplot(111)
sns.kdeplot(anime_df['rating'],
 kernel='gau', # Code for shape of kernel to fit with. Bivariate KDE can only use Gaussian kernel
 bw=0.4, # bw affects curve smoothness. Small bw is precise but potentially messy, large bw is smooth but vague
 shade=True)
# Define axis titles and title
ax1.set_xlabel("rating", fontsize = 15)
ax1.set_ylabel("density", fontsize = 15)
ax1.set_title("KDE plot of Anime Rating Data", fontsize = 18)
plt.show()

# analyse anime by type
# From anime_df, group the entries by 'type', and sort them in descending order of the count for each type
anime_types = anime_df.groupby('type').size().reset_index(name = 'count').sort_values('count', ascending = False)
# Create a new dataframe - Adding 'drop = True' within .reset_index() eliminates the 'index' column that is not needed here
anime_types_df = pd.DataFrame(data = anime_types.reset_index(drop = True))
# Note that the most numerous anime type will be in the first row, at index 0
display(anime_types_df)
total_count = anime_types_df['count'].sum() # This calculates the total number of anime series
highest_type_count = anime_types_df['count'][0] # This calculates the number of anime series of the most numerous type
highest_type_proportion = highest_type_count / total_count # This calculates the proportion of the most numerous type
print('The proportion of ' + str(anime_types_df['type'][0]) + '-type anime is: ' + str(highest_type_proportion))
# Plot data as a horizontal bar chart
plt.figure(figsize = (12,8))
plt.barh(anime_types['type'], # y-axis of the bar chart
 anime_types['count'], # x-axis of the bar chart
 align = 'center', # Center the bars on the y-coordinates
 color='forestgreen',
 edgecolor ='black')
plt.gca().invert_yaxis()
plt.title('Bar Chart of Anime by Type', fontsize =20)
plt.xlabel('Count', fontsize =15)
plt.xticks(np.arange(0, 4001, 500))
plt.ylabel('Type', fontsize =15)

# List all anime genres represented
# Initialise empty Python set
genres = set()
# Iterate through each entry, with focus on the genre column
for entry in anime_df['genre']:
 # Without the condition below, AttributeError will occur: 'float' object has no attribute 'split'
 # If the genre isn't a string, the continue' statement continues to the next iteration of the loop (skip)
 if type(entry) is not str:
 continue
 # The split() method splits a string into a list. Specify separator as comma.
 genres.update(entry.split(", "))
# Note that a set cannot have duplicate elements by definition. Thus there is no need to deliberately prevent double-adding
print(genres)
print("Total Genres: " + str(len(genres)))

# List genres by count
# defaultdict: modified dict that can count characters in strings, or elements in lists
# Pass int as the factory function (data type) to defaultdict
# When we type 'defaultdict(int)', the default value of each key in 'genres_count' is 0
genres_count = collections.defaultdict(int)
for entry in anime_df['genre']:
 # Same as above, only proceed with 'entry' if it is a string type
 if type(entry) is not str:
 continue
 # 'entry.split(", ")' can look something like this: ['Horror', 'Comedy', 'Action', 'Drama']
 for genre in entry.split(", "):
 genres_count[genre] += 1

genres_count = sorted(genres_count.items(), key=operator.itemgetter(1), reverse=True)
print(genres_count)
# Syntax: sorted(iterable, key, reverse)
# Iterable: Collection that needs to be sorted
# Key: Basis for comparison
# Reverse: Descending (True) or ascending (False)
# operator.itemgetter(1) constructs a callable that assumes an iterable object (e.g. list, tuple, set) as input,
# and fetches the 1st element out of it. In this case, the 1st element for each nested tuple is the count for the genre

# Initialise two empty lists to store each genre, as well as the count for each genre
genre_list = []
genre_count_list = []
# Recall that genres_count is a list of tuples, with each tuple containing the genre and its count: e.g. ('Comedy', 4645)
# Iterate through each nested tuple within the list, and append the genre and its count to the two lists
for each_tuple in genres_count:
 genre_list.append(each_tuple[0])
 genre_count_list.append(each_tuple[1])
# Plot bar chart using seaborn
fig2 = plt.figure(figsize = (18,10))
sns.barplot(x = genre_list,
 y = genre_count_list,
 color = 'steelblue')
plt.title('Bar Chart of Anime Genres', fontsize = 20)
# Rotate the genres on the x-axis to ensure that they do not overlap and become illegible
plt.xticks(rotation = 'vertical')
# Ensure that the divisions on the y-axis are appropriate
plt.yticks(np.arange(0, 5001, 500))
plt.xlabel('Genres', fontsize = 15)
plt.ylabel('Count', fontsize = 15)
# Calculate the proportion of the most common genre
# Note that the two lists are already sorted in descending order: Index 0 holds the most common genre/its count
most_common_genre_count = genre_count_list[0]
most_common_genre = genre_list[0]
# Recall that total_count was calculcated previously already
most_common_genre_proportion = most_common_genre_count / total_count
print('The most common genre is ' + str(most_common_genre) + ' with a proportion of: ' + str(most_common_genre_proportion))
