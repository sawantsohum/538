# importing csv module 
import csv 
from decimal import Decimal 
# csv file name 
filename = "soccer-spi/spi_global_rankings.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 
leagues = {} 
avgSpi = {}
leagueSpi = {}
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
for row in rows:
    league = row[3]
    spi = float(row[6])
    # If the league already exists (league, entries + 1)
    # If the league doesn't exist add the mapping (league, 1)
    if league in leagues:
        numTeams = leagues[league]
        currSpi = leagueSpi[league]
        leagues[league] = numTeams + 1
        leagueSpi[league] = currSpi + spi
    else:
        leagues[league] = 1
        leagueSpi[league] = spi
for league in leagues:
    avgSpi[league] = leagueSpi[league] / leagues[league]
# print(avgSpi)
sort_leagues = sorted(avgSpi.items(), key=lambda x: x[1], reverse=True)
rank = 1
for i in sort_leagues:
    print("Rank:", rank, "League:", i[0], "SPI Average", i[1])
    rank+= 1

# csv file name 
filename = "soccer-spi/spi_global_rankings_intl.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 
leagues = {} 
avgSpi = {}
leagueSpi = {}
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
for row in rows:
    league = row[2]
    spi = float(row[5])
    # If the league already exists (league, entries + 1)
    # If the league doesn't exist add the mapping (league, 1)
    if league in leagues:
        numTeams = leagues[league]
        currSpi = leagueSpi[league]
        leagues[league] = numTeams + 1
        leagueSpi[league] = currSpi + spi
    else:
        leagues[league] = 1
        leagueSpi[league] = spi
for league in leagues:
    avgSpi[league] = leagueSpi[league] / leagues[league]
# print(avgSpi)
sort_leagues = sorted(avgSpi.items(), key=lambda x: x[1], reverse=True)
rank = 1
for i in sort_leagues:
    print("Rank:", rank, "Confederation:", i[0], "SPI Average", i[1])
    rank+= 1