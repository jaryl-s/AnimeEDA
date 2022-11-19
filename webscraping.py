def urlToHTML(url):
 headers = {'User-Agent': 'Mozilla/5.0'}
 HTML = requests.get(url, headers=headers)
 time.sleep(2)
 return BeautifulSoup(HTML.text, 'html.parser')
def HTMLtopara(html):
 h_text = html.findAll('p')
 para=[]
 for p in h_text[28:]:
 if '\n'not in p.text:
 if '[–]' not in p.text:
 if len(p.text) >5:
 if '[+]' not in p.text:
 para.append(p.text)
return para

def stripText(text):
 text = re.sub("[.®'&$’\"\-()]", "", text)
 text = text.lower().strip()
 return text #stripText(HTMLtopara(urlToHTML(url)))

def crunchHTMLURLtostripped(url,stripped=[]):
 paras = HTMLtopara(urlToHTML(url))
 for para in paras:
 para = stripText(para)
 stripped.append(para)
 
def clean_name(test):
 test = re.sub('&amp;','&',test)
 test = re.sub('&#039;',"'",test)
 test = re.sub('★'," ",test)
 test = re.sub('°',"",test)
 return test # this function is for the kaggle dataset (anime.csv)

ani = pd.read_csv('anime.csv')
names = ani['name'].apply(clean_name)
names = names.reset_index()
names = names['name'].apply(stripText)
names = names.reset_index() #names = o/p list of anime titles
listOfNames = names['name'].tolist()
filtered_names = []
for name in listOfNames:
 if name not in english_words:
 if name not in ['af','isu','hana','tori'
 ,'osu','ryo','dr','oni'
 ,'ys','rec','hal','memories'
 ,'uba','kuro','kagami'
 ,'umo','nora','yuki']:
 filtered_names.append(name)
Dict_count = {}
for name in filtered_names:
 Dict_count[name] = 0 #Dict_count o/p as nameOfAnimeTitle: 0

stripped= []

crunchHTMLURLtostripped('https://old.reddit.com/r/anime/comments/5ag0kb/recommendation_tuesdays_week_of_november_01_2016/',stripped)
crunchHTMLURLtostripped('https://old.reddit.com/r/anime/comments/3pa2it/lets_list_anime_that_affected_your_emotions/',stripped)
crunchHTMLURLtostripped('https://old.reddit.com/r/anime/comments/947lub/good_anime_recommendations/',stripped)

for name in filtered_names:
 for para in stripped:
 if name in para:
 Dict_count[name] +=1
Dict_count

df = pd.DataFrame()
df['name'] = Dict_count.keys()
df['count'] = Dict_count.values()
df['count'].sort_values()
df.describe()

# Set condition: We only want the most significant series, so we shall only display those with a count greater than 5
cond = df['count'] > 5
df_filter = df[cond]
fig2 = plt.figure(figsize = (18,10))
plt.barh(df_filter['name'],df_filter['count'],color = 'lightcoral')
plt.title('Most Common Anime Titles from Web-Scraping of Subreddit Threads', fontsize = 20)

df_filter

genre_web = {}
for genre in genres:
 genre_web[genre] = 0 #creating the container for each genre.
#steins;gate: Sci-Fi, Thriller
genre_web['Sci-Fi'] += df_filter.iloc[0,1]
genre_web['Thriller'] += df_filter.iloc[0,1]
#hajime no ippo: Comedy, Sports, Drama, Shounen
genre_web['Comedy'] += df_filter.iloc[1,1]
genre_web['Sports'] += df_filter.iloc[1,1]
genre_web['Drama'] += df_filter.iloc[1,1]
genre_web['Shounen'] += df_filter.iloc[1,1]
#cowboy bebop: Action, Adventure, Comedy, Drama, Sci-Fi, Space
genre_web['Comedy'] += df_filter.iloc[2,1]
genre_web['Drama'] += df_filter.iloc[2,1]
genre_web['Adventure'] += df_filter.iloc[2,1]
genre_web['Action'] += df_filter.iloc[2,1]
genre_web['Sci-Fi'] += df_filter.iloc[2,1]
genre_web['Space'] += df_filter.iloc[2,1]
#death note: Mystery, Police, Psychological, Supernatural, Thriller, Shounen
genre_web['Shounen'] += df_filter.iloc[3,1]
genre_web['Thriller'] += df_filter.iloc[3,1]
genre_web['Supernatural'] += df_filter.iloc[3,1]
genre_web['Psychological'] += df_filter.iloc[3,1]
genre_web['Police'] += df_filter.iloc[3,1]
genre_web['Mystery'] += df_filter.iloc[3,1]
#cross game: Comedy, Drama, Romance, School, Shounen, Sports
genre_web['Drama'] += df_filter.iloc[4,1]
genre_web['Comedy'] += df_filter.iloc[4,1]
genre_web['Romance'] += df_filter.iloc[4,1]
genre_web['School'] += df_filter.iloc[4,1]
genre_web['Shounen'] += df_filter.iloc[4,1]
genre_web['Sports'] += df_filter.iloc[4,1]
# shinsekai yori: Sci-Fi, Mystery, Horror, Psychological, Supernatural, Drama
genre_web['Sci-Fi'] += df_filter.iloc[5,1]
genre_web['Mystery'] += df_filter.iloc[5,1]
genre_web['Horror'] += df_filter.iloc[5,1]
genre_web['Psychological'] += df_filter.iloc[5,1]
genre_web['Supernatural'] += df_filter.iloc[5,1]
genre_web['Drama'] += df_filter.iloc[5,1]
#fate/zero: Action, Supernatural, Magic, Fantasy
genre_web['Action'] += df_filter.iloc[6,1]
genre_web['Supernatural'] += df_filter.iloc[6,1]
genre_web['Magic'] += df_filter.iloc[6,1]
genre_web['Fantasy'] += df_filter.iloc[6,1]
#nichijou: Slice of Life, Comedy, School, Shounen
genre_web['Slice of Life'] += df_filter.iloc[7,1]
genre_web['Comedy'] += df_filter.iloc[7,1]
genre_web['School'] += df_filter.iloc[7,1]
genre_web['Shounen'] += df_filter.iloc[7,1]
#barakamon: Comedy, Slice of Life
genre_web['Comedy'] += df_filter.iloc[8,1]
genre_web['Slice of Life'] += df_filter.iloc[8,1]
#hunter x hunter: Action, Adventure, Super Power, Fantasy, Shounen
genre_web['Action'] += df_filter.iloc[9,1]
genre_web['Adventure'] += df_filter.iloc[9,1]
genre_web['Super Power'] += df_filter.iloc[9,1]
genre_web['Fantasy'] += df_filter.iloc[9,1]
genre_web['Shounen'] += df_filter.iloc[9,1]
#natsume yuujinchou: Slice of Life, Demons, Supernatural, Drama, Shoujo
genre_web['Slice of Life'] += df_filter.iloc[10,1]
genre_web['Demons'] += df_filter.iloc[10,1]
genre_web['Supernatural'] += df_filter.iloc[10,1]
genre_web['Drama'] += df_filter.iloc[10,1]
genre_web['Shoujo'] += df_filter.iloc[10,1]
#bakemonogatari: Romance, Supernatural, Mystery, Vampire
genre_web['Romance'] += df_filter.iloc[11,1]
genre_web['Supernatural'] += df_filter.iloc[11,1]
genre_web['Mystery'] += df_filter.iloc[11,1]
genre_web['Vampire'] += df_filter.iloc[11,1]
# death parade: Game, Mystery, Psychological, Drama, Thriller
genre_web['Mystery'] += df_filter.iloc[12,1]
genre_web['Game'] += df_filter.iloc[12,1]
genre_web['Psychological'] += df_filter.iloc[12,1]
genre_web['Drama'] += df_filter.iloc[12,1]
genre_web['Thriller'] += df_filter.iloc[12,1]
#fullmetal alchemist: Action, Adventure, Comedy, Drama, Fantasy, Magic, Military, Shounen
genre_web['Drama'] += df_filter.iloc[13,1]
genre_web['Comedy'] += df_filter.iloc[13,1]
genre_web['Adventure'] += df_filter.iloc[13,1]
genre_web['Action'] += df_filter.iloc[13,1]
genre_web['Fantasy'] += df_filter.iloc[13,1]
genre_web['Magic'] += df_filter.iloc[13,1]
genre_web['Military'] += df_filter.iloc[13,1]
genre_web['Shounen'] += df_filter.iloc[13,1]
# chihayafuru: Drama, Game, Josei, School, Slice of Life, Sports
genre_web['Drama'] += df_filter.iloc[14,1]
genre_web['Game'] += df_filter.iloc[14,1]
genre_web['Josei'] += df_filter.iloc[14,1]
genre_web['School'] += df_filter.iloc[14,1]
genre_web['Slice of Life'] += df_filter.iloc[14,1]
genre_web['Sports'] += df_filter.iloc[14,1]
#clannad: Comedy, Drama, Romance, School, Slice of Life, Supernatural
genre_web['Comedy'] += df_filter.iloc[15,1]
genre_web['Drama'] += df_filter.iloc[15,1]
genre_web['Romance'] += df_filter.iloc[15,1]
genre_web['School'] += df_filter.iloc[15,1]
genre_web['Slice of Life'] += df_filter.iloc[15,1]
genre_web['Supernatural'] += df_filter.iloc[15,1]
# kill la kill: Action, Comedy, Super Power, Ecchi, School
genre_web['Comedy'] += df_filter.iloc[16,1]
genre_web['Action'] += df_filter.iloc[16,1]
genre_web['Super Power'] += df_filter.iloc[16,1]
genre_web['Ecchi'] += df_filter.iloc[16,1]
genre_web['School'] += df_filter.iloc[16,1]
# plastic memories: Sci-Fi, Drama, Romance
genre_web['Romance'] += df_filter.iloc[17,1]
genre_web['Sci-Fi'] += df_filter.iloc[17,1]
genre_web['Drama'] += df_filter.iloc[17,1]
# nisekoi: Harem, Comedy, Romance, School, Shounen
genre_web['Romance'] += df_filter.iloc[18,1]
genre_web['Harem'] += df_filter.iloc[18,1]
genre_web['Comedy'] += df_filter.iloc[18,1]
genre_web['School'] += df_filter.iloc[18,1]
genre_web['Shounen'] += df_filter.iloc[18,1]
# flip flappers: Sci-Fi, Adventure, Comedy, Magic
genre_web['Sci-Fi'] += df_filter.iloc[19,1]
genre_web['Adventure'] += df_filter.iloc[19,1]
genre_web['Comedy'] += df_filter.iloc[19,1]
genre_web['Magic'] += df_filter.iloc[19,1]

df2 = pd.DataFrame()
df2['name'] =genre_web.keys()
df2['count'] = genre_web.values()
df_sort = df2.sort_values(by='count', ascending=False).reset_index()
plt.figure(figsize = (20,15))
sns.set(style="whitegrid")
sns.barplot(y=df_sort['name'],x=df_sort['count'])
sns.despine(left=True, bottom=True)
plt.title('Most Common Anime Genres from Web-Scraping of Subreddit Threads', fontsize = 25)
plt.xticks(np.arange(0,101,10))
