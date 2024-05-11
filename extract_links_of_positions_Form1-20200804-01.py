from bs4 import BeautifulSoup
import requests
import csv



def form1(url):

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

    Box5 = []
    Box5surename = soup.find('span', id="lblDSurname").get_text()
    Box5 += [Box5surename]
    Box5firstname = soup.find('span', id="lblDFirstname").get_text()
    Box5 += [Box5firstname]
    Box5middlename = soup.find('span', id="lblDMidname").get_text()
    Box5 += [Box5middlename]
    data += [Box5]

    Box8 = soup.find('span', id="lblDChiName").get_text()
    data += [Box8]

    Box9 = soup.find('span', id="lblDCharCode").get_text()
    data += [Box9]

    Box12 = soup.find('span', id="lblDEventDate").get_text()
    data += [Box12]

    Box13 = soup.find('span', id="lblDAwareDate").get_text()
    data += [Box13]


    Box14all = []
    Box14_position = soup.find('span', id="lblDEvtPosition").get_text()
    Box14all += [Box14_position]

    Box14_eventcode = soup.find('span', id="lblDEvtReason").get_text()
    Box14all += [Box14_eventcode]

    Box14_capbefore = soup.find('span', id="lblDEvtCapBefore").get_text()
    Box14all += [Box14_capbefore]

    Box14_capafter = soup.find('span', id="lblDEvtCapAfter").get_text()
    Box14all += [Box14_capafter]

    Box14_eventshare = soup.find('span', id="lblDEvtShare").get_text()
    Box14all += [Box14_eventshare]

    Box14_eventcurrency = soup.find('span', id="lblDEvtCurrency").get_text()
    Box14all += [Box14_eventcurrency]

    Box14_eventHprice = soup.find('span', id="lblDEvtHPrice").get_text()
    Box14all += [Box14_eventHprice]

    Box14_eventAprice = soup.find('span', id="lblDEvtAPrice").get_text()
    Box14all += [Box14_eventAprice]

    Box14_eventAconsider = soup.find('span', id="lblDEvtAConsider").get_text()
    Box14all += [Box14_eventAconsider]

    Box14_eventNATconsider = soup.find('span', id="lblDEvtNatConsider").get_text()
    Box14all += [Box14_eventNATconsider]

    Box14all2 = []
    try:
        Box14_position2 = soup.find('span', id="lblDEvtPosition2").get_text()
        Box14all2 += [Box14_position2]
    except:
        Box14all2 += [""]

    try:
        Box14_eventcode2 = soup.find('span', id="lblDEvtReason2").get_text()
        Box14all2 += [Box14_eventcode2]
    except:
        Box14all2 += [""]

    try:
        Box14_capbefore2 = soup.find('span', id="lblDEvtCapBefore2").get_text()
        Box14all2 += [Box14_capbefore2]
    except:
        Box14all2 += [""]

    try:
        Box14_capafter2 = soup.find('span', id="lblDEvtCapAfter2").get_text()
        Box14all2 += [Box14_capafter2]
    except:
        Box14all2 += [""]

    try:
        Box14_eventshare2 = soup.find('span', id="lblDEvtShare2").get_text()
        Box14all2 += [Box14_eventshare2]
    except:
        Box14all2 += [""]

    try:
        Box14_eventcurrency2 = soup.find('span', id="lblDEvtCurrency2").get_text()
        Box14all2 += [Box14_eventcurrency2]
    except:
        Box14all2 += [""]

    try:
        Box14_eventHprice2 = soup.find('span', id="lblDEvtHPrice2").get_text()
        Box14all2 += [Box14_eventHprice2]
    except:
        Box14all2 += [""]

    try:
        Box14_eventAprice2 = soup.find('span', id="lblDEvtAPrice2").get_text()
        Box14all2 += [Box14_eventAprice2]
    except:
        Box14all2 += [""]

    try:
        Box14_eventAconsider2 = soup.find('span', id="lblDEvtAConsider2").get_text()
        Box14all2 += [Box14_eventAconsider2]
    except:
        Box14all2 += [""]

    try:
        Box14_eventNATconsider2 = soup.find('span', id="lblDEvtNatConsider2").get_text()
        Box14all2 += [Box14_eventNATconsider2]
    except:
        Box14all2 += [""]

    data += [[Box14all, Box14all2]]



    Box15 = soup.find('table', id='grdSh_BEvt')
    Box15all = []
    rows = Box15.find_all('tr')[1:]
    for row in rows:
        temp = []
        for cell in row.find_all('td'):
            temp += [cell.text]
        Box15all += [temp]
    data += [Box15all]


    Box16 = soup.find('table', id='grdSh_AEvt')
    Box16all = []
    rows = Box16.find_all('tr')[1:]
    for row in rows:
        temp = []
        for cell in row.find_all('td'):
            temp += [cell.text]
        Box16all += [temp]
    data += [Box16all]

    Box17 = soup.find('table', id='grdCap_SS')
    Box17all = []
    rows = Box17.find_all('tr')[1:]
    for row in rows:
        temp = []
        for cell in row.find_all('td'):
            temp += [cell.text]
        Box17all += [temp]
    data += [Box17all]

    Box18 = soup.find('table', id='grdDer_SS')
    Box18all = []
    rows = Box18.find_all('tr')[1:]
    for row in rows:
        temp = []
        for cell in row.find_all('td'):
            temp += [cell.text]
        Box18all += [temp]
    data += [Box18all]

    Box19 = soup.find('table', id='grdFI_Sh')
    Box19all = []
    rows = Box19.find_all('tr')[1:]
    for row in rows:
        temp = []
        for cell in row.find_all('td'):
            temp += [cell.text]
        Box19all += [temp]
    data += [Box19all]

    Box20 = soup.find('table', id='grdCtrlCorp')
    Box20all = []
    rows = Box20.find_all('tr')[1:]
    for row in rows:
        temp = []
        for cell in row.find_all('td'):
            temp += [cell.text]
        Box20all += [temp]
    data += [Box20all]

    Box21 = soup.find('table', id='grdJI_Sh')
    row = Box21.find_all('tr')[1]
    Box21all = []
    for cell in row.find_all('td'):
        Box21all += [cell.text]
    data += [Box21all]

    Box22 = soup.find('table', id='grdTrust_Sh')
    row = Box22.find_all('tr')[1]
    Box22all = []
    for cell in row.find_all('td'):
        Box22all += [cell.text]
    data += [Box22all]

    Box23 = soup.find('table', id='grdPA_Sh')
    row = Box23.find_all('tr')[1]
    Box23all = []
    for cell in row.find_all('td'):
        Box23all += [cell.text]
    data += [Box23all]

    Box24 = soup.find('span', id="lblDSignDate").get_text()
    data += [Box24]

    Box26 = soup.find('span', id="lblDNoAttachment").get_text()
    data += [Box26]

    return data


k=0
form1data = []
with open('FormLinks_NonDION-2003Apr01-2017Oct02.csv', newline='') as csvfile:
    linereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in linereader:
        url = row[0]
        if "Form1." in url:
            k += 1
            print(k)
            try:
                print(form1(url))
                form1data.append(form1(url))
            except:
                print("Retrying!")
                while True:
                    try:
                        print(form1(url))
                        form1data.append(form1(url))
                        break
                    except Exception:  # Replace Exception with something more specific.
                        continue

m=0
with open('Form1.csv', 'w', newline='', encoding='utf-8') as csvfile:
    linewriter = csv.writer(csvfile, delimiter='@')
    for row in form1data:
        m += 1
        print("Write Row " + str(m))
        linewriter.writerow(row)











