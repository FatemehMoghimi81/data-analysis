import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import random

dataset = pd.read_excel(r"D:\DA\DA 01 tamrin\10_iranian_cities.xlsx")
# print(dataset)
# dataset.to_csv("10_iranian_cities.csv")





# create new figure, axes instances.
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])

# setup mercator map projection.
m = Basemap(llcrnrlon=40.,llcrnrlat=20.,urcrnrlon=70.,urcrnrlat=45.,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            lat_0=40.,lon_0=-20.,lat_ts=20.)

# nylat, nylon are lat/lon of Iran
nylat = 40.78; nylon = -73.98
# lonlat, lonlon are lat/lon of Iran.
lonlat = 51.53; lonlon = 0.08

#  m.drawgrea atcircle(nylon,nylat,lonlon,lonlat,linewidth=2,color='b')
m.drawcoastlines()
m.fillcontinents()
m.drawcountries()
m.drawcounties()
m.drawstates()

colors =[]
for _ in range(len(dataset)):
    r = random.random()  # Red component (0.0 to 1.0)
    g = random.random()  # Green component (0.0 to 1.0)
    b = random.random()  # Blue component (0.0 to 1.0)
    colors.append((r, g, b))

x,y = m(dataset["lon"], dataset["lat"] )
m.scatter(x , y , s=dataset["population"]*10, c = colors)
ax.set_title('Iran')
plt.show()
