import bs4 as bs
import urllib.request
from SQLiteClass import MySQLiteDB
from testingNew import SearchSecurityCourse

listOfDataFromSite = []
objectSecurity = SearchSecurityCourse()

newDB = MySQLiteDB()
link = 'https://www.a1securitycameras.com/technical-support/default-username-passwords-ip-addresses-for-surveillance-cameras/'
link2 = 'http://www.phenoelit.org/dpl/dpl.html'
listOfDataFromSite.extend(objectSecurity.setLinkSite(link))
listOfDataFromSite.extend(objectSecurity.setLinkSite(link2))

for line in listOfDataFromSite:
    if ('dib' not in line['Model'] and 'dib' not in line['Username'] and 'dib' not in line['Password']):
        newDB.insertIntoDefaultUsers(line['Model'], line['Username'], line['Password'])

newDB.printDefaultUsers()
newDB.clearDefaultUsers()
