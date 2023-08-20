#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) Write a python program to display all the header tags from wikipedia.org and make data frame.

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.wikipedia.org'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
header_text = [header.get_text() for header in headers]
header_tags = [header.name for header in headers]

df = pd.DataFrame({'Header Tag': header_tags, 'Text': header_text})
print(df)


# In[3]:


#3-Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
#a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
#b) Top 10 ODI Batsmen along with the records of their team andrating.
#c) Top 10 ODI bowlers along with the records of their team andrating.



import pandas as pd
import requests
from bs4 import BeautifulSoup

# Scrape top 10 ODI teams in men's cricket
url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', class_='table')
rows = table.find_all('tr')

data = []
for row in rows[1:11]:
    cols = row.find_all('td')
    rank = cols[0].text.strip()
    team = cols[1].text.strip()
    matches = cols[2].text.strip()
    points = cols[3].text.strip()
    rating = cols[4].text.strip()
    data.append([rank, team, matches, points, rating])

teams_df = pd.DataFrame(data, columns=['Rank', 'Team', 'Matches', 'Points', 'Rating'])

# Scrape top 10 ODI batsmen in men's cricket
url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', class_='table')
rows = table.find_all('tr')

data = []
for row in rows[1:11]:
    cols = row.find_all('td')
    rank = cols[0].text.strip()
    player = cols[1].text.strip()
    team = cols[2].text.strip()
    rating = cols[3].text.strip()
    data.append([rank, player, team, rating])

batsmen_df = pd.DataFrame(data, columns=['Rank', 'Player', 'Team', 'Rating'])

# Scrape top 10 ODI bowlers in men's cricket
url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', class_='table')
rows = table.find_all('tr')

data = []
for row in rows[1:11]:
    cols = row.find_all('td')
    rank = cols[0].text.strip()
    player = cols[1].text.strip()
    team = cols[2].text.strip()
    rating = cols[3].text.strip()
    data.append([rank, player, team, rating])

bowlers_df = pd.DataFrame(data, columns=['Rank', 'Player', 'Team', 'Rating'])

# Display the dataframes
print("Top 10 ODI Teams in Men's Cricket:")
print(teams_df)
print("\nTop 10 ODI Batsmen in Men's Cricket:")
print(batsmen_df)
print("\nTop 10 ODI Bowlers in Men's Cricket:")
print(bowlers_df)


# In[1]:


#4-Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
#a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
#b) Top 10 women’s ODI Batting players along with the records of their team and rating.
#c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get the top 10 ODI teams in women's cricket
def get_top_10_teams():
    url = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', class_='table')
    rows = table.find_all('tr')
    data = []
    for row in rows[1:11]:
        cols = row.find_all('td')
        team = cols[1].text.strip()
        matches = cols[2].text.strip()
        points = cols[3].text.strip()
        rating = cols[4].text.strip()
        data.append([team, matches, points, rating])
    df = pd.DataFrame(data, columns=['Team', 'Matches', 'Points', 'Rating'])
    return df

# Function to get the top 10 ODI batting players in women's cricket
def get_top_10_batting_players():
    url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', class_='table')
    rows = table.find_all('tr')
    data = []
    for row in rows[1:11]:
        cols = row.find_all('td')
        name = cols[1].text.strip()
        team = cols[2].text.strip()
        rating = cols[3].text.strip()
        data.append([name, team, rating])
    df = pd.DataFrame(data, columns=['Name', 'Team', 'Rating'])
    return df

# Function to get the top 10 ODI all-rounders in women's cricket
def get_top_10_all_rounders():
    url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', class_='table')
    rows = table.find_all('tr')
    data = []
    for row in rows[1:11]:
        cols = row.find_all('td')
        name = cols[1].text.strip()
        team = cols[2].text.strip()
        rating = cols[3].text.strip()
        data.append([name, team, rating])
    df = pd.DataFrame(data, columns=['Name', 'Team', 'Rating'])
    return df

# Get the top 10 ODI teams in women's cricket
top_10_teams_df = get_top_10_teams()

# Get the top 10 ODI batting players in women's cricket
top_10_batting_players_df = get_top_10_batting_players()

# Get the top 10 ODI all-rounders in women's cricket
top_10_all_rounders_df = get_top_10_all_rounders()

# Display the data frames
print("Top 10 ODI Teams in Women's Cricket:")
print(top_10_teams_df)
print("\nTop 10 ODI Batting Players in Women's Cricket:")
print(top_10_batting_players_df)
print("\nTop 10 ODI All-Rounders in Women's Cricket:")
print(top_10_all_rounders_df)


# In[ ]:


#5-Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame-
#i) Headline
#ii) Time
#iii) News Link


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get the news details from CNBC World News
def get_news_details():
    url = "https://www.cnbc.com/world/?region=world"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    articles = soup.find_all('div', class_='Card-titleContainer')
    data = []
    for article in articles:
        headline = article.find('a').text.strip()
        time = article.find('time').text.strip()
        link = article.find('a')['href']
        data.append([headline, time, link])
    df = pd.DataFrame(data, columns=['Headline', 'Time', 'Link'])
    return df

# Get the news details from CNBC World News
news_df = get_news_details()

# Display the data frame
print("News Details from CNBC World News:")
print(news_df)


# In[3]:


#6-Write a python program to scrape the details of most downloaded articles from AI in last 90 days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles Scrape below mentioned details and make data frame-
#i) Paper Title
#ii) Authors
#iii) Published Date
#iv) Paper URL

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get the details of the most downloaded articles from AI in the last 90 days
def get_most_downloaded_articles():
    url = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    articles = soup.find_all('div', class_='pod-listing')
    data = []
    for article in articles:
        title = article.find('h3').text.strip()
        authors = article.find('p', class_='authors').text.strip()
        date = article.find('p', class_='date').text.strip()
        link = article.find('a')['href']
        data.append([title, authors, date, link])
    df = pd.DataFrame(data, columns=['Title', 'Authors', 'Date', 'Link'])
    return df

# Get the details of the most downloaded articles from AI in the last 90 days
articles_df = get_most_downloaded_articles()

# Display the data frame
print("Most Downloaded Articles from AI in Last 90 Days:")
print(articles_df)


# In[ ]:


#7-Write a python program to scrape mentioned details from dineout.co.in and make data frame-
#i) Restaurant name
#ii) Cuisine
#iii) Location
#iv) Ratings
#v) Image URL

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set the URL to scrape
url = 'https://www.dineout.co.in/delhi-restaurants'

# Make a GET request to the URL
response = requests.get(url)

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Create empty lists to store the scraped data
restaurant_names = []
cuisines = []
locations = []
ratings = []
image_urls = []

# Find all restaurant elements on the page
restaurants = soup.find_all('div', class_='restnt-card')

# Loop through each restaurant element and extract the required information
for restaurant in restaurants:
    # Extract the restaurant name
    name = restaurant.find('a', class_='restnt-name ellipsis').text.strip()
    restaurant_names.append(name)
    
    # Extract the cuisine information
    cuisine = restaurant.find('div', class_='double-line-ellipsis').text.strip()
    cuisines.append(cuisine)
    
    # Extract the location information
    location = restaurant.find('div', class_='restnt-loc ellipsis').text.strip()
    locations.append(location)
    
    # Extract the rating information
    rating = restaurant.find('span', class_='rating').text.strip()
    ratings.append(rating)
    
    # Extract the image URL
    image_url = restaurant.find('img')['src']
    image_urls.append(image_url)

# Create a data frame with the scraped data
data = {
    'Restaurant Name': restaurant_names,
    'Cuisine': cuisines,
    'Location': locations,
    'Rating': ratings,
    'Image URL': image_urls
}
df = pd.DataFrame(data)

# Display the data frame
print(df)

