import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from find_tweets import *

df = pd.read_csv('elonmusk.csv')
followers = np.array(df['followers'])
change = np.array(df['change'])
date = np.array(df['date'])

peaks,_ = find_peaks(change)
peak_dates = date[peaks]

print(extract_tweets(peak_dates[0]))




