import bs4 as bs
import urllib.request


class SearchSecurityCourse:
    def __init__(self):
        self.source = None
        self.soup = None
        self.TableWithoutEmptyIndex = []
        self.listPass = []
        '''open file to write and push inside only the line that include the sequence username ... password'''
        self.optionUser = ['username:', 'user id:', 'user name:', 'userid:', 'user:', 'Username', 'Username:', 'User',
                           'Username-', 'USERNAME']
        self.optionPass = ['password', 'password :', 'password: ', 'password-', 'password - ', 'password = ',
                           'Password', 'Password:', 'Password-', 'Pass', 'Pass-', 'PASSWORD']

    def setLinkSite(self, linkSite):
        self.source = urllib.request.urlopen(linkSite).read()
        self.soup = bs.BeautifulSoup(self.source, 'lxml')
        self.insertTextToFile()
        # self.tookWordFromTxtFile()
        # return self.listPass

    def insertTextToFile(self):
        for url in self.soup.find_all('tr'):
            '''we append to this list each line in the table , and we filter the trash word from the beautiful soup libary like : \n \r \t etc...'''
            self.TableWithoutEmptyIndex.append(
                list(filter(lambda s: s != '', list(map(lambda s: s.strip(), url.get_text().split('\n'))))))
            '''this condition check if the first line on table is contain username and password , if not, this is not table for us'''
            if ((len(self.TableWithoutEmptyIndex) == 1) and
                 not (any(elem in self.optionUser for elem in self.TableWithoutEmptyIndex[0]) and
                      any(elem in self.optionPass for elem in self.TableWithoutEmptyIndex[0]))):
                self.TableWithoutEmptyIndex = []
                print('Not Table for us')
                break
        for i in self.TableWithoutEmptyIndex:
            print(i)


link = 'http://www.phenoelit.org/dpl/dpl.html'
link2 = 'https://www.contextures.com/xlSampleData01.html'
newSearch = SearchSecurityCourse()
newSearch.setLinkSite(link)

# a = ['123', 're45']
# b = ['re45', '345345', 'sdf234']
# print((not any(elem in a for elem in b)))
