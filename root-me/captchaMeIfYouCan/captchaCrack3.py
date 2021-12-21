import bs4 as BeautifulSoup
import base64, sys, os, requests

# No cookies to configure :D (but need to be logged in root-me.org)

while(1):
    s = requests.Session()
    html = s.get('http://challenge01.root-me.org/programmation/ch8/')
    
    soup = BeautifulSoup.BeautifulSoup(html.text)

    img = soup.find_all('img')
    pngBin = str(img).split(',')[1]
    pngBin = base64.b64decode(pngBin[:-4])

    imgfile = open('./test.png', 'wb+')
    imgfile.write(pngBin)

    os.system('gocr -i ./test.png > res.txt')
    f = open('./res.txt')
    res = f.read()

    payload = {'cametu': str(res)[:-1]}

    d = s.post('http://challenge01.root-me.org/programmation/ch8/', data=payload)

    soup = BeautifulSoup.BeautifulSoup(d.text)
    t = soup.find_all('p')

    cnt = d.text.count("retente ta chance")

    if cnt == 0:
        print(d.text)
        break
    
for file in os.listdir('.'):
    if file.endswith(('.png','.txt')):
        os.remove(file)