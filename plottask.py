# Explanation: A program that takes a range and creates a plot based on three separate functions iterating through those ranges.

# Task: Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

# Sources: I was able to complete the bulk of this task using the lecture slides and the accompanying further reading material. I did some extra research 
# into more advanced styling options, namely:
#    - W3Schools' material on Matplotlib markers, lines, grids and labels
#    - The NumPy documentation for that library's append function, which I ultimately couldn't get to work.
# All links are contained in the README.

# Working Notes: The actual logic of this was quite simple, I knew I needed to loop through a range and produce three separate arrays. I initially tried
# to use a NumPy array, but this doesn't seem to work with the standard append command. I researched the NumPy append command, which produces a new 
# array for reasons that I don't yet understand, and then experimented with the insert and concatenate commands from the same library, all of which I 
# could only generate more errors. Instead I changed each array back to a standard list and used the original append command. After that it was a matter 
# of experimenting with various line, grid, label and marker styles.

import matplotlib.pyplot as plt

range = [0,1,2,3,4]

# one range each for the three arrays required
xpoints = []
ypoints = []
zpoints = []

# loops through range and adds the result of each operation to a separate array
for i in range:
    normal = i
    square = i*i
    cubed = i*i*i
    xpoints.append(normal)
    ypoints.append(square)
    zpoints.append(cubed)

# ls indicates the line style, with - representing a solid (default) line, : a dotted line, and -- a dashed line.
# 
plt.plot(xpoints,label="Original Values", color="DodgerBlue", ls="-", marker="o")
plt.plot(ypoints,label="Squared Values", color="GoldenRod", ls="-.", marker="D")
plt.plot(zpoints,label="Cubed Values", color="FireBrick", ls="--", marker="^")

# the fontdict parameter allows for the setting of uniform or divergent font properties across different elements

titlefont = {"family":"sans-serif","color":"FireBrick","size": 14}
labelfont = {"family":"sans-serif","color":"FireBrick","size": 10}

plt.grid(color="NavajoWhite",linestyle=":")
plt.legend(edgecolor="FireBrick",borderpad=1,facecolor="FloralWhite")
plt.title("The Integers 0 to 4, Powered by 1, 2 and 3",fontdict=titlefont)
plt.xlabel("Integer Value",fontdict=labelfont)
plt.ylabel("Powered Value",fontdict=labelfont)

plt.savefig("plot.png")