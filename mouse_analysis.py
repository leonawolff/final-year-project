keylog = open("mouse_data_file.txt", "r")
lastLine = ""
clicksX = []
clicksY = []
moveX = []
moveY = []
scrollX = []
scrollY = []
scrollDir = []
startTime = ""
endTime = ""

"2022-05-04 01:43:29,820: Mouse moved to (1431, 218)"
"2022-05-04 01:53:29,273: Mouse clicked at (-1014, 11) with Button.left"
"2022-05-04 01:53:02,865: Mouse scrolled at (-1151, 543)(0, -1)"


def get_x_coord(s):
    try:
        return s[s.index("(") + len("("):s.index(",")]
    except ValueError:
        return ""


def get_y_coord(s):
    try:
        return s[s.index(",") + len(", "):s.index(")")]
    except ValueError:
        return ""


def do_scroll_stuff(s):
    try:
        coords = s[s.index("at (") + len("at ("):s.index(")(0,")]
        coords = coords.split(", ")
        scrollX.append(coords[0].strip())
        scrollY.append(coords[1].strip())
        direction = s[s.index(")(0, ") + len(")(0, "):s.index(")")]
        scrollDir.append(direction.strip())  # -1 = scroll up, 1 = scroll down
        return 1
    except ValueError:
        return -1


for line in keylog:
    if lastLine is not None:
        splitLine = line.split(" Mouse ")
        if startTime is "":
            splitLine[0] = splitLine[0].strip()
            splitLine[0] = splitLine[0].rstrip(":")
            startTime = splitLine[0]
        splitLine[1] = splitLine[1].strip()
        if "moved" in splitLine[1]:
            moveX.append(get_x_coord(splitLine[1]))
            moveY.append(get_y_coord(splitLine[1]))
        if "click" in splitLine[1]:
            clicksX.append(get_x_coord(splitLine[1]))
            clicksY.append(get_y_coord(splitLine[1]))
        if "scroll" in splitLine[1]:
            do_scroll_stuff(splitLine[1])

print("clicksX = [" + ", ".join(clicksX) + "]")
print("clicksY = [" + ", ".join(clicksY) + "]")
print("moveX = [" + ", ".join(moveX) + "]")
print("moveY = [" + ", ".join(moveY) + "]")
print("scrollX = [" + ", ".join(scrollX) + "]")
print("scrollY = [" + ", ".join(scrollY) + "]")
print("scrollDir = [" + ", ".join(scrollDir) + "]")
print("startTime = " + startTime)

f = open("analysed_mouse_stuff.txt", "a")
f.write("clicksX = [" + ", ".join(clicksX) + "]\n")
f.write("clicksY = [" + ", ".join(clicksY) + "]\n")
f.write("moveX = [" + ", ".join(moveX) + "]\n")
f.write("moveY = [" + ", ".join(moveY) + "]\n")
f.write("scrollX = [" + ", ".join(scrollX) + "]\n")
f.write("scrollY = [" + ", ".join(scrollY) + "]\n")
f.write("scrollDir = [" + ", ".join(scrollDir) + "]\n")
f.write("startTime = " + startTime)
f.write("\n")
f.close()
