import pickle
import datetime
import os


first_time = True
if os.path.isfile("last_run.pkl"):
    pickle_file = open("last_run.pkl")
try:
    file = open("somefile.txt", "r")
except:
    print "Couldn't open the file. Do you want to try again ?"