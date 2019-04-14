import bs4 as bs
import urllib.request


class SearchSecurityCourse:
    def __init__(self):
        self.source = None
        self.soup = None
        self.listTextFree = []
        self.listTables = []
        ''' A lists that holds different types of writing '''
        self.optionUser = ['username:', 'user id:', 'user name:', 'User name:', 'User name', 'userid:', 'user:',
                           'Username', 'Username:', 'User', 'User:', 'Username-', 'USERNAME', 'USERNAME:', 'user',
                           'login', 'login:', 'Login', 'Login:', 'Default User Name', 'Default Username',
                           'Default user name', 'Default username is']
        self.optionPass = ['password', 'password :', 'password:', 'password-', 'password - ', 'password = ',
                           'Password', 'Password:', 'Password-', 'Pass', 'Pass-', 'PASSWORD', 'PASSWORD:',
                           'Default Password', 'default password', 'Default password', 'Default password is', 'passwrd']
        self.optionModel = ['Bosch', 'Samsung', 'Axis', '3xLogic', 'Canon', 'Cisco', 'JVC', 'TP-Link', 'TP-LINK',
                            'Panasonic', 'Sony', 'Veriant', 'Netgear', 'HP', 'Asus', 'Google', 'NIHON', 'ACTi',
                            'Motorola', 'Foscam', 'Pelco', 'Toshiba', 'LTS Security', 'Apple', 'GeoVision', 'Microsoft',
                            'Nexus', 'Alcatel', 'LG', 'Huawei', 'Gigabyte', '3COM']

    '''set a link inside a beautiful soup feature and he give us the tags inside the site'''

    def setLinkSite(self, linkSite):
        self.source = urllib.request.urlopen(linkSite).read()
        self.soup = bs.BeautifulSoup(self.source, 'lxml')
        self.getUser_PassFromTable()
        self.getUser_PassFromFreeText()

        return self.listTables + self.listTextFree

    '''create a list with all the tags that include username and password and we filter the relevant data for us '''

    def getUser_PassFromFreeText(self):
        for url in self.soup.find_all({'p', 'code', 'h3', 'h4', 'h5', 'h6', 'div', 'blockquote'}):
            '''we append to this list each line in the table , and we filter the trash word from the beautiful soup libary like : \n \r \t etc...'''
            ls = list(filter(lambda s: s != ' ', list(map(lambda s: s.strip(), url.get_text(separator=' ').split()))))
            for i in range(len(ls)):
                if ((ls[i] in self.optionUser) and (i + 2 < len(ls))):
                    if ((ls[i + 2] in self.optionPass) and (i + 3 < len(ls))):
                        if ({'Model': 'None', 'Username': ls[i + 1], 'Password': ls[i + 3]} not in self.listTextFree):
                            self.listTextFree.append({'Model': 'None', 'Username': ls[i + 1], 'Password': ls[i + 3]})

    '''create a list with all the table that include username and password and we filter the relevant data for us from the table '''

    def getUser_PassFromTable(self):
        listTmp = []
        for url in self.soup.find_all('tr'):
            '''we append to this list each line in the table , and we filter the trash word from the beautiful soup libary like : \n \r \t etc...'''
            ls = list(map(lambda s: s.strip(), url.get_text().split('\n')))
            listTmp.append(ls)
            '''this condition check if the first line on table is contain username and password , if not, this is not table for us'''
            if ((len(listTmp) == 1) and
                    not (any(elem in self.optionUser for elem in listTmp[0]) and
                         any(elem in self.optionPass for elem in listTmp[0]))):
                listTmp.remove(ls)
            '''get index from my list to filter the table to what relevant for us (model,username,password...)'''
        if(listTmp != []):
            indexModel = None
            indexUser = listTmp[0].index([i for i in listTmp[0] if i in self.optionUser][0])
            indexPass = listTmp[0].index([i for i in listTmp[0] if i in self.optionPass][0])
            for miniList in listTmp:
                '''return the type if is exist inside the table'''
                tmpItem = [j for j in miniList if j in self.optionModel]
                '''if the type is exist i get the index where the "Model" is inside the list'''
                if (tmpItem != []):
                    indexModel = miniList.index(tmpItem[0])
                    break
            '''remove the first line from the table(we dont need that after we filter the list)'''
            listTmp.pop(0)
        '''append to the list the model username and password from the list after filtering'''
        for miniList in listTmp:
            if (max(indexModel, indexUser, indexPass) < len(miniList)):
                self.listTables.append(
                    {'Model': miniList[indexModel], 'Username': miniList[indexUser], 'Password': miniList[indexPass]})



