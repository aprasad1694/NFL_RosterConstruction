# analysis does not take into account rollover or dead CAP

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

""" Need to create the URLs """
# internet archive source -- years 2000 - 2009 ;
#2002 was first 'Texans' -- if year >= 2002, int_arch_teams.append('Texans')
int_arch_teams = ['Jets','Eagles','Cowboys','Dolphins','Falcons',
                'Colts','Bengals','Browns','Lions','Patriots','Giants','Redskins',
                'Ravens','Panthers','Steelers','Jaguars','Buccaneers','Bills',
                'Bears','Rams','Saints','Vikings','Titans','Packers','Chiefs',
                'Broncos','Cardinals','Chargers','49ers','Raiders','Seahawks']
# spotrac source -- years: 2011 - 2017 ;
#2015 was last year for the san-diego-chargers before 2016 being los-angeles-chargers
spotrac_teams = ['new-york-jets','philadelphia-eagles','dallas-cowboys','houston-texans',
                'miami-dolphins','atlanta-falcons', 'indianapolis-colts','cincinnati-bengals',
                'cleveland-browns','detroit-lions','new-england-patriots','new-york-giants',
                'washington-redskins', 'baltimore-ravens','carolina-panthers','pittsburgh-steelers',
                'jacksonville-jaguars','tampa-bay-buccaneers','buffalo-bills','chicago-bears',
                'st.-louis-rams','new-orleans-saints','minnesota-vikings','tennessee-titans',
                'green-bay-packers','kansas-city-chiefs','denver-broncos','arzona-cardinals',
                'san-diego-chargers','san-francisco-49ers','oakland-raiders','seattle-seahawks']
def create_int_arch_url(pg, team_str, yr):
    one_yr_urls = []
    for team in team_str:
        url = pg % (team, yr)
        one_yr_urls.append(url)
    return one_yr_urls
def create_all_yr_urls():
    """CREATES ALL OF THE URLS OF ALL TEAMS BETWEEN YEARS 2000 AND 2017 (INCLUSIVE)"""
    url_lst = []
    url = 'https://web.archive.org/web/20110622061736/http://content.usatoday.com:80/sportsdata/football/nfl/%s/salaries/%s'
    for i in np.arange(2000,2018):
        #Internet ARchive when 2000 <= i <=2009
        if i < 2010:
            url = 'https://web.archive.org/web/20110622061736/http://content.usatoday.com:80/sportsdata/football/nfl/%s/salaries/%s'
            if i == 2002:
                int_arch_teams.append('Texans')
                url_lst.append(create_int_arch_url(url, int_arch_teams, i))
            elif i > 2002:
                url_lst.append(create_int_arch_url(url, int_arch_teams, i))
                # for team in int_arch_teams:
                #     url = 'https://web.archive.org/web/20110622061736/http://content.usatoday.com:80/sportsdata/football/nfl/%s/salaries/%s' % (team, i)
                #     print(url)
            else:
                try:
                    int_arch_teams.remove('Texans')
                except ValueError:
                    url_lst.append(create_int_arch_url(url, int_arch_teams, i))
        elif i == 2010:
            continue
        else:
            #spotrac website for years 2011 - 2017
            url = 'https://www.spotrac.com/nfl/%s/cap/%s/'
            if i < 2016:
                url_lst.append(create_int_arch_url(url, int_arch_teams, i))
            elif i == 2016:
                try:
                    spotrac_teams.remove('st.-louis-rams')
                except ValueError:
                        spotrac_teams.append('los-angeles-rams')
                spotrac_teams.append('los-angeles-rams')
                url_lst.append(create_int_arch_url(url, int_arch_teams, i))
            else:
                try:
                    spotrac_teams.remove('san-diego-chargers')
                except ValueError:
                        url_lst.append(create_int_arch_url(url, int_arch_teams, i))
                        continue
                spotrac_teams.append('los-angeles-chargers')
                url_lst.append(create_int_arch_url(url, int_arch_teams, i))
                # create_int_arch_url(url, int_arch_teams, i)
    flat_url_lst = [item for sublist in url_lst for item in sublist]
    return flat_url_lst


test = create_all_yr_urls()
print(len(test))

    # break
    #spotrac when 2011 <= i <=2017

""" use pandas read_html fct to get data from url spit out by fct above"""


""" Make differential transformations to data based on source  """
""" For internet archive website """
# organization column
# year column
# drop the 'ALL BONUSES' column

""" For spotrac data """
# organization column
# year column
# drop these columns : 'ROSTER BONUS', 'OPTION BONUS', 'WORKOUT BONUS', 'RESTRUC. BONUS', 'MISC.', 'DEAD CAP'
