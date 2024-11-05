import os
import hashlib
import threading

def createHashList(path="."):
    files = list(filter(os.path.isfile, os.listdir(path)))
    for file in files:
        thrd = threading.Thread(target=md5sum, args=[file])
        thrd.start()

def md5sum(fname):
    fptr = open(fname, "rb").read()
    md5sum = hashlib.md5(fptr).hexdigest()
    print(f"{fname}, {md5sum}")

createHashList()
