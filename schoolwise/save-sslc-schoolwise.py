from bs4 import BeautifulSoup
import requests, urllib3, sys,time
urllib3.disable_warnings() # disable TLS
from urllib.request import Request, urlopen

#--------------------------------------------------------------
def online(url='http://www.google.com/', timeout=5):
    try:
        req = requests.head(url, timeout=timeout)
        # HTTP errors are not raised by default, this statement does that
        req.raise_for_status()
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False
#--------------------------------------------------------------

#--------------------------------------------------------------

def save_html(scode): # returns list of registernumbers
    base_url = f"https://results.kite.kerala.gov.in/school_files/{scode}.html"
    if online()==True:
        response = requests.get(base_url,verify=False,timeout=60,headers={
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Referer': 'https://sampoorna.kite.kerala.gov.in'})
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        filename = f"{scode}.html"
        file = open(filename,'w')
        file.write(str(soup))
        file.close()
    else:
            print("Waiting For Connection")
            time.sleep(20)
#------------------------------------------------------------------------------------------

schoolcodes = ['45045','45046','45050','45051','45052','45053','45054','45055','46017','46023','46024','46030','46031','46032','46033','46037','46038','46039','46040','46042','46043','46047','46049','46056','46057','46058','46060','46062','46063','46064','46065','46066','46067','46068','46069','46070','46071','46072','46073','46074','46075','47017','47018','47019','47020','47021','47022','47023','47024','47025','47026','47027','47028','47029','47030','47031','47037','47039','47040','47041','47042','47043','47044','47045','47046','47047','47049','47050','47058','47060','47061','47063','47064','47065','47066','47067','47068','47069','47070','47071','47072','47075','47080','47083','47084','47085','47087','47088','47089','47090','47094','47095','47096','47098','47099','47101','47102','47103','47104','47105','47106','47107','47108','47109','47110','47111','47113','47114','47115','47116','47117','47118','47119','47120','48001','48002','48003','48022','48034','48035','48036','48037','48038','48039','48040','48041','48042','48043','48044','48045','48046','48047','48048','48049','48050','48051','48052','48053','48054','48055','48056','48063','48076','48077','48081','48086','48090','48095','48099','48100','48104','48105','48106','48107','48114','48115','48118','48119','48126','48127','48129','48130','48131','48132','48133','48134','48135','48136','48137','48138','48139','48140','48141','48142','48143','48144','48145','48146','48148']
#------------------------------------------------------------------------------------------
count = 2672
for scode in schoolcodes :
    count = count + 1
    save_html(scode)
    sys.stdout.flush()
    sys.stdout.write(f"\r[{count}/2851] Saved {scode}.html    ")
    

print(f"-----Succesfully Saved-----")