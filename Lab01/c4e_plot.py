import matplotlib

matplotlib.use("TkAgg")

from matplotlib import pyplot



# prepare data

labels = ["iOs", "Android", "Web", "React Native"]
values = [15, 15, 40, 30]
colors = ["blue", "yellow", "grey", "pink"]
explode = [0, 0, 0, 0.2]

# plot

pyplot.pie(values, 
colors=colors, 
labels=labels,
explode=explode
)
pyplot.axis("equal")

# show

pyplot.show()


