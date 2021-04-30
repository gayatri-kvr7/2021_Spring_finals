import numpy as np
import pandas as pd
import requests
import lxml.html
import re


def extract_year(some_data):
    some_data['FiscalYear'] = pd.DatetimeIndex(some_data['Date']).year
    some_data['FiscalYear'] = some_data['FiscalYear'].fillna(0).astype(np.int64)
    return some_data


def admissions(some_data):

