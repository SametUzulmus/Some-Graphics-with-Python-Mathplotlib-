# These lines of code show the simple supply demand market equilibrium in the economy.
# The market does not depend on equilibrium functions, it is just shown.
# Libraries used: Matplotlib, Numpy, Pandas

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig=plt.figure(figsize=(8,6))
ax = plt.subplot2grid((1,1),(0,0)) 

x=np.array([0,5,10])
y=np.array([0,10,20])

x1=np.array([10,0])
y1=np.array([0,20])

ax.plot([0,5,5], [10,10,0], "r--o")

ax.plot(x,y,x1,y1,marker="o",markerfacecolor="red")

ax.set_title("Simple Suppy Demand Graph")
ax.set_ylabel("Price Level")
ax.set_xlabel("Quantity Level")
ax.set_ylim(0,25)
ax.set_xlim(0,15)

ax.annotate("(P: {}, Q:{})".format(10, 5),xy=(5,10),xytext=(7+(5/10), 10),arrowprops=dict(facecolor='red', shrink=0.10),
            fontsize = 10,color = "black",fontweight = "bold")
