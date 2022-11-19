# Analysis of Popular Japanese Anime Genres in Python

This project is a two-part analysis of popular Japanese anime genres in Python. 

In the first part of this study, exploratory data analysis was performed on a CSV file from Kaggle containing over 12,000 anime series. Subsequently, a graphical 
analysis of the rating distribution, type distribution, as well as genre distribution was conducted using several relevant libraries and functions. From an inspection 
of the dataset, the most commonly-produced genres of anime by the industry can be shown. 

In the second part, web scraping was conducted to extract sentiment data from selected subreddit threads discussing recommended anime titles. Data visualisation was 
then executed to identify the most positively-viewed genres of anime by a sample of the Reddit community. 

## Part 1: Exploratory Data Analysis of Anime Dataset from Kaggle

### Data Source
Anime Recommendations Database, Kaggle (https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database), Retrieved on 22 July 2019

### KDE Plot of Anime Ratings

<img width="436" alt="image" src="https://user-images.githubusercontent.com/93922854/202857807-89d742f2-4d0c-4373-a7d1-77ab7406696c.png">

### Type Distribution of Anime

<img width="442" alt="image" src="https://user-images.githubusercontent.com/93922854/202857864-c864f9c4-a23f-4363-937e-9d37f1fa08ff.png">

### Genre Distribution of Anime 

<img width="508" alt="image" src="https://user-images.githubusercontent.com/93922854/202857876-09fbb2e3-e8de-45a4-8702-db22b8af1879.png">



## Part 2: Web Scraping of Selected Subreddit Threads

### Data Source
Thread 1: https://old.reddit.com/r/anime/comments/5ag0kb/recommendation_tuesdays_week_of_november_01_2016/

Thread 2: https://old.reddit.com/r/anime/comments/3pa2it/lets_list_anime_that_affected_your_emotions/

Thread 3: https://old.reddit.com/r/anime/comments/947lub/good_anime_recommendations/'

### Web Scraping Results for Most Common Anime Titles

<img width="670" alt="image" src="https://user-images.githubusercontent.com/93922854/202857945-120483fa-85cc-4d8c-8074-46c64f02270b.png">

### Web Scraping Results for Most Common Anime Genres

<img width="564" alt="image" src="https://user-images.githubusercontent.com/93922854/202857993-6bd5cf9b-b90d-4348-9e35-9ef240ecfc1e.png">


## Key Insights

Top 5 Anime Genres (from `anime.csv`): Comedy, Action, Adventure, Fantasy, Sci-fi

Top 3 Types of Anime (from `anime.csv`): TV, OVA, Movie

Top 5 Anime Genres (Reddit sentiments): Drama, Comedy, Shounen, School, Supernatural



## References
1. Category_Visualization, Kaggle (https://www.kaggle.com/xthunder94/category-visualization)
2. Anime, Kaggle (https://www.kaggle.com/igoratsberger/anime)
3. WHAT IS ANIME?, BellaOnline (http://www.bellaonline.com/articles/art4260.asp)
4. Framing Attention in Japanese and American Comics: Cross-Cultural Differences in Attentional
Structure, NCBI (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3449338/)
