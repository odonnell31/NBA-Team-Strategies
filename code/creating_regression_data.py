# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 15:41:27 2020

@author: ODsLaptop

@title: creating regression dataset
"""

# import libraries
import pandas as pd

# loading nba team data
nba_data = pd.read_csv("https://raw.githubusercontent.com/odonnell31/NBA-Team-Strategies/main/data/nba_team_data_1990_v2.csv")

# create dataframe for only nba finals teams
nba_finals_teams = nba_data[nba_data['Finals_Team'] == 'Y']
nba_finals_teams = nba_finals_teams[nba_finals_teams['Year'] > 2012]
nba_finals_teams = nba_finals_teams.reset_index(drop=True)

"""
# calc years since last losing season
years_since_losing = []
consecutive_years_losing = []
consecutive_playoffs = []
for i in range(len(nba_finals_teams)):
    finals_year = nba_finals_teams['Year'][i]
    year_prior = finals_year - 1
    team = nba_finals_teams['Team'][i]
    last_losing_season = 0
    consec_losing_seasons = 0
    consec_playoffs = 0
    # flags
    losing = 0
    playoffs = 0
    
    # if the last season was a losing season:
    if nba_data.loc[(nba_data['Team'] == team) & (nba_data['Year'] == year_prior)]['Losing_season'].values[0] == "Y":
        last_losing_season = year_prior
        consec_losing_seasons += 1
        losing = 1
        year_prior -= 1
        
        # how many consecutive losing seasons were there?
        while losing == 1:
            if nba_data.loc[((nba_data['Team'] == team) & (nba_data['Year'] == year_prior))]['Losing_season'].values[0] == 'Y':
                consec_losing_seasons += 1
                year_prior -= 1
            else:
                losing = 0
    
    # if the last season was a winning season            
    elif nba_data.loc[((nba_data['Team'] == team) & (nba_data['Year'] == year_prior))]['Losing_season'].values[0] == 'N':
        
        # if the last season was also a playoffs seasons
        if nba_data.loc[((nba_data['Team'] == team) & (nba_data['Year'] == year_prior))]['Playoffs'].values[0] == 'Y':
            playoffs = 1
            consec_playoffs += 1
            year_prior -= 1
            
            # how many consecutive playoffs years were there?
            while playoffs == 1:
                
                # if previous season was playoffs season, add it.
                if nba_data.loc[((nba_data['Team'] == team) & (nba_data['Year'] == year_prior))]['Playoffs'].values[0] == 'Y':
                    consec_playoffs += 1
                    year_prior -= 1
                else:
                    playoffs = 0
                    
            # if its no longer a playoffs streak, was it a losing season
            if nba_data.loc[(nba_data['Team'] == team) & (nba_data['Year'] == year_prior)]['Losing_season'].values[0] == "Y":
                last_losing_season = year_prior
                consec_losing_seasons += 1
                losing = 1
                year_prior -= 1
                
        # if it was not a playoffs season, was it winning or losing?
        else:
            playoffs = 0
            year_prior -= 1
                    
            while losing == 0:
                
                if nba_data.loc[((nba_data['Team'] == team) & (nba_data['Year'] == year_prior))]['Losing_season'].values[0] == 'N':
                    year_prior -= 1
                    
                else:
                    last_losing_season = year_prior
                    consec_losing_seasons += 1
                    losing = 1
                    year_prior -= 1
                    
                    while losing == 1:
                        if nba_data.loc[((nba_data['Team'] == team) & (nba_data['Year'] == year_prior))]['Losing_season'].values[0] == 'Y':
                            consec_losing_seasons += 1
                            year_prior -= 1
                        else:
                            losing = 0
  
            
                    
    years_since_losing.append(finals_year - last_losing_season)
    consecutive_years_losing.append(consec_losing_seasons)
    consecutive_playoffs.append(consec_playoffs)
                
nba_finals_teams['years_since_losing_season'] = years_since_losing
nba_finals_teams['consecutive_years_losing'] = consecutive_years_losing
nba_finals_teams['consecutive_playoffs'] = consecutive_playoffs
            
"""

# calc number of consecutive losing seasons


# calc number of consecutive playoff seasons leading to final appearance


# calc years since last losing season
years_since_losing = []
consecutive_years_losing = []

for i in range(len(nba_finals_teams)):
    finals_year = nba_finals_teams['Year'][i]
    year_prior = finals_year - 1
    team = nba_finals_teams['Team'][i]
    last_losing_season = 0
    consec_losing_seasons = 0
    # flags
    losing = 0
    
    # if the last season was a losing season:
    if nba_data.loc[(nba_data['Team'] == team) & (nba_data['Year'] == year_prior)]['Losing_season'].values[0] == "Y":
        last_losing_season = year_prior
        consec_losing_seasons += 1
        losing = 1
        year_prior -= 1
        
        # how many consecutive losing seasons were there?
        while losing == 1:
            if nba_data.loc[((nba_data['Team'] == team) & (nba_data['Year'] == year_prior))]['Losing_season'].values[0] == 'Y':
                consec_losing_seasons += 1
                year_prior -= 1
            else:
                losing = 0
    
    # if the last season was a winning season            
    elif nba_data.loc[((nba_data['Team'] == team) & (nba_data['Year'] == year_prior))]['Losing_season'].values[0] == 'N':
        year_prior -= 1
        losing = 0
        
        while losing == 0:
            if nba_data.loc[((nba_data['Team'] == team) & (nba_data['Year'] == year_prior))]['Losing_season'].values[0] == 'N':
                year_prior -= 1
                losing = 0
                
            else:
                last_losing_season = year_prior
                consec_losing_seasons += 1
                year_prior -= 1
                losing = 1
                
        while losing == 1:
            if nba_data.loc[((nba_data['Team'] == team) & (nba_data['Year'] == year_prior))]['Losing_season'].values[0] == 'Y':
                consec_losing_seasons += 1
                year_prior -= 1
                losing = 1
                
            else:
                losing = 0
            
                    
    years_since_losing.append(finals_year - last_losing_season)
    consecutive_years_losing.append(consec_losing_seasons)
    #consecutive_playoffs.append(consec_playoffs)
                
nba_finals_teams['years_since_losing_season'] = years_since_losing
nba_finals_teams['consecutive_years_losing'] = consecutive_years_losing
#nba_finals_teams['consecutive_playoffs'] = consecutive_playoffs