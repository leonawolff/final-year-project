keylog = open("file.txt", "r")
lastLine = ""
lastUnixTime = 0
for line in keylog:
    if lastLine is not None or "********************":
        splitLine = line.split(" - ")
        splitLine[0] = splitLine[0].strip()
        splitLine[1] = splitLine[1].strip()
        f = open("league_log1.txt", "a")
        f.write(splitLine[0])
        f.write("\n")
        f.close()
        f = open("league_log2.txt", "a")
        f.write(splitLine[1])
        f.write("\n")
        f.close()
    if lastLine is "********************":
        f = open("league_log1.txt", "a")
        f.write("********************")
        f.write("\n")
        f.close()
        f = open("league_log2.txt", "a")
        f.write("********************")
        f.write("\n")
        f.close()
