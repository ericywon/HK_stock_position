from bs4 import BeautifulSoup
import requests
import csv


def DIONlinks(url):
    data = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.find_all('a', href=True):
        if "List of all notices" in a.text:
            link = "https://di.hkex.com.hk/filing/di/" + a['href']
            data.append(link)
    return data


dionlinks = []
for i in range(1,10000):
    url = "https://di.hkex.com.hk/di/NSSrchCorpList.aspx?sa1=cl&scsd=01/01/1900&sced=11/09/2020&sc=" + str(i) + "&src=MAIN&lang=EN"
    indlink = []
    try:
        indlink += DIONlinks(url)
    except:
        print("Retrying!")
        n = 1
        while n<500:
            n += 1
            try:
                indlink += DIONlinks(url)
                break
            except Exception:  # Replace Exception with something more specific.
                continue
    if not indlink == []:
        for line in indlink:
            print(line)
            dionlinks.append([line])
print(dionlinks)

m=0
with open('DIONlinks.csv', 'w', newline='', encoding='utf-8') as csvfile:
    linewriter = csv.writer(csvfile, delimiter='@')
    for row in dionlinks:
        m += 1
        print("Write Row " + str(m))
        linewriter.writerow(row)


