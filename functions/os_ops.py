import os
import subprocess as sp

paths = {
    "SublimeText": "C:\\Program Files\\Sublime Text\\sublime_text.exe",
    "calculator": "C:\\Windows\\System32\\calc.exe",
    "google_chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "brave": "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
}


# Open the camera
def open_camera():
    sp.run('start microsoft.windows camera:', shell=True)


# Open the paths in the system
def open_sublime_text():
    os.startfile(paths['SublimeText'])


def open_calc():
    os.startfile(paths['calculator'])


def open_google():
    os.startfile(paths['google_chrome'])


def open_brave():
    os.startfile(paths['brave'])


def open_cmd():
    os.system("start cmd")