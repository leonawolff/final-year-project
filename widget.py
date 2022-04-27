import os
from time import time
from datetime import datetime
from time import mktime as mktime
from tkinter import *
from mttkinter import mtTkinter as tk

# from PIL import Image,ImageTk ... pip install pillow

root = Tk()
root.geometry('200x200')
root.title("Assistant")
starting_text = "HIII!!"
good_text = 'You\'re doing great :)'
bad_text = 'Back to work!'
timeout = 30


def exitt():
    exit()


def timeToUnix(timeobj):
    time_tuple = datetime.strptime(timeobj, '%Y-%m-%d %H:%M:%S').timetuple() \
        # print(time_tuple)
    unix_time = mktime(time_tuple)
    return unix_time


def update_label(time_diff):
    if time_diff > timeout:
        msg = bad_text
    else:
        msg = good_text
    global label
    label["text"] = msg


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
        timeobj = everything[0].split(",")[0]
        key_time_epoch = timeToUnix(timeobj)
        print(timeobj)
        print("THEN TIME " + str(key_time_epoch))
        timeNow = datetime.now()
        now_time_epoch = timeToUnix(datetime.strftime(timeNow, '%Y-%m-%d %H:%M:%S'))
        print("NOW TIME " + str(now_time_epoch))
        time_diff = now_time_epoch - key_time_epoch
        update_label(time_diff)
        print("time diff = " + str(time_diff) + " seconds")
    else:
        print("The file is empty")
    pass


def loop_func(root):
    print("Hi")
    # root.after(5000, lambda: key_calculations())
    key_calculations()
    root.after(5000, lambda: loop_func(root))


label = Label(root, text=starting_text, relief="solid", width=18, font=("arial", 10, "bold"))

label.place(x=24, y=40)

but_qui = Button(root, text="Quit", width=12, bg="red", fg="white", command=exitt).place(x=55, y=80)

root.after(5000, loop_func(root))
root.mainloop()
