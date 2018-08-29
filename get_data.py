# analysis does not take into account rollover or dead CAP

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

""" Need to create the URLs """
# internet archive source -- years 2000 - 2009 ;
#2002 was first 'Texans' -- if year >= 2002, int_arch_teams.append('Texans')
int_arch_teams = ['Jets','Eagles','Cowboys','Texans','Dolphins','Falcons',
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
