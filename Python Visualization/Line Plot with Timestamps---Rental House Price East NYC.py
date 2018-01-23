#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:19:17 2018

@author: kerry
"""

import matplotlib.pyplot as plt
from matplotlib import dates
import quandl

print('\tStyles Available to Use\n', plt.style.available)
plt.style.use('seaborn')
# Zillow Home Value Index (Neighborhood): Median Rental Price - One Bedroom - East New York
one_bedroom = quandl.get("ZILLOW/N15706_MRP1B", authtoken="ugSzAwsLjFpwqPBn_JBc")
# Zillow Home Value Index (Neighborhood): Median Listing Price - Three Bedrooms - East New York
three_bedroom = quandl.get("ZILLOW/N15706_MLP3B", authtoken="ugSzAwsLjFpwqPBn_JBc")

# convert date to numbers
one_datenums=dates.date2num(one_bedroom.index.to_pydatetime())

# format date as year/month/day
xfmt = dates.DateFormatter('%Y-%m-%d')
# calling gca
ax=plt.gca()
# Get the current Axes instance on the current figure matching the given keyword args, or create one.
ax.xaxis.set_major_formatter(xfmt)

# rotate the x-axis label so that it is easier for people to see
plt.xticks( rotation=25 )
# title 
plt.title('Rental Price of East New York(One Bedroom)')
plt.plot(one_datenums, one_bedroom.Value, color = 'red' )


plt.xlabel('Time')
plt.ylabel('Price')
plt.show()

plt.title('Rental Price of East New York(Three Bedroom)')
three_datenums = dates.date2num(three_bedroom.index.to_pydatetime())
xfmt = dates.DateFormatter('%Y-%m-%d')
ax=plt.gca()
ax.xaxis.set_major_formatter(xfmt)
plt.xticks( rotation=25 )
plt.plot(three_datenums, three_bedroom.Value, color = 'blue')
plt.xlabel('Time')
plt.ylabel('Price')

plt.show()


