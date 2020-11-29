# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:46:48 2020

@author: Michael ODonnell

@title: scraping NBA team data
"""

# import needed libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# Choose NBA seasons to scrape
year = 2018

# URL to scrape
url = f"https://www.basketball-reference.com/leagues/NBA_{year}_standings.html"

# HTML data collected
html = urlopen(url)

# create bs4 object from HTML
soup = BeautifulSoup(html, features="lxml")

# use findALL() to get the column headers
#soup.findAll('tr', limit=2)

# use getText()to extract the headers into a list
titles = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

# first, find only column headers
headers = titles[1:titles.index("SRS")+1]

# then, update the titles list to exclude first set of column headers
titles = titles[titles.index("SRS")+1:]

# then, grab all row titles (ex: Boston Celtics, Toronto Raptors, etc)
row_titles = titles[0:titles.index("Eastern Conference")]
# remove the non-teams from this list
for i in headers:
    row_titles.remove(i)
row_titles.remove("Western Conference")

# next, grab all data from rows (avoid first row)
rows = soup.findAll('tr')[1:]
team_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
# remove empty elements
team_stats = [e for e in team_stats if e != []]
# only keep needed rows
team_stats = team_stats[0:len(row_titles)]

# add team to each row in team_stats
for i in range(0, len(team_stats)):
    team_stats[i].insert(0, row_titles[i])
    team_stats[i].insert(0, year)
    
# add team column to headers
headers.insert(0, "Team")
headers.insert(0, "Year")


# finally, create dataframe with all aquired info
year_standings = pd.DataFrame(team_stats, columns = headers)
print(year_standings)

# add column to dataframe to indicate playoff appearance
year_standings["Playoffs"] = ["Y" if "*" in ele else "N" for ele in year_standings["Team"]]
# remove * from team names
year_standings["Team"] = [ele.replace('*', '') for ele in year_standings["Team"]]