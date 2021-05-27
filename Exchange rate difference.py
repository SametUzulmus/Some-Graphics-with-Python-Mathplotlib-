### These lines of code show Turkey's dollar and euro exchange rates between 2010 and 2020 and the rate of change of these rates over the years.

### Libraries used: Pandas , Numpy , Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data={"Dollar / TL" :(1.5084,1.6788,1.8007,1.9061,2.1921,2.7258,3.0277,3.6557,4.8241,5.6826,7.0234),
      "Euro / TL": (1.9991,2.3338,2.3151,2.5316,2.9112,3.0235,3.3471,4.1273,5.6751,6.3607,8.0453)}
variables=pd.DataFrame(data,index=["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"])

def degisim(a,b):
     return 100*(b/a)-100

variables["Percent Change Euro / TL"]=[degisim(variables.loc[f"{i}"]["Euro / TL"],variables.loc[f"{2020 if i>=2020 else i+1}"]["Euro / TL"])for i in range(2010,2021)]
variables["Percent Change Dollar / TL"]=[degisim(variables.loc[f"{i}"]["Dollar / TL"],variables.loc[f"{2020 if i>=2020 else i+1}"]["Dollar / TL"])for i in range(2010,2021)]  

fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(15,5))



axes[0].plot(variables["Dollar / TL"],"blue",marker="o",markerfacecolor="red",label="Dollar / TL")
axes[0].plot(variables["Euro / TL"],"red",marker="o",markerfacecolor="black",label="Euro / TL")
axes[1].plot(variables["Percent Change Euro / TL"],"red",marker="o",markerfacecolor="black",label="Rate Change(%) Euro / TL")
axes[1].plot(variables["Percent Change Dollar / TL"],"blue",marker="o",markerfacecolor="black",label="Rate Cahange(%) Dollar/ TL")

axes[0].set_title("Between 2010-2020 Dollar / TL - Euro / TL",fontsize=13,color="black")
axes[0].set_ylabel("Price",fontsize=15,color="black")
axes[0].set_xlabel("Years",fontsize=15,color="black")

axes[1].set_title("""Proportional changes of dollar and euro-
among themselves. Between 2010-2020""",fontsize=13,color="black")

axes[1].set_ylabel("Rate(%)",fontsize=15,color="black")
axes[1].set_xlabel("Years",fontsize=15,color="black")
axes[0].legend()
axes[1].legend()
