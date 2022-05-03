import os
from time import time
from datetime import datetime, timedelta
from time import mktime as mktime
from tkinter import *
from mttkinter import mtTkinter as tk

# from PIL import Image,ImageTk ... pip install pillow

root = Tk()
root.geometry('200x200')
root.title("Assistant")
root.configure(bg="#FEC5E5")
starting_text = "HIII!!"
good_text = 'You\'re doing great :)'
bad_text = 'Back to work!'
game_text = 'Are ya gaming son?'
timeout = 120


def exitt():
    exit()


def timeToUnix(timeobj):
    time_tuple = datetime.strptime(timeobj, '%Y-%m-%d %H:%M:%S').timetuple() \
        # print(time_tuple)
    unix_time = mktime(time_tuple)
    return unix_time


def update_label(time_diff, numKeys, allKeys, keyFrequencies):
    if numKeys != 0:
        print("HOW MANY DIF KEYS?!?? " + str(len(allKeys)))
        if (time_diff < timeout) and len(allKeys) > 20:   # has typed within last 2 mins & more than 20 dif chars
            msg = good_text
        elif numKeys > 300 and len(allKeys) < 20:         # more than 300 chars, less than 20 dif chars. probably gamin
            msg = game_text
        elif time_diff > timeout or (time_diff > 60 and numKeys < 30):  # hasn't typed in 2 mins, or hasn't typed in one
            msg = bad_text                                              # min and only doing 30 chars/min
        else:
            msg = bad_text
    else:
        msg = bad_text
    global label
    label["text"] = msg


def no_activity_update():
    global label
    label["text"] = bad_text


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def getTimeObj(line):
    line_time = line.strip()
    line_time = line_time.rstrip('\n')
    everything = line_time.split(" - ")
    timeobj_string = everything[0].split(",")[0]
    time_obj = datetime.strptime(timeobj_string, '%Y-%m-%d %H:%M:%S')
    # print(time_obj)
    return time_obj


def getKeyPressed(line):
    line_time = line.strip()
    line_time = line_time.rstrip('\n')
    everything = line_time.split(" - ")
    key = everything[1].strip("'")
    print(key)
    return key


def key_calculations(*args):
    filesize = os.path.getsize("keylog.txt")

    if filesize != 0:
        with open("keylog.txt") as f:
            for line in f:
                pass
            last_line = line
        # some messy code that snips apart the time objects so I can get unix time
        last = last_line.strip()
        last = last.rstrip('\n')
        everything = last.split(" - ")
        timeobj_string = everything[0].split(",")[0]
        key_time_epoch = timeToUnix(timeobj_string)
        # print(timeobj_string)
        print("LAST KEY TIME " + str(key_time_epoch))
        timeNow = datetime.now()
        now_time_epoch = timeToUnix(datetime.strftime(timeNow, '%Y-%m-%d %H:%M:%S'))
        print("NOW TIME " + str(now_time_epoch))
        time_diff = now_time_epoch - key_time_epoch
        if time_diff < 600:  # if last keypress was within 5 mins....
            # print(timeNow)  # do something
            file = open('analysis_file.txt', 'a')
            numKeys = 0
            allKeys = []
            keyFrequencies = []
            start_range_time = timeNow - timedelta(minutes=5)
            print(start_range_time)
            last_time_obj = datetime.strptime(timeobj_string, '%Y-%m-%d %H:%M:%S')
            # print(last_time_obj < timeNow)
            textfile = open("keylog.txt")
            lines = textfile.readlines()
            found = False
            for line in reversed(lines):
                line_time_obj = getTimeObj(line)
                if timeNow > line_time_obj > start_range_time:
                    key = getKeyPressed(line)
                    print(datetime.strftime(line_time_obj, '%Y-%m-%d %H:%M:%S') + " at " + key)
                    numKeys += 1
                    for idx, x in enumerate(allKeys):
                        print("x = " + x)
                        print("key = " + key)
                        if x == key:
                            keyFrequencies[idx] += 1
                            found = True
                    if not found:
                        allKeys.append(key)
                        keyFrequencies.append(1)
                found = False
            keysString = str(allKeys)
            freqString = str(keyFrequencies)
            fullString = datetime.strftime(timeNow, '%Y-%m-%d %H:%M:%S') + "\nKeys pressed: "
            fullString += str(numKeys) + "\nAll Keys: " + keysString + "\nKey Frequencies:" + freqString
            fullString += "\n**************\n"
            print(fullString)
            file.write(fullString)
            file.close()
            textfile.close()
            update_label(time_diff, numKeys, allKeys, keyFrequencies)  # HERE IS WHERE WE UPDATE!
        else:
            print("avg keys: 0")
            no_activity_update()

        print("time diff = " + str(time_diff) + " seconds")
    else:
        print("The file is empty")
    pass


def loop_func(root):
    print("Hi")
    # root.after(5000, lambda: key_calculations())
    key_calculations()
    root.after(5000, lambda: loop_func(root))


label = Label(root, text=starting_text, bg="#F699CD", relief="solid", width=18, font=("arial", 10, "bold"))

label.place(x=24, y=40)

but_qui = Button(root, text="Quit", width=12, bg="#821432", fg="white", command=exitt).place(x=55, y=80)
root.update()

root.after(5000, loop_func(root))
root.mainloop()
