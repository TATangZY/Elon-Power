#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 18:45:08 2023

@author: Mack
"""

cook = '__utma=10102256.1412599872.1678646744.1678646753.1678646753.1; __utmb=10102256.11.9.1678647127319; __utmc=10102256; __utmz=10102256.1678646753.1.1.utmcsr=trends.google.com|utmccn=(referral)|utmcmd=referral|utmcct=/; SIDCC=AFvIBn9z67xIE_7ISX3JI6jT7M6pV-6XdP1omPqy7vXB_pjLVS9S-R17p9ZMSSv1Dj-3UvoGnabw; __Secure-1PSIDCC=AFvIBn-_oxbgPyDQJYjME1_NlyQ0A-_70oDckXaGYWCMqPRum6ka3cpMNbecBMNsRnjjefAqqNnk; __Secure-3PSIDCC=AFvIBn_uiA7GjOjoYdhvRIGCdI2e6Y5f66O_x_VKfv9V6PifhJtKUGBEMOTy8XiYalse0PjxOLk; _ga_VWZPXDNJJB=GS1.1.1678646744.1.1.1678647361.0.0.0; _ga=GA1.3.1412599872.1678646744; _gat_gtag_UA_4401283=1; _gid=GA1.3.1893447336.1678646745; OTZ=6939046_84_88_104280_84_446940; 1P_JAR=2023-03-12-18; NID=511=OuWsBl_f6Rzqi-Fqyouhy5X9vTnO5NU09imD4nRC549YjY5LOW1ws9lvFSdsbucMvYw9LCil6G1Fglu3knVEEgEi9VQ9yjU3_8AxhJS2SmjIHzVwpH4GyJcAqWlFDlxGIGQVvsBrT5ELDFKJ_vaj4aSert3amOAO7vRogFLad1xmf9qTYEdIokz2z4oFU2VXI93K6ritSkiEfvZ7LHbyOicyQS3Oo8lkRDyPZw35zYOyhFtde5SGkoR-SJ6CPKU2NaD8dYM7S9jwhrp6K4b0PaAWL3jf5fSF0ebcirqERqyxVM9IsNYFlJqE4n7diTATggi2n0KUvPuhUY4x7FCsOgW0QPuNHkyfIpyAF1CCr95tuoUtdDOv3QnidoLCLXfMd03I0yKMcTr-VErWrm63t54EPZOf; AEC=ARSKqsIAw4KQkT_LrxA27_gPnjSlLszqFLHLSn6F7fcyVFEIJ952TIHnEA; APISID=j1y-gIRiDDYj74mh/AmCA73W8647xS1mVK; HSID=Aaz1ecjVMqMRLFaZQ; SAPISID=fJzdxwP9ijr7-Iei/Ay6QniFtKOERLw_Cp; SID=UQhslpwMHdQtDk60Qoto89fUV6SulEkbGtdfM_z8T10SKKMaS6JuYrgKMxolQNdvd8X3hQ.; SSID=A5YJahKJMoLRoVjEJ; __Secure-1PAPISID=fJzdxwP9ijr7-Iei/Ay6QniFtKOERLw_Cp; __Secure-1PSID=UQhslpwMHdQtDk60Qoto89fUV6SulEkbGtdfM_z8T10SKKMagOMrkN9lA2E1YUtgZVtOzw.; __Secure-3PAPISID=fJzdxwP9ijr7-Iei/Ay6QniFtKOERLw_Cp; __Secure-3PSID=UQhslpwMHdQtDk60Qoto89fUV6SulEkbGtdfM_z8T10SKKMa-e7xyZjCxwAQZHfxwJ235A.; ANID=AHWqTUmv_4AH2oQgEw8JUmw0COEY_hlGbURjn_JnkKx6UFoDde1MMA9rX_mecMqW'

import pandas as pd

def plot_trends(keywords, cookie, keydates= [], tf = 'today 3-m'):
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

    pytrends = TrendReq(requests_args = {'headers': {'Cookie': cookie}})

    pytrends.build_payload(keywords, cat=0, timeframe=tf, geo='', gprop='')

    df = pytrends.interest_over_time()
    axv = df.plot.line()
    for keydate in keydates:
        axv.axvline(keydate, color="r", linewidth=0.5)
        
    return df

def search_change(keywords, keydate, dayframe, cookie, tf = 'today 3-m'):
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

    pytrends = TrendReq(requests_args = {'headers': {'Cookie': cookie}})

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

def find_key_dates(keywords, cookie, threshlow = 0, threshhigh = 100, tf = 'today 3-m'):
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
    
    pytrends = TrendReq(requests_args = {'headers': {'Cookie': cookie}})

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
