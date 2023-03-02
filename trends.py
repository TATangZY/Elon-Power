#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 18:45:08 2023

@author: Mack
"""

import pandas as pd

def plot_trends(keywords, keydates= [], tf = 'today 3-m'):
    '''
    
    Description
    -----------
    A function that plots the trends in google searches of up to five keywords
    on the same graph over a certain timeframe. Also adds a vertical line at 
    each specified keydate, if given them.

    Parameters
    ----------
    keywords : list
        A list of keywords to plot.
    keydates : list, optional
        A list of keydates to add vertical lines at. The default is [].
    tf : a pytrends timeframe code, optional
        The timeframe to plot over. The default is 'today 3-m'.

    Returns
    -------
    df : pd.DataFrame
        A dataframe containing all of the data that was plotted.

    '''
    from pytrends.request import TrendReq

    pytrends = TrendReq(hl='en-US', tz=360)

    pytrends.build_payload(keywords, cat=0, timeframe=tf, geo='', gprop='')

    df = pytrends.interest_over_time()
    axv = df.plot.line()
    for keydate in keydates:
        axv.axvline(keydate, color="black", linestyle="dashed")
        
    return df

def search_change(keywords, keydate, dayframe, tf = 'today 3-m'):
    '''
    
    Description
    -----------
    A function that determines the change in relative search rate over a 
    specified timeframe for each keyword in a given list.

    Parameters
    ----------
    keywords : list
        A list of keywords to find the change in search rates of.
    keydate : datetime
        The center of the range of time to find the change over.
    dayframe : int
        The number of days on each side of the keydate to find the change over.
    tf : a pytrends timeframe code, optional
        The timeframe to have access to. The default is 'today 3-m'.

    Returns
    -------
    deltatab : list
        A list containing the changes for each keyword.

    '''
    from pytrends.request import TrendReq
    from datetime import datetime, timedelta

    pytrends = TrendReq(hl='en-US', tz=360)

    pytrends.build_payload(keywords, cat=0, timeframe=tf, geo='', gprop='')
    
    df = pytrends.interest_over_time()
    deltatab = []
    
    Date = datetime.strptime(keydate, '%Y-%m-%d')
    
    for keyword in keywords:
        delta = df.at[Date + timedelta(days = dayframe), keyword] - df.at[Date - timedelta(days = dayframe), keyword]
        deltatab.append(delta)
    return deltatab

def find_peaks(x, thresh_low, thresh_high):
    import scipy.signal as sig
    
    peaks, _ = sig.find_peaks(x)

    locations = []
    for peak in peaks:
        if x[peak] >= thresh_low and x[peak] <= thresh_high:
          locations.append(peak)

    return locations

def find_key_dates(keywords, threshlow = 0, threshhigh = 100, tf = 'today 3-m'):
    '''
    
    Description
    -----------
    A function that finds the dates of spikes in a given timeframe for each 
    keyword in a given list.

    Parameters
    ----------
    keywords : list
        A list of keywords to find the key dates of.
    threshlow : int, optional
        The lowest relative search rate to count as a spike. The default is 0.
    threshhigh : int, optional
        The highest relative search rate to count as a spike. The default is 100.
    tf : a pytrends timeframe code, optional
        The timeframe to search for key dates over. The default is 'today 3-m'.

    Returns
    -------
    kdates : pd.DataFrame
        A dataframe containing the key dates for each keyword.

    '''
    from pytrends.request import TrendReq
    
    pytrends = TrendReq(hl='en-US', tz=360)

    pytrends.build_payload(keywords, cat=0, timeframe=tf, geo='', gprop='')

    df = pytrends.interest_over_time()
    
    klocs = []
    for keyword in df.columns:
        if keyword != "isPartial":
            spikes = find_peaks(df[keyword], threshlow, threshhigh)
            klocs.append(spikes)

    dates = []
    for kword in klocs:
        spikedates = []
        for spike in kword:
            spikedates.append(df.index[spike])
        dates.append(spikedates)
    
    kdates = pd.DataFrame(dates, keywords)
    
    return kdates