import os
import hashlib
import threading


def getPlatformByExtension(fname):
    extensionMap = {
        "a26": "Atari 2600",
        "nes": "NES",
        "snes": "SNES",
        "z64": "N64",
        "wbfs": "Wii",
        "gb": "GB",
        "gbc": "GBC",
        "gba": "GBA",
        "nds": "DS",
        "3ds": "3DS"
        }
    try:
        extension = (fname.split(".")[-1]).lower()
        if extension not in extensionMap:
            return ""
        return extensionMap[extension]
    except ValueError:
        print("unable to parse file extension")
        return ""


def createHashList(path="."):
    files = list(filter(os.path.isfile, os.listdir(path)))
    for file in files:
        thrd = threading.Thread(target=md5sum, args=[file])
        thrd.start()


def md5sum(fname):
    fptr = open(fname, "rb").read()
    md5sum = hashlib.md5(fptr).hexdigest()
    platform = getPlatformByExtension(fname)
    print(f"{fname}, {md5sum} {platform}")


createHashList()
