import urllib
import csv
from bs4 import BeautifulSoup
FBSRushing='https://www.cbssports.com/collegefootball/stats/leaders/NCAAF/RYDS/regularseason'
page = urllib.request.urlopen(FBSRushing).read()
soup = BeautifulSoup(page)
table = soup.find('table')
x = (len(table.findAll('tr')) - 1)
f = csv.writer(open("RushingLeaders.csv", "w"))
f.writerow([ "Rank","Name", "School", "Attempts", "Yards", "YPA", "YPG", "TD"])
for row in table.findAll('tr')[2:x]:
    col = row.findAll('td')
    rank = col[0].getText()
    name = col[1].getText()
    school = col[2].getText()
    attempts = col[3].getText()
    yards = col[4].getText()
    ypa = col[5].getText()
    ypg = col[6].getText()
    touchdowns = col[7].getText()
    player = (rank, name, school, attempts, yards, ypa, ypg, touchdowns)
    f.writerow(player)