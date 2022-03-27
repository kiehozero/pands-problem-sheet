# Explanation: A program that takes a range and creates a plot based on three separate functions iterating through those ranges.

# Task: Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

# Sources: I was able to complete the bulk of this task using the lecture slides and the accompanying further reading material. I did some extra research 
# into more advanced styling options, namely:
#    - W3Schools' material on Matplotlib markers, lines and labels
#    - The NumPy documentation for that library's append function.
# All links are contained in the README.

# Working Notes: 

import matplotlib.pyplot as plt

range = [0,1,2,3,4]

# one range each for the three arrays required
xpoints = []
ypoints = []
zpoints = []

# loops through range and adds the result of each operation to a separate array
for i in range:
    xpoints.append(i)
    ypoints.append(i*i)
    zpoints.append(i*i*i)

# ls indicates the line style, with - representing a solid (default) line, : a dotted line, and -- a dashed line.
plt.plot(xpoints,label="function: f(x)=x", color="blue", ls="-", marker="^")
plt.plot(ypoints,label="function: g(x)=x*x", color="red", ls=":", marker="x")
plt.plot(zpoints,label="function: h(x)=x*x*x", ls="--", color="green", marker="D")
plt.legend()

plt.show()