import bs4 as bs
import urllib.request


class SearchSecurityCourse:
    def __init__(self):
        self.source = None
        self.soup = None
        self.listPass = []
        '''open file to write and push inside only the line that include the sequence username ... password'''
        self.optionUser = ['username:', 'user id:', 'user name:', 'userid:', 'user:']
        self.optionPass = ['password', 'password :', 'password: ', 'password-', 'password - ', 'password = ']

    def setLinkSite(self, linkSite):
        self.source = urllib.request.urlopen(linkSite).read()
        self.soup = bs.BeautifulSoup(self.source, 'lxml')
        self.insertTextToFile()
        self.tookWordFromTxtFile()
        return self.listPass

    def insertTextToFile(self):
        file_object = open('securityText.txt', 'w')
        for url in self.soup.find_all():
            if (('Username' or 'username') and ('password' or 'Password') in url.get_text()):
                file_object.write(url.get_text(separator=' '))  # separator add space after tag
        file_object.close()

    def tookWordFromTxtFile(self):
        self.listPass = []
        with open('securityText.txt') as f:
            credentials = [x.strip().split(' ') for x in f.readlines()]
        for i in range(len(credentials)):
            for j in range(len(credentials[i])):
                if (credentials[i][j].lower() in self.optionUser):
                    self.listPass.append(
                        {'username': credentials[i][j + 1], 'password': credentials[i][j + 3]})
        for text in self.listPass:
            print(text)


#
#
link = 'https://www.a1securitycameras.com/technical-support/default-username-passwords-ip-addresses-for-surveillance-cameras/'
link2 = 'https://ipvm.com/reports/ip-cameras-default-passwords-directory'
newSearch = SearchSecurityCourse()
newSearch.setLinkSite(link2)
