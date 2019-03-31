import bs4 as bs
import urllib.request
from SQLiteClass import MySQLiteDB
from projectSecurity import SearchSecurityCourse


ssc = SearchSecurityCourse()

newDB = MySQLiteDB()
link = 'https://www.a1securitycameras.com/technical-support/default-username-passwords-ip-addresses-for-surveillance-cameras/'
dict = ssc.setLinkSite(link)

for text in dict:
    newDB.insertIntoDefaultUsers('None', text['username'], text['password'])


newDB.printDefaultUsers()
newDB.clearDefaultUsers()