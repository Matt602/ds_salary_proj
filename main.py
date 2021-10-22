# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:10:39 2021

@author: matth
"""

import glassdoor_scraper as gs
import pandas as pd

path = 'C:/Users/matth/dsDocuments/ds_salary_proj/chromedriver'

df = gs.get_jobs('data scientist', 1000, False, path, 15)


df.to_csv('glassdoor_jobs.csv', index = False)