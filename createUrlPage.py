import bs4 as bs
import urllib.request
import testingNew

# to know if there was an error
class createUrlPage:
    def __init__(self):
        self.err = 0

    def geturl(self, url):
        ### i will use a while loop until templist is not empty and every time
        ### i will pop the first link and go into, i will put the data again in sauce and soup
        ### then i will try to manage it with a global variable to check that i dont go deep to much
        try:
            sauce = urllib.request.urlopen(url).read()
            soup = bs.BeautifulSoup(sauce, 'lxml')
        except:
            print("cant connect to this url")
            err = 1
            return -1
        urls = []
        if self.err == 0:
            for url in soup.find_all('a'):
                if (url.get('href') is not None):
                    if 'https' in url.get('href'):  # filter to only links
                        urls.append(url.get('href'))
        return urls


    def GoDeep(self, url, depth):
        if depth == 0:
            return
        ssc = testingNew.SearchSecurityCourse()
        print(url)
        default = ssc.setLinkSite(url)
        urls = self.geturl(url)
        urls = urls[:5]
        for currUrl in urls:
            print(currUrl)
            default.append(self.GoDeep(str(currUrl), depth - 1))
        return default


cup = createUrlPage()
print(cup.GoDeep("https://www.a1securitycameras.com/technical-support/default-username-passwords-ip-addresses-for-surveillance-cameras/", 3))