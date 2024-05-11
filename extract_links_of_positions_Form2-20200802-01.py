from bs4 import BeautifulSoup
import requests
import csv



def form2(url):

    data = []
    data += [url]

    r = requests.get(url)
    soup = BeautifulSoup(r.content)

    FormSerialNo = soup.find('span', id="lblDLogNo").get_text()
    data += [FormSerialNo]

    Box1 = soup.find('span', id="lblViewCorpName").get_text()
    data += [Box1]

    Box2 = soup.find('span', id="lblDStockCode").get_text()
    data += [Box2]

    Box3 = soup.find('span', id="lblDClass").get_text()
    data += [Box3]

    Box4 = soup.find('span', id="lblDIssued").get_text()
    data += [Box4]

    Box5 = soup.find('span', id="lblDName").get_text()
    data += [Box5]

    Box6 = soup.find('span', id="lblDRegOffice").get_text()
    data += [Box6]

    Box7 = soup.find('span', id="lblDPrinPlace").get_text()
    data += [Box7]

    Box13 = soup.find('span', id="lblDExList").get_text()
    data += [Box13]

    Box14 = soup.find('span', id="lblDParent").get_text()
    data += [Box14]

    Box15 = soup.find('span', id="lblDEventDate").get_text()
    data += [Box15]

    Box16 = soup.find('span', id="lblDAwareDate").get_text()
    data += [Box16]

    Box17all = []
    Box17_position = soup.find('span', id="lblDEvtPosition").get_text()
    Box17all += [Box17_position]

    Box17_eventcode = soup.find('span', id="lblDEvtReason").get_text()
    Box17all += [Box17_eventcode]

    Box17_capbefore = soup.find('span', id="lblDEvtCapBefore").get_text()
    Box17all += [Box17_capbefore]

    Box17_capafter = soup.find('span', id="lblDEvtCapAfter").get_text()
    Box17all += [Box17_capafter]

    Box17_eventshare = soup.find('span', id="lblDEvtShare").get_text()
    Box17all += [Box17_eventshare]

    Box17_eventcurrency = soup.find('span', id="lblDEvtCurrency").get_text()
    Box17all += [Box17_eventcurrency]

    Box17_eventHprice = soup.find('span', id="lblDEvtHPrice").get_text()
    Box17all += [Box17_eventHprice]

    Box17_eventAprice = soup.find('span', id="lblDEvtAPrice").get_text()
    Box17all += [Box17_eventAprice]

    Box17_eventAconsider = soup.find('span', id="lblDEvtAConsider").get_text()
    Box17all += [Box17_eventAconsider]

    Box17_eventNATconsider = soup.find('span', id="lblDEvtNatConsider").get_text()
    Box17all += [Box17_eventNATconsider]

    Box17all2 = []
    try:
        Box17_position2 = soup.find('span', id="lblDEvtPosition2").get_text()
        Box17all2 += [Box17_position2]
    except:
        Box17all2 += [""]

    try:
        Box17_eventcode2 = soup.find('span', id="lblDEvtReason2").get_text()
        Box17all2 += [Box17_eventcode2]
    except:
        Box17all2 += [""]

    try:
        Box17_capbefore2 = soup.find('span', id="lblDEvtCapBefore2").get_text()
        Box17all2 += [Box17_capbefore2]
    except:
        Box17all2 += [""]

    try:
        Box17_capafter2 = soup.find('span', id="lblDEvtCapAfter2").get_text()
        Box17all2 += [Box17_capafter2]
    except:
        Box17all2 += [""]

    try:
        Box17_eventshare2 = soup.find('span', id="lblDEvtShare2").get_text()
        Box17all2 += [Box17_eventshare2]
    except:
        Box17all2 += [""]

    try:
        Box17_eventcurrency2 = soup.find('span', id="lblDEvtCurrency2").get_text()
        Box17all2 += [Box17_eventcurrency2]
    except:
        Box17all2 += [""]

    try:
        Box17_eventHprice2 = soup.find('span', id="lblDEvtHPrice2").get_text()
        Box17all2 += [Box17_eventHprice2]
    except:
        Box17all2 += [""]

    try:
        Box17_eventAprice2 = soup.find('span', id="lblDEvtAPrice2").get_text()
        Box17all2 += [Box17_eventAprice2]
    except:
        Box17all2 += [""]

    try:
        Box17_eventAconsider2 = soup.find('span', id="lblDEvtAConsider2").get_text()
        Box17all2 += [Box17_eventAconsider2]
    except:
        Box17all2 += [""]

    try:
        Box17_eventNATconsider2 = soup.find('span', id="lblDEvtNatConsider2").get_text()
        Box17all2 += [Box17_eventNATconsider2]
    except:
        Box17all2 += [""]

    data += [[Box17all, Box17all2]]




    Box18 = soup.find('table', id='grdSh_BEvt')
    Box18all = []
    rows = Box18.find_all('tr')[1:]
    for row in rows:
        temp = []
        for cell in row.find_all('td'):
            temp += [cell.text]
        Box18all += [temp]
    data += [Box18all]


    Box19 = soup.find('table', id='grdSh_AEvt')
    Box19all = []
    rows = Box19.find_all('tr')[1:]
    for row in rows:
        temp = []
        for cell in row.find_all('td'):
            temp += [cell.text]
        Box19all += [temp]
    data += [Box19all]


    Box20 = soup.find('table', id='grdCap_SS')
    Box20all = []
    rows = Box20.find_all('tr')[1:]
    for row in rows:
        temp = []
        for cell in row.find_all('td'):
            temp += [cell.text]
        Box20all += [temp]
    data += [Box20all]


    Box21 = soup.find('table', id='grdDer_SS')
    Box21all = []
    rows = Box21.find_all('tr')[1:]
    for row in rows:
        temp = []
        for cell in row.find_all('td'):
            temp += [cell.text]
        Box21all += [temp]
    data += [Box21all]


    Box22 = soup.find('table', id='grdCtrlCorp')
    Box22all = []
    rows = Box22.find_all('tr')[1:]
    for row in rows:
        temp = []
        for cell in row.find_all('td'):
            temp += [cell.text]
        Box22all += [temp]
    data += [Box22all]


    Box23 = soup.find('table', id='grdJI_Sh')
    row = Box23.find_all('tr')[1]
    Box23all = []
    for cell in row.find_all('td'):
        Box23all += [cell.text]
    data += [Box23all]


    Box24 = soup.find('table', id='grdTrust_Sh')
    row = Box24.find_all('tr')[1]
    Box24all = []
    for cell in row.find_all('td'):
        Box24all += [cell.text]
    data += [Box24all]


    Box25 = soup.find('table', id='grdPA_Sh')
    row = Box25.find_all('tr')[1]
    Box25all = []
    for cell in row.find_all('td'):
        Box25all += [cell.text]
    data += [Box25all]


    Box26 = soup.find('table', id='grdPer_CorpRel')
    row = Box26.find_all('tr')[1]
    Box26all = []
    for cell in row.find_all('td'):
        Box26all += [cell.text]
    data += [Box26all]


    Box27 = soup.find('span', id="lblDSignDate").get_text()
    data += [Box27]


    Box29 = soup.find('span', id="lblDNoAttachment").get_text()
    data += [Box29]

    return data

k=0
form2data = []
with open('FormLinks_NonDION-2003Apr01-2017Oct02.csv', newline='') as csvfile:
    linereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in linereader:
        url = row[0]
        if "Form2." in url:
            k += 1
            print(k)
            try:
                print(form2(url))
                form2data.append(form2(url))
            except:
                print("Retrying!")
                while True:
                    try:
                        print(form2(url))
                        form2data.append(form2(url))
                        break
                    except Exception:  # Replace Exception with something more specific.
                        continue

m=0
with open('Form2.csv', 'w', newline='', encoding='utf-8') as csvfile:
    linewriter = csv.writer(csvfile, delimiter='@')
    for row in form2data:
        m += 1
        print("Write Row " + str(m))
        linewriter.writerow(row)

