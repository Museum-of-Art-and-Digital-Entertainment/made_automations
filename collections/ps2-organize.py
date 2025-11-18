# Author: David Chidester
# Email: davidchidester@themade.org

# script to move PS2 roms to a folder structure that the PS2 OPL can boot from
# copy PS2 library from NAS to the SMB server and run script to reformat the file tree
# requires python >= 3.10

import os
import logging

logger = logging.getLogger()

def main():
    alphabet = list(chr(x) for x in range(65, 91))
    for letter in alphabet:
        gameList = os.listdir(letter)
        for game in gameList:
            fileList = os.listdir(f"{letter}/{game}")
            for file in fileList:
                try:
                    move_game(game, file, f"{letter}/{game}")
                except Exception as e:
                    logger.error(f"Unable to transfer {game}")
    print("done")

def move_game(title: str, fname: str, path: str):
    extension = fname.split(".")[-1].lower()
    dest = ""
    match extension:
        case "bin":
            dest = "CD"
        case "cue":
            dest = "CD"
        case "iso":
            dest = "DVD"
        case _:
            logger.error(f"{fname} has an invalid file extension")
    logger.info(f"moving {fname}")
    os.rename(f"{path}/{fname}", f"{dest}/{title}.{extension}")

main()
