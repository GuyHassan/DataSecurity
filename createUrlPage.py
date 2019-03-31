import bs4 as bs
import urllib.request

# to know if there was an error
class createUrlPage:
    def __init__(self):
      self.err = 0
      self.tempList = []
    def geturl(self):
        ### i will use a while loop until templist is not empty and every time
        ### i will pop the first link and go into, i will put the data again in sauce and soup
        ### then i will try to manage it with a global variable to check that i dont go deep to much
        try:
            sauce = urllib.request.urlopen('https://www.mako.co.il').read()
            soup = bs.BeautifulSoup(sauce, 'lxml')
        except:
            print("cant connect to this url")
            err = 1

        if self.err == 0:
            for url in soup.find_all('a'):
                if (url.get('href') is not None):
                    if 'https' in url.get('href'):  # filter to only links
                        self.tempList.append(url.get('href'))

    def printURL(self):
        print(self.tempList[0])
        print(self.tempList[1])
        print(self.tempList[2])
        print(self.tempList[3])




UrlPage = createUrlPage()
UrlPage.geturl()
UrlPage.printURL()














