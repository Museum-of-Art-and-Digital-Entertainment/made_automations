#╭──────────────────────────────────────────────╮
#│ Myrient Download Script                      │
#│ Author: David Chidester                      │
#│ Email: davidchidester@themade.org            │
#╰──────────────────────────────────────────────╯

import requests
import logging
from concurrent.futures import ThreadPoolExecutor
from urllib import parse
from bs4 import BeautifulSoup

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger()

class Game:
    def __init__(self, gameTitle: str, url: str, downloadPath: str):
        self.title = gameTitle
        self.link = url
        self.path = downloadPath

def get_game_list(url: str) -> [Game]:
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    gameLinks = soup.find(id="list").find_all("a")
    gameList = []
    for elem in gameLinks:
        link = elem.attrs["href"]
        if "zip" in link:
            gameList.append(link)
    return gameList

def download(game: Game):
    fname = parse.unquote(game.title)
    logger.info(f"downloading {fname}")
    try:
        res = requests.get(game.link)
        if res.status_code != 200:
            logger.error(f"{fname} download failed, http status {res.status_code}")
            exit(1)
        fptr = open(f"{game.path}/{fname}", "wb")
        fptr.write(res.content)
        fptr.close()
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    libs = [
            "Microsoft%20-%20Xbox%20360%20(Digital)",
            "Nintendo%20-%20Nintendo%20DSi%20%28Digital%29/",
            "Nintendo%20-%20Wii%20%28Digital%29%20%28CDN%29",
            "Nintendo%20-%20Wii%20U%20%28Digital%29%20%28CDN%29",
            "Sony%20-%20PlayStation%203%20%28PSN%29%20%28Content%29",
            "Sony%20-%20PlayStation%203%20%28PSN%29%20%28DLC%29",
            "Sony%20-%20PlayStation%203%20%28PSN%29%20%28Updates%29"
            ]

    print("Which library would you like to Download?")
    for i in range(len(libs)):
        print(f"{i+1} {parse.unquote(libs[i])}")
    choice = int(input().strip()) - 1
    assert choice in range(len(libs)), "invalid choice"
    downloadPath = input("Enter download path (leave black for current directory): ") or "."
    domain = "https://myrient.erista.me"
    library = f"{domain}/files/No-Intro/{libs[choice]}"
    links = get_game_list(library)
    gameList = []
    for game in links:
        gameList.append(Game(game, f"{library}{game}", downloadPath))
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(download, gameList)

