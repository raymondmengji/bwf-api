import requests
import bs4
from bs4 import BeautifulSoup


class Player:
    def __init__(self, rank, country, name, ranking_change, record, earnings, points):
        self.rank = rank
        self.country = country
        self.name = name
        self.ranking_change = ranking_change
        winloss = list(record.split("-"))
        self.win = int(winloss[0])
        self.loss = int(winloss[1])
        self.earnings = earnings
        pointstmnts = list(points.split("/"))
        self.points = pointstmnts[0]
        self.tmntsPlayed = pointstmnts[1]
    def __str__(self):
        return str(self.__dict__)

if __name__ == "__main__":

    page = requests.get('https://bwfbadminton.com/rankings/2/bwf-world-rankings/6/men-s-singles/2020/12/?rows=25&page_no=1')

    soup = BeautifulSoup(page.content, 'html.parser')

    class_to_ignore = ["tr-ranking-detail"]

    l = soup.find_all("tr", class_=lambda x: x not in class_to_ignore)
    l.pop(0)

    playerList = []

    for player in l:
        tags = [t for t in list(player.children) if type(t) == bs4.element.Tag]
        rank = list(tags[0].children)[0]

        country = list(list(list(tags[1].children)[1].children)[1].children)[0]
        country = country[country.find('\t')+1 : country.find('\t')+4]

        name = list(list(tags[2].children)[1].children)
        name.pop(0)
        name.pop(len(name) - 1)

        if len(name) > 1:
            name1 = list(list(name[0].children)[1].children)[0]
            name2 = list(list(name[2].children)[1].children)[0]
            name = name1 + "," + name2
        else:
            name = ' '.join(list(list(name[0].children)[1].children)[0].split())

        ranking_change = list(tags[3].children)
        ranking_num = int(list(ranking_change[1].children)[0])
        if ranking_num != 0:
            posneg = str(ranking_change[3])
            index = posneg.find('arrow-up.png')
            if index == -1:
                ranking_num *= -1

        record = ''.join(list(tags[4].children)[0].split())

        earnings = str(list(tags[5].children)[0])

        points = ''.join(list(list(tags[6].children)[1].children)[0].split())
        playerList.append(Player(rank, country, name, ranking_num, record, earnings, points))
    for p in playerList:
        print(p)
    












