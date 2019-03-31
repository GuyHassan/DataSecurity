import bs4 as bs
import urllib.request


class SearchSecurityCourse:
    def __init__(self):
        self.source = None
        self.soup = None
        '''open file to write and push inside only the line that include the sequence username ... password'''
        self.optionUser = ['username:', 'user id:', 'user name:', 'userid:', 'user:']
        self.optionPass = ['password', 'password :', 'password: ', 'password-', 'password - ', 'password = ']

    def setLinkSite(self, linkSite):
        self.source = urllib.request.urlopen(linkSite).read()
        self.soup = bs.BeautifulSoup(self.source, 'lxml')
        self.insertTextToFile()
        self.tookWordFromTxtFile()

    def insertTextToFile(self):
        file_object = open('securityText.txt', 'w')
        for url in self.soup.find_all():
            if (('password' or 'Password') and ('Username' or 'username') in url.get_text()):
                file_object.write(url.get_text(separator=' '))  # separator add space after tag
        file_object.close()

    def tookWordFromTxtFile(self):
        listPass = []
        with open('securityText.txt') as f:
            credentials = [x.strip().split(' ') for x in f.readlines()]
        for i in range(len(credentials)):
            for j in range(len(credentials[i])):
                if (credentials[i][j].lower() in self.optionUser):
                    listPass.append(
                        {credentials[i][j]: credentials[i][j + 1], credentials[i][j + 2]: credentials[i][j + 3]})
        for text in listPass:
            print(text)


link = 'https://www.a1securitycameras.com/technical-support/default-username-passwords-ip-addresses-for-surveillance-cameras/'
newSearch = SearchSecurityCourse()
newSearch.setLinkSite(link)
