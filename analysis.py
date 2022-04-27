import time


def timeToUnix(timeobj):
    time_tuple = time.strptime(timeobj, '%Y-%m-%d %H:%M:%S')
    unix_time = time.mktime(time_tuple)

    return unix_time


keylog = open("keylog.txt", "r")
lastLine = ""
lastUnixTime = 0
for line in keylog:
    splitLine = line.split(" - ")
    splitLine[0] = splitLine[0].strip()
    splitLine[1] = splitLine[1].strip()
    timeobj = splitLine[0].split(",")[0]
    unixTime = timeToUnix(timeobj)
    if lastLine is not None:
        timeDiff = unixTime - lastUnixTime
        print(timeDiff)
        if timeDiff > 1800:
            f = open("newlog.txt", "a")
            f.write("********************")
            f.write("\n")
            f.close()
    f = open("newlog.txt", "a")
    f.write(line)
    f.close()
    lastLine = line
    lastUnixTime = unixTime
