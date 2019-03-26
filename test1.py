import bs4 as bs
import urllib.request

source = urllib.request.urlopen(
    'http://www.phenoelit.org/dpl/dpl.html'
    # 'https://www.a1securitycameras.com/technical-support/default-username-passwords-ip-addresses-for-surveillance-cameras/'
).read()
soup = bs.BeautifulSoup(source, 'lxml')

'''open file to write and push inside only the line that include the sequence username ... password'''
optionUser = ['username:', 'user id:', 'user name:', 'userid:', 'user:']
optionPass = ['password', 'password :', 'password: ', 'password-', 'password - ', 'password = ']

file_object = open('guyText.txt', 'w')

for url in soup.find_all('table'):
    print(url)
    if (('password' or 'Password') and ('Username' or 'username') in url.get_text()):
        file_object.write(url.get_text(separator=' '))  # separator add space after tag
