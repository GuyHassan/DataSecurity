import bs4 as bs
import urllib.request

source = urllib.request.urlopen(
    # 'http://www.phenoelit.org/dpl/dpl.html'
    'https://www.a1securitycameras.com/technical-support/default-username-passwords-ip-addresses-for-surveillance-cameras/'
).read()
soup = bs.BeautifulSoup(source, 'lxml')

'''open file to write and push inside only the line that include the sequence username ... password'''
optionUser = ['username:', 'user id:', 'user name:', 'userid:', 'user:']
optionPass = ['password', 'password :', 'password: ', 'password-', 'password - ', 'password = ']

file_object = open('guyText.txt', 'w')

for url in soup.find_all('p'):
    if (('password' or 'Password') and ('Username' or 'username') in url.get_text()):
        file_object.write(url.get_text(separator=' '))  # separator add space after tag

file_object.close()
listPass = []

with open('guyText.txt') as f:
    credentials = [x.strip().split(' ') for x in f.readlines()]

for i in range(len(credentials)):
    for j in range(len(credentials[i])):

        if (credentials[i][j].lower() in optionUser):
            listPass.append({credentials[i][j]: credentials[i][j + 1], credentials[i][j + 2]: credentials[i][j + 3]})
for text in listPass:
    print(text)
