"""
Install required packages.

pip install pandas
pip install seaborn
pip install openpyxl
"""

import datetime
'''
import os
import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
import seaborn as sns  # type: ignore
from dotenv import load_dotenv  # type: ignore
from db_functions import get_members
from cohort_analysis import get_analysis

DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DB = os.getenv("DB")

load_dotenv()
members = get_members()

#get_analysis(members, '2022-05-01', '2022-05-22')
'''
now_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
print(now_timestamp)