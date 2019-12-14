import eel
import json
from createUrlPage import createUrlPage
from SQLiteClass import MySQLiteDB

url = "https://www.a1securitycameras.com/technical-support/default-username-passwords-ip-addresses-for-surveillance-cameras/"

eel.init('webFolder')


@eel.expose  # Expose this function to Javascript
def getLinkFromSite(urlAddress):
    sites = createUrlPage()
    DataFromSites = sites.GoDeep(str(urlAddress), 1)
    global db_string
    newDB = MySQLiteDB()
    if (DataFromSites != None):
        for line in DataFromSites:
            if ('dib' not in line['Model'] and 'dib' not in line['Username'] and 'dib' not in line['Password']):
                newDB.insertIntoDefaultUsers(line['Model'], line['Username'], line['Password'])
    db_string = newDB.printDefaultUsers()
    data = {}
    for i in range(len(db_string)):
        data[i + 1] = []
        data[i + 1].append({
                'Model': db_string[i][0],
                'Username': db_string[i][1],
                'Password': db_string[i][2]
            })
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
    return db_string


# eel.start('FinalProject.html', size=(1300, 700))  # Start
eel.start('FinalProject.html', size=(1300, 700), mode='chrome-app', port=8080,
          cmdline_args=['--start-fullscreen', '--browser-startup-dialog']).Default: []
