from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# create new figure, axes instances.
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
# setup mercator map projection.
m = Basemap(llcrnrlon=43.,llcrnrlat=23.,urcrnrlon=63.,urcrnrlat=41.,
            rsphere=(6378137.00,6356752.3142),
            resolution='l',projection='merc',
            lat_0=40.,lon_0=-20.,lat_ts=20.)
# nylat, nylon are lat/lon
nylat = 40.78; nylon = -73.98
# lonlat, lonlon are lat/lon
lonlat = 51.53; lonlon = 0.08

m.drawcoastlines()
m.drawcountries()
m.fillcontinents()


m.drawparallels(range(20,45,5),labels=[1,0,0,0])
m.drawmeridians(range(45,65,5),labels=[0,0,0,1])




data = pd.read_csv('data-frame.csv')


lon = data['x']
lat = data['y']
x,y = m(lon.values,lat.values)
citi_name = data['name']
population = np.array(data["population"])
s = population / 10000

plt.scatter(x,y, color="Green",label="population",s=list(s), alpha=0.5)



for i in range(len(citi_name)):
    if citi_name[i] == 'karag':
        x[i] = x[i] - 200000
    plt.text(x[i]+10000,y[i]+10000,citi_name[i],fontsize=8 )



plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="upper right")
plt.title("iran-10-biggest-population")


plt.show()