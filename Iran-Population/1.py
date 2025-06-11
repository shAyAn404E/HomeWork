import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('data-frame.csv')

x = data["x"]
y = data["y"]
population = np.array(data["population"])
s = population / 3000

plt.scatter(x,y, color="Green",label="population",s=list(s), alpha=0.5)


plt.xlabel("Longitude")
plt.xticks(rotation=45)
plt.ylabel("Latitude")
plt.yticks(rotation=45)
plt.legend()
plt.grid( )



plt.title("iran-10-biggest-population")
plt.show()




