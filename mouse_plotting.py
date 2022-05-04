# libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

f = open("analysed_mouse_stuff.txt", "r")
for line in f:
    if "clicksX" in line:
        clicksX = line.lstrip("clicksX = [")
        clicksX = clicksX.rstrip("]\n")
        clicksX = clicksX.split(", ")
    if "clicksY" in line:
        clicksY = line.lstrip("clicksY = [")
        clicksY = clicksY.rstrip("]\n")
        clicksY = clicksY.split(", ")
    if "moveX" in line:
        moveX = line.lstrip("moveX = [")
        moveX = moveX.rstrip("]\n")
        moveX = moveX.split(", ")
    if "moveY" in line:
        moveY = line.lstrip("moveY = [")
        moveY = moveY.rstrip("]\n")
        moveY = moveY.split(", ")
    if "scrollX" in line:
        scrollX = line.lstrip("scrollX = [")
        scrollX = scrollX.rstrip("]\n")
        scrollX = scrollX.split(", ")
    if "scrollY" in line:
        scrollY = line.lstrip("scrollY = [")
        scrollY = scrollY.rstrip("]\n")
        scrollY = scrollY.split(", ")
    if "scrollDir" in line:
        scrollDir = line.lstrip("scrollDir = [")
        scrollDir = scrollDir.rstrip("]\n")
        scrollDir = scrollDir.split(", ")
    if "startTime" in line:
        startTime = line.strip("startTime = ")
    if "endTime" in line:
        endTime = line.strip("endTime = ")

print(len(moveX))
print("clicksX = [" + ", ".join(clicksX) + "]")


x1 = moveX
y1 = moveY
x2 = clicksX
y2 = clicksY
x3 = scrollX
y3 = scrollY

fig = plt.figure()
ax1 = fig.add_subplot(111)

plt.title('Mouse Events', loc='left')
ax1.scatter(x1, y1, s=2, c='#7AD7F0', marker='o', label='movements')
ax1.scatter(x2, y2, s=10, c='r', marker="o", label='clicks')
ax1.scatter(x3, y3, s=10, c="#357A38", marker="o", label='scrolls')
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
plt.legend(loc='upper left')
plt.show()

