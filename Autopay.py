import requests
from bs4 import BeautifulSoup
import datetime
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

today = datetime.datetime.now().strftime("%Y%m%d")

class card:
    def carddata(self,number,yr,mo,id_billkey,dow_id):
        self.Number = number
        if len(self.Number) != 16 :
            return print('카드번호가 잘못되었습니다!')
        self.Number1 = number[0:4]
        self.Number2 = number[4:8]
        self.Number3 = number[8:12]
        self.Number4 = number[12:16]
        self.Yr = yr
        self.Mo = mo
        self.Billkey = id_billkey
        self.Dow_id = dow_id
    def yr(self):
        return self.Yr
    def mo(self):
        return self.Mo
    def number(self):
        return self.Number
    def number1(self):
        return self.Number1
    def number2(self):
        return self.Number2
    def number3(self):
        return self.Number3
    def number4(self):
        return self.Number4
    def billkey(self):
        return self.Billkey
    def dow_id(self):
        return self.Dow_id

themore1 = card()
themore1.carddata('9410618646966220','26','07','64094','550167210712BA921046')
themore2 = card()
themore2.carddata('9410618647046626','26','07','64526','550167210712BA921060')
themore3 = card()
themore3.carddata('9410618647228836','26','07','','550167210728BA039830')
kakao1 = card()
kakao1.carddata('4518421240504758','26','08','','550167210820BA190968')
cards = [themore1, themore2, themore3, kakao1]
with open('cards.bin','wb') as f:
    pickle.dump(cards, f)

##지오영 - 작동됨
def gy_pay(card, money):
    header_gy = {
    'Host': 'order.geoweb.kr',
    'Connection': 'keep-alive',
    'Content-Length': '64',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://order.geoweb.kr',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://order.geoweb.kr/Member/Login',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9',
    'Cookie': 'LoginID_Web=gd3304; .GEOWEBAUTH='}
    formdata_gy = {'LoginID':'gd3304','Password':'1234','IDSave':'true','IDSave':'false','returnUrl':""}
    response_gy = requests.post("https://order.geoweb.kr/Member/Login",data=formdata_gy,headers=header_gy,verify=False,allow_redirects=False)
    response_gy.encoding = 'euc-kr'
    soup_gy = BeautifulSoup(response_gy.text,'html.parser')
    cookie_gy = 'LoginID_Web=gd3304; '+response_gy.headers['Set-cookie']
    header_gy_payment={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "303",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": cookie_gy,
    "Host": "order.geoweb.kr",
    "Origin": "https://order.geoweb.kr",
    "Referer": "https://order.geoweb.kr/Payment/",
    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    "sec-ch-ua-mobile": "?0",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    formdata_gy_payment={
    "PaymentAmt": money,
    "jsCardType": "on",
    "CardPlan": "00",
    "cardCompany": "66",
    "txtcard1": card.number1(),
    "txtcard2": card.number2(),
    "txtcard3": card.number3(),
    "txtcard4": card.number4(),
    "txtmm": card.mo(),
    "txtyy": card.yr(),
    "chkSave": "false",
    "authtext": "1234",
    "chkRev": "false",
    "ddlAuthYear":"",
    "ddlAuthMonth":"",
    "ddlAuthDay":"",
    "mode": "2",
    "amt": money,
    "cardidx":"",
    "auth": "1234",
    "resDate":"",
    "cardnick": "신한카드"}
    response_gy_payment = requests.post("https://order.geoweb.kr/Payment",data=formdata_gy_payment,headers=header_gy_payment,verify=False,allow_redirects=False)
##티제이 - 작동됨
def tj_pay(card,money):
    header_tj_login = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '66',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.tjp.co.kr',
    'Origin': 'http://www.tjp.co.kr',
    'Referer': 'http://www.tjp.co.kr/login.php?login_p=2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }
    formdata_tj_login = {
    'service_gubun': '2',
    'remember_1': '1',
    'remember_2': '1',
    'userid': '3304',
    'userpwd': '1234'
    }
    response_tj_login = requests.post("http://www.tjp.co.kr/login_proc.php",data=formdata_tj_login,headers=header_tj_login,verify=False,allow_redirects=False)
    response_tj_login.encoding = 'euc-kr'
    soup_tj = BeautifulSoup(response_tj_login.text, 'html.parser')
    tj_header_cookie = response_tj_login.headers['Set-Cookie'].split(",")
    tj_cookie_temp = []
    for i in range(tj_header_cookie.__len__()):
        if (tj_header_cookie[i].find('deleted') == -1):
            if(tj_header_cookie[i].find('GMT') == -1):
                tj_cookie_temp.append(tj_header_cookie[i][:tj_header_cookie[i].index('; ')])
    tj_cookie = str()
    for i in tj_cookie_temp:
        tj_cookie = tj_cookie+';'+i
    tj_cookie = tj_cookie[1:]
    tj_payment_header = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '181',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': tj_cookie,
    'Host': 'www.tjp.co.kr',
    'Origin': 'http://www.tjp.co.kr',
    'Referer': 'http://www.tjp.co.kr/Payment/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }
    tj_payment_formdata = {
    'ordername': '김지수',
    'email': 'kixponent@gmail.com',
    'phoneno': '01030333304',
    'card_type': '05',
    'cardno': card.number(),
    'expyear': card.yr(),
    'expmon': card.mo(),
    'rdGub': '00',
    'amount': money,
    'cardno_save': 'N'
    }
    response_tj_payment = requests.post('http://www.tjp.co.kr/Payment/pay_proc.php',data=tj_payment_formdata,headers=tj_payment_header,verify=False)
# ##대웅 더샵
# def dw_pay(card):
#     response_dw = requests.get("https://www.shop.co.kr/front/intro/login")
#     response_dw.encoding = 'euc-kr'
#     soup_dw = BeautifulSoup(response_dw.text, 'html.parser')
#     cookie_dw1 = response_dw.headers['Set-cookie'][response_dw.headers['Set-cookie'].find('SCOUTER'):response_dw.headers['Set-cookie'].find('Max') - 2]
#     cookie_dw2 = response_dw.headers['Set-cookie'][response_dw.headers['Set-cookie'].find('JSESSIONID'):response_dw.headers['Set-cookie'].find('Secure')-15]
#     header_dw_login = {
#         "Host": "www.shop.co.kr",
#         "Connection": "keep-alive",
#         "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         "sec-ch-ua-mobile": "?0",
#         "Upgrade-Insecure-Requests": "1",
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "Sec-Fetch-Site": "same-origin",
#         "Sec-Fetch-Mode": "navigate",
#         "Sec-Fetch-User": "?1",
#         "Sec-Fetch-Dest": "document",
#         "Referer": "https://www.shop.co.kr/front/intro/login",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "ko-KR,ko;q=0.9",
#         "Cookie": cookie_dw2 + ';' + cookie_dw1 +'; USER_AREA_INFO1000118052=N^%EC%9D%B8%EC%B2%9C^%EB%8F%99%EA%B5%AC^%EC%86%A1%EB%A6%BC%EB%8F%99^; USER_BEAN=b4a9c581dfb01386871ce59b3105f1f24962735c17a67ab18f1adcf368749f6877827ca7f9d1b9ea5857e22c9875374b03eb92a319748b49ae61adeadab819d80e0cff941ea8b5de0a26edbb96709295519550961f82f2f5410cb4adec75c940f51039835d5b04284281700ad792a7ffae9152c5dd63f5ed82bfe84ce1866875d2649eed91cece4b462d2506cd62e4b1; USER_MALL_TYPE=2; USER_LOGIN_DOMAIN_ID=www; USER_SELLER_AREA=; PASSWORD_MODI_CHECK1000118052=0'}
#     response_dw_login = requests.get("https://www.shop.co.kr/front/api/auth/loginJsonp?loginType=01&userId=hm2021&userPwd=gmlakd!2021")
#     header_dw_money = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#         'Connection': 'keep-alive',
#         'Cookie': 'SCOUTER=x1tjv138s2t89o; userId=hm2021; list-myPageZoneList=monoGoods|monoGoods2|orderReBuy|frontwishList|orderList|vocGet; _gid=GA1.3.76842192.1626319395; JSESSIONID=36ECAC805F8B0987CDB98E3900CB232C; TS01df1835=0156a1c66ce54622fe65ff0c4d394838f2fc8b9d7ce9f2f4d963b651db6ec8fe5eca6bcf309f9f98516a39f0ba01095c5f772608d84fafee6696220ae6e293839cb4d50970; USER_AREA_INFO1000118052=N^%EC%9D%B8%EC%B2%9C^%EB%8F%99%EA%B5%AC^%EC%86%A1%EB%A6%BC%EB%8F%99^; USER_BEAN=b4a9c581dfb01386871ce59b3105f1f24962735c17a67ab18f1adcf368749f6877827ca7f9d1b9ea5857e22c9875374b03eb92a319748b49ae61adeadab819d80e0cff941ea8b5de0a26edbb96709295519550961f82f2f5410cb4adec75c940ec94ed73ef6d1802b645caa8df2b69755e9e6018627423edcac1ca7f476ae77ca861d312c09b2b61a7fd927e02acf03f; USER_MALL_TYPE=2; USER_LOGIN_DOMAIN_ID=www; USER_SELLER_AREA=; PASSWORD_MODI_CHECK1000118052=0; _ga_RV83N690NK=GS1.1.1626486986.70.0.1626486986.0; _ga=GA1.3.607092520.1623128379',
#         'Host': 'www.shop.co.kr',
#         'Referer': 'https://www.shop.co.kr/front/theshop/main/main',
#         'sec-ch-ua' : ' "Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile': '?0',
#         'Sec-Fetch-Dest': 'document',
#         'Sec-Fetch-Mode': 'navigate',
#         'Sec-Fetch-Site': 'same-origin',
#         'Sec-Fetch-User': '?1',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         }
#     response_dw_money = requests.get("https://www.shop.co.kr/event/raEvent.do", headers = header_dw_money)
# ##일동 - 사전등록카드
# def id_pay(card):
#     response_id = requests.get("https://www.ildongshop.com/w/login/login.do")
#     response_id.encoding = 'utf-8'
#     soup_id = BeautifulSoup(response_id.text, 'html.parser')
#     Cookie_id = response_id.headers['Set-Cookie'][response_id.headers['Set-Cookie'].find('JSESSIONID'):response_id.headers['Set-Cookie'].find('Path=/w; Secure;')-2]
#     header_id = {
#     'Accept':'application/json, text/javascript, */*; q=0.01',
#     'Accept-Encoding':'gzip, deflate, br',
#     'Accept-Language':'ko-KR,ko;q=0.9',
#     'Connection':'keep-alive',
#     'Content-Type':'application/json; charset=utf-8',
#     'Cookie':Cookie_id+'; _ga=GA1.2.1412552661.1625544312; _gid=GA1.2.631508235.1625544312',
#     'Host':'www.ildongshop.com',
#     'Referer':'https://www.ildongshop.com/w/login/login.do',
#     'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#     'sec-ch-ua-mobile':'?0',
#     'Sec-Fetch-Dest':'empty',
#     'Sec-Fetch-Mode':'cors',
#     'Sec-Fetch-Site':'same-origin',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
#     'X-Requested-With':'XMLHttpRequest'
#     }
#     response_id_login = requests.get("https://www.ildongshop.com/w/ajax/login/loginCheckAjax.do?userId=hm2021&userPw=gml!2021",headers=header_id)
#     header_id_start = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#         'Connection': 'keep-alive',
#         'Cookie': Cookie_id,
#         'Host': 'www.ildongshop.com',
#         'Referer': 'https://www.ildongshop.com/w/main.do',
#         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile': '?0',
#         'Sec-Fetch-Dest': 'document',
#         'Sec-Fetch-Mode': 'navigate',
#         'Sec-Fetch-Site': 'same-origin',
#         'Sec-Fetch-User': '?1',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     }
#     response_id_start = requests.get("https://www.ildongshop.com/w/order/deposit.do", headers = header_id_start)
#     response_id_start.encoding = 'utf-8'
#     soup_id_start = BeautifulSoup(response_id_start.text, 'html.parser')
#     #일동 카트
# ##    header_id_cart = {
# ##        'Accept': 'application/json, text/javascript, */*; q=0.01',
# ##        'Accept-Encoding': 'gzip, deflate, br',
# ##        'Accept-Language': 'ko-KR,ko;q=0.9',
# ##        'Connection': 'keep-alive',
# ##        'Content-Length': '0',
# ##        'Content-Type': 'application/json',
# ##        'Cookie': Cookie_id,
# ##        'Host': 'www.ildongshop.com',
# ##        'Origin': 'https://www.ildongshop.com',
# ##        'Referer': 'https://www.ildongshop.com/w/order/deposit.do',
# ##        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
# ##        'sec-ch-ua-mobile': '?0',
# ##        'Sec-Fetch-Dest': 'empty',
# ##        'Sec-Fetch-Mode': 'cors',
# ##        'Sec-Fetch-Site': 'same-origin',
# ##        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
# ##        'X-Requested-With': 'XMLHttpRequest'
# ##    }
# ##    jsondata_id_cart = {
# ##            "result": 'true',
# ##            "msg": "",
# ##            "error_code": "",
# ##            "data1": "9",
# ##            "data2": "0",
# ##            "data3": "",
# ##            "code": '0',
# ##            "min_qty": ""
# ##    }
# ##    response_id_beforepayment = requests.post('https://www.ildongshop.com/w/ajax/cart/CountCart.do', data=jsondata_id_cart, headers=header_id_cart, verify=False, allow_redirects=False)
#     header_id_checker = {
#         'accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
#         'accept-encoding':'gzip, deflate, br',
#         'accept-language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#         'connection':'keep-alive',
#         'cookie':Cookie_id,
#         'host':'www.ildongshop.com',
#         'referer':'https://www.ildongshop.com/w/css/shop.css?ver=1.6.37',
#         'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile':'?0',
#         'sec-fetch-dest':'image',
#         'sec-fetch-mode':'no-cors',
#         'sec-fetch-site':'same-origin',
#         'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
#     }
#     #결제전 사전 절차
#     header_id_beforepayment1 = {
#         'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'accept-encoding':'gzip, deflate, br',
#         'accept-language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#         'connection':'keep-alive',
#         'cookie':Cookie_id,
#         'host':'www.ildongshop.com',
#         'referer':'https://www.ildongshop.com/w/order/deposit_result.do?orderidx=109043472',
#         'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile':'?0',
#         'sec-fetch-dest':'document',
#         'sec-fetch-mode':'navigate',
#         'sec-fetch-site':'same-origin',
#         'sec-fetch-user':'?1',
#         'upgrade-insecure-requests':'1',
#         'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
#     header_id_countcart = {
#         'accept':'application/json, text/javascript, */*; q=0.01',
#         'accept-encoding':'gzip, deflate, br',
#         'accept-language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#         'connection':'keep-alive',
#         'content-length':'0',
#         'content-type':'application/json',
#         'cookie':Cookie_id,
#         'host':'www.ildongshop.com',
#         'origin':'https://www.ildongshop.com',
#         'referer':'https://www.ildongshop.com/w/order/deposit.do',
#         'sec-ch-ua' :'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile':'?0',
#         'sec-fetch-dest':'empty',
#         'sec-fetch-mode':'cors',
#         'sec-fetch-site':'same-origin',
#         'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'x-requested-with':'XMLHttpRequest'
#     }
#     header_id_beforepayment2 = {
#         'Host': 'www.ildongshop.com',
#         'Connection': 'keep-alive',
#         'Content-Length': '27',
#         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'Accept': 'application/json, text/javascript, */*; q=0.01',
#         'X-Requested-With': 'XMLHttpRequest',
#         'sec-ch-ua-mobile': '?0',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'Content-Type': 'application/json',
#         'Origin': 'https://www.ildongshop.com',
#         'Sec-Fetch-Site': 'same-origin',
#         'Sec-Fetch-Mode': 'cors',
#         'Sec-Fetch-Dest': 'empty',
#         'Referer': 'https://www.ildongshop.com/w/order/deposit.do',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'ko-KR,ko;q=0.9',
#         'Cookie': Cookie_id
#     }
#     formdata_id_beforepayment = {
#         "orderidx": "1",
#         "dsNo": "3"
#     }
#     response_id_checker = requests.get('https://www.ildongshop.com/w/images/contents/deposit_btn_active.png', headers = header_id_checker, verify=False)
#     response_id_beforepayment1 = requests.post('https://www.ildongshop.com/w/order/deposit.do',headers=header_id_beforepayment1,verify=False)
#     response_id_countcart = requests.post('https://www.ildongshop.com/w/ajax/cart/CountCart.do',headers=header_id_countcart)
#     # response_id_info1 = requests.post('https://www.ildongshop.com/w/ajax/product/productInfoAjax.do',headers=header_id_info1, data=data_id_info1)
#     # response_id_info2 = requests.post('https://www.ildongshop.com/w/ajax/product/productInfoAjax.do',headers=header_id_info2, data=data_id_info2)
#     # response_id_info3 = requests.post('https://www.ildongshop.com/w/ajax/product/productInfoAjax.do',headers=header_id_info3, data=data_id_info3)
#     response_id_beforepayment2 = requests.post('https://www.ildongshop.com/w/ajax/order/checkBeforeDepositOrder.do',data=formdata_id_beforepayment,headers=header_id_beforepayment2,verify=False)
#     response_id_beforepayment1.encoding = 'utf-8'
#     soup_id_beforepayment = BeautifulSoup(response_id_beforepayment1.text, 'html.parser')
#     response_id_beforepayment2.encoding = 'utf-8'
#     soup_id_beforepayment2 = BeautifulSoup(response_id_beforepayment2.text, 'html.parser')
#     #결제 절차
#     header_id_payment = {
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding':'gzip, deflate, br',
#     'Accept-Language':'ko-KR,ko;q=0.9',
#     'Cache-Control':'max-age=0',
#     'Connection':'keep-alive',
#     'Content-Length':'1170',
#     'Content-Type':'application/x-www-form-urlencoded',
#     'Cookie': Cookie_id, # + '; _ga=GA1.2.1412552661.1625544312; _gid=GA1.2.631508235.1625544312; _gat=1',
#     'Host':'www.ildongshop.com',
#     'Origin':'https://www.ildongshop.com',
#     'Referer':'https://www.ildongshop.com/w/order/deposit.do',
#     'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#     'sec-ch-ua-mobile':'?0',
#     'Sec-Fetch-Dest':'document',
#     'Sec-Fetch-Mode':'navigate',
#     'Sec-Fetch-Site':'same-origin',
#     'Sec-Fetch-User':'?1',
#     'Upgrade-Insecure-Requests':'1',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
#     }
#     formdata_id_payment = {
#     'EP_mall_id': '05531302',
#     'EP_mall_nm': '일동샵',
#     'EP_currency': '00',
#     'EP_return_url': 'https://www.ildongshop.com/w/order/order_res.do',
#     'EP_ci_url':'',
#     'EP_charset': 'UTF-8',
#     'EP_user_type': '2',
#     'EP_order_no': '108939140',
#     'EP_memb_user_no': '172431',
#     'EP_product_nm': '예치금',
#     'EP_product_amt': '5999',
#     'EP_user_id': 'hm2021',
#     'EP_user_name': '김지수',
#     'EP_user_nm': '김지수',
#     'EP_user_mail': 'kixponent@gmail.com',
#     'EP_user_phone1': '01030333304',
#     'EP_user_define1': '3',
#     'EP_user_define2': '1',
#     'EP_user_define3':'',
#     'EP_user_define4':'',
#     'EP_user_define5':'',
#     'EP_user_define6':'',
#     'EP_product_type': '0',
#     'EP_window_type': 'iframe',
#     'EP_res_cd':'',
#     'EP_res_msg':'',
#     'EP_tr_cd':'',
#     'EP_ret_pay_type':'',
#     'EP_ret_complex_yn':'',
#     'EP_card_code':'',
#     'EP_eci_code':'',
#     'EP_card_req_type':'',
#     'EP_save_useyn':'',
#     'EP_trace_no':'',
#     'EP_sessionkey':'',
#     'EP_encrypt_data':'',
#     'EP_pnt_cp_cd':'',
#     'EP_spay_cp':'',
#     'EP_prepaid_cp':'',
#     'EP_card_prefix':'',
#     'EP_card_no_7':'',
#     'EP_usedcard_code':'',
#     'EP_pay_type': '60',
#     'payway': '1',
#     'billKey_idx': card.billkey(),
#     'billKey_cardgbn':'',
#     'EP_install_period': '00',
#     'EP_cno':'',
#     'req_cno':'',
#     'cli_ver':'',
#     'EP_client_version':'',
#     'EP_req_type':'',
#     'EP_cert_no':'',
#     'EP_cert_value':'',
#     'EP_coupon_amt':'',
#     'EP_point_amt':'',
#     'EP_card_cd':'',
#     'EP_tax_flg':'',
#     'EP_com_free_amt':'',
#     'EP_com_tax_amt':'',
#     'EP_com_vat_amt':'',
#     'EP_spay_txtype':'',
#     'EP_card_amt':'',
#     'EP_noint':'' }
#     response_id_payment = requests.post("https://www.ildongshop.com/w/order/easypay_deposit_request.do",data=formdata_id_payment,headers=header_id_payment,verify=False,allow_redirects=False)
# #결제 후 절차
#     header_id_afterpayment = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'ko-KR,ko;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Cookie': Cookie_id,
#     'Host': 'www.ildongshop.com',
#     'Referer': 'https://www.ildongshop.com/w/order/deposit.do',
#     'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#     'sec-ch-ua-mobile': '?0',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     }
#     id_id = response_id_payment.headers['Location'][response_id_payment.headers['Location'].find('orderidx')+9:response_id_payment.headers['Location'].find('orderidx')+18]
#     response_id_afterpayment = requests.get("https://www.ildongshop.com/w/order/deposit_result.do?orderidx=" + id_id, headers=header_id_payment, verify=False, allow_redirects=False)
# ##일동 - 신용카드
# def id_paycard(card):
#     response_id = requests.get("https://www.ildongshop.com/w/login/login.do")
#     response_id.encoding = 'utf-8'
#     soup_id = BeautifulSoup(response_id.text, 'html.parser')
#     Cookie_id = response_id.headers['Set-Cookie'][
#                 response_id.headers['Set-Cookie'].find('JSESSIONID'):response_id.headers['Set-Cookie'].find(
#                     'Path=/w; Secure;') - 2]
#     header_id = {
#         'Accept': 'application/json, text/javascript, */*; q=0.01',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'ko-KR,ko;q=0.9',
#         'Connection': 'keep-alive',
#         'Content-Type': 'application/json; charset=utf-8',
#         'Cookie': Cookie_id + '; _ga=GA1.2.1412552661.1625544312; _gid=GA1.2.631508235.1625544312',
#         'Host': 'www.ildongshop.com',
#         'Referer': 'https://www.ildongshop.com/w/login/login.do',
#         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile': '?0',
#         'Sec-Fetch-Dest': 'empty',
#         'Sec-Fetch-Mode': 'cors',
#         'Sec-Fetch-Site': 'same-origin',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
#         'X-Requested-With': 'XMLHttpRequest'
#     }
#     response_id_login = requests.get(
#         "https://www.ildongshop.com/w/ajax/login/loginCheckAjax.do?userId=hm2021&userPw=gml!2021", headers=header_id)
#     header_id_start = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#         'Connection': 'keep-alive',
#         'Cookie': Cookie_id,
#         'Host': 'www.ildongshop.com',
#         'Referer': 'https://www.ildongshop.com/w/main.do',
#         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile': '?0',
#         'Sec-Fetch-Dest': 'document',
#         'Sec-Fetch-Mode': 'navigate',
#         'Sec-Fetch-Site': 'same-origin',
#         'Sec-Fetch-User': '?1',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     }
#     response_id_start = requests.get("https://www.ildongshop.com/w/order/deposit.do", headers=header_id_start)
#     response_id_start.encoding = 'euc-kr'
#     soup_id_start = BeautifulSoup(response_id_start.text, 'html.parser')
#     header_id_card = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'ko-KR,ko;q=0.9',
#         'Cache-Control': 'max-age=0',
#         'Connection': 'keep-alive',
#         'Content-Length': '1217',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Host': 'pg.easypay.co.kr',
#         'Origin': 'https://www.ildongshop.com',
#         'Referer': 'https://www.ildongshop.com/',
#         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile': '?0',
#         'Sec-Fetch-Dest': 'iframe',
#         'Sec-Fetch-Mode': 'navigate',
#         'Sec-Fetch-Site': 'cross-site',
#         'Sec-Fetch-User': '?1',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     }
#     # formdata_id_card = {
#     #     'EP_mall_id': '05545414',
#     #     'EP_mall_nm': '%EC%9D%BC%EB%8F%99%EC%83%B5',
#     #     'EP_currency': '00',
#     #     'EP_return_url': 'https://www.ildongshop.com/w/order/order_res.do',
#     #     'EP_ci_url': '',
#     #     'EP_charset': 'UTF-8',
#     #     'EP_user_type': '2',
#     #     'EP_order_no': '108993734',
#     #     'EP_memb_user_no': '172431',
#     #     'EP_product_nm': '%EC%98%88%EC%B9%98%EA%B8%88',
#     #     'EP_product_amt': '5999',
#     #     'EP_user_id': 'hm2021',
#     #     'EP_user_name': '김지수',
#     #     'EP_user_nm': '%EA%B9%80%EC%A7%80%EC%88%98',
#     #     'EP_user_mail': 'kixponent@gmail.com',
#     #     'EP_user_phone1': '01030333304',
#     #     'EP_user_define1': '3',
#     #     'EP_user_define2': '1',
#     #     'EP_user_define3': ''',
#     #     'EP_user_define4': ''',
#     #     'EP_user_define5': ''',
#     #     'EP_user_define6': ''',
#     #     'EP_product_type': '0',
#     #     'EP_window_type': 'iframe',
#     #     'EP_res_cd': '',
#     #     'EP_res_msg': '',
#     #     'EP_tr_cd': '',
#     #     'EP_ret_pay_type': '',
#     #     'EP_ret_complex_yn': '',
#     #     'EP_card_code': '',
#     #     'EP_eci_code': '',
#     #     'EP_card_req_type': '',
#     #     'EP_save_useyn': '',
#     #     'EP_trace_no': '',
#     #     'EP_sessionkey': '',
#     #     'EP_encrypt_data': '',
#     #     'EP_pnt_cp_cd': '',
#     #     'EP_spay_cp': '',
#     #     'EP_prepaid_cp': '',
#     #     'EP_card_prefix': '',
#     #     'EP_card_no_7': '',
#     #     'EP_usedcard_code': '',
#     #     'EP_pay_type': '11',
#     #     'payway': '1',
#     #     'billKey_idx': '',
#     #     'billKey_cardgbn': '',
#     #     'EP_install_period': '',
#     #     'EP_cno': '',
#     #     'req_cno': '',
#     #     'cli_ver': '',
#     #     'EP_client_version': '',
#     #     'EP_req_type': '',
#     #     'EP_cert_no': '',
#     #     'EP_cert_value': '',
#     #     'EP_coupon_amt': '',
#     #     'EP_point_amt': '',
#     #     'EP_card_cd': '',
#     #     'EP_tax_flg': '',
#     #     'EP_com_free_amt': '',
#     #     'EP_com_tax_amt': '',
#     #     'EP_com_vat_amt': '',
#     #     'EP_spay_txtype': '',
#     #     'EP_card_amt': '',
#     #     'EP_noint': '',
#     # }
#     # response_id_start = requests.post("https://pg.easypay.co.kr/webpay/MainAction.do", headers=header_id_card)
# ##한미
# def hm_pay(card):
#     response_hm = requests.get("https://www.hmpmall.co.kr/login.do")
#     response_hm.encoding = 'euc-kr'
#     soup_hm = BeautifulSoup(response_hm.text, 'html.parser')
##동화 - 작동됨
# def dow_pay(card,money):
#     response_dw = requests.get('https://www.dw1897.co.kr/emall/')
#     cookie_dw_login = response_dw.headers['Set-Cookie'][:response_dw.headers['Set-Cookie'].find(';')]
#     header_dw_login = {
#         'Accept': 'application/json, text/javascript, */*; q=0.01',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'ko-KR,ko;q=0.9',
#         'Connection': 'keep-alive',
#         'connection_type': 'web_emall',
#         'Content-Length': '74',
#         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'Cookie': cookie_dw_login,
#         'Host': 'www.dw1897.co.kr',
#         'Origin': 'https://www.dw1897.co.kr',
#         'os': 'Chrome',
#         'os_ver': '0',
#         'Referer': 'https://www.dw1897.co.kr/emall/',
#         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile': '?0',
#         'Sec-Fetch-Dest': 'empty',
#         'Sec-Fetch-Mode': 'cors',
#         'Sec-Fetch-Site': 'same-origin',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'X-Requested-With': 'XMLHttpRequest'
#     }
#     data_dw_login = {
#         'coakey': 'USER_CO_LOGIN_R_001',
#         'IN_USER_ID': 'hm2021',
#         'IN_PASSWD': 'gml!2021',
#         'IN_DEVICE': ''
#     }
#     response_dw_login = requests.post("https://www.dw1897.co.kr/emall/proxy/logimax/auth/login", data= data_dw_login, headers = header_dw_login)
#     response_dw_paypage = requests.get('https://www.dw1897.co.kr/emall/order/balance_pay')
#     response_dw_paypage.encoding = 'euc-kr'
#     soup_dw_paypage = BeautifulSoup(response_dw_paypage.text, 'html.parser')
#     Cookie_dw = response_dw.headers['Set-Cookie'][:response_dw.headers['Set-Cookie'].find(';')] + '; ' + \
#                 response_dw_login.headers['Set-Cookie'][:response_dw_login.headers['Set-Cookie'].find(';')]
#     data_dw_coa1 = {
#         'coakey' : 'USER_PRODUCT_R_001',
#         'IN_JOB' : 'CATEGORY'
#     }
#     header_dw_coa1 = {
#         'accept':'application/json, text/javascript, */*; q=0.01',
#         'accept-encoding':'gzip, deflate, br',
#         'accept-language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#         'connection':'keep-alive',
#         'connection_type':'web_emall',
#         'content-length':'41',
#         'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
#         'cookie':Cookie_dw,
#         'device_no':'',
#         'host':'www.dw1897.co.kr',
#         'origin':'https://www.dw1897.co.kr',
#         'os':'Chrome',
#         'os_ver':'0',
#         'phone_no':'',
#         'referer':'https://www.dw1897.co.kr/emall/order/balance_pay',
#         'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile':'?0',
#         'sec-fetch-dest':'empty',
#         'sec-fetch-mode':'cors',
#         'sec-fetch-site':'same-origin',
#         'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'x-requested-with':'XMLHttpRequest'
#     }
#     response_dw_coa1 = requests.post("https://www.dw1897.co.kr/emall/proxy/logimax/coa/extstore", data= data_dw_coa1, headers = header_dw_coa1)
#     data_dw_coa2 = {
#         'coakey' : 'USER_PRODUCT_CART',
#         'IN_JOB' : 'COUNT'
#     }
#     header_dw_coa2 = {
#         'accept': 'application/json, text/javascript, */*; q=0.01',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#         'connection': 'keep-alive',
#         'connection_type': 'web_emall',
#         'content-length': '37',
#         'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'cookie': Cookie_dw,
#         'device_no': '',
#         'host': 'www.dw1897.co.kr',
#         'origin': 'https://www.dw1897.co.kr',
#         'os': 'Chrome',
#         'os_ver': '0',
#         'phone_no': '',
#         'referer': 'https://www.dw1897.co.kr/emall/order/balance_pay',
#         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'x-requested-with': 'XMLHttpRequest'
#     }
#     response_dw_coa2 = requests.post("https://www.dw1897.co.kr/emall/proxy/logimax/coa/extstore", data=data_dw_coa2,
#                                      headers=header_dw_coa2)
#     data_dw_coa3 = {
#         'coakey' : 'USER_COLLECT_JANGO'
#     }
#     header_dw_coa3 = {
#         'accept': 'application/json, text/javascript, */*; q=0.01',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#         'connection': 'keep-alive',
#         'connection_type': 'web_emall',
#         'content-length': '25',
#         'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'cookie': Cookie_dw,
#         'device_no': '',
#         'host': 'www.dw1897.co.kr',
#         'origin': 'https://www.dw1897.co.kr',
#         'os': 'Chrome',
#         'os_ver': '0',
#         'phone_no': '',
#         'referer': 'https://www.dw1897.co.kr/emall/order/balance_pay',
#         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'x-requested-with': 'XMLHttpRequest'
#     }
#     response_dw_coa3 = requests.post("https://www.dw1897.co.kr/emall/proxy/logimax/coa/extstore", data=data_dw_coa3,
#                                      headers=header_dw_coa3)
#     Jango = response_dw_coa3.text[response_dw_coa3.text.find('"JANGO"')+9:response_dw_coa3.text.find('}')-1]
#     data_dw_coa4 = {
#         'coakey' : 'USER_MYINFO_EASYPAY_CRUD',
#         'IN_JOB' : 'R'
#     }
#     header_dw_coa4 = {
#         'accept': 'application/json, text/javascript, */*; q=0.01',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#         'connection': 'keep-alive',
#         'connection_type': 'web_emall',
#         'content-length': '40',
#         'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'cookie': Cookie_dw,
#         'device_no': '',
#         'host': 'www.dw1897.co.kr',
#         'origin': 'https://www.dw1897.co.kr',
#         'os': 'Chrome',
#         'os_ver': '0',
#         'phone_no': '',
#         'referer': 'https://www.dw1897.co.kr/emall/order/balance_pay',
#         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'x-requested-with': 'XMLHttpRequest'
#     }
#     response_dw_coa4 = requests.post("https://www.dw1897.co.kr/emall/proxy/logimax/coa/extstore", data=data_dw_coa4,
#                                      headers=header_dw_coa4)
#     data_dw_coa5 = {
#         'coakey':'USER_CO_COMMON_R',
#         'IN_JOB':'PWD',
#         'IN_PASSWD':'gml!2021'
#     }
#     header_dw_coa5 = {
#         'accept': 'application/json, text/javascript, */*; q=0.01',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#         'connection': 'keep-alive',
#         'connection_type': 'web_emall',
#         'content-length': '53',
#         'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'cookie': Cookie_dw,
#         'device_no': '',
#         'host': 'www.dw1897.co.kr',
#         'origin': 'https://www.dw1897.co.kr',
#         'os': 'Chrome',
#         'os_ver': '0',
#         'phone_no': '',
#         'referer': 'https://www.dw1897.co.kr/emall/order/balance_pay',
#         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'x-requested-with': 'XMLHttpRequest'
#     }
#     response_dw_coa5 = requests.post("https://www.dw1897.co.kr/emall/proxy/logimax/coa/extstore", data=data_dw_coa5,
#                                      headers=header_dw_coa5)
#     data_dw_coa6 = {
#         'coakey':'USER_COLLECT_MASTER',
#         'IN_JANGO':Jango,
#         # 'IN_AMT':money
#         'IN_AMT':'50000'
#     }
#     header_dw_coa6 = {
#         'accept': 'application/json, text/javascript, */*; q=0.01',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#         'connection': 'keep-alive',
#         'connection_type': 'web_emall',
#         'content-length': '54',
#         'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'cookie': Cookie_dw,
#         'device_no': '',
#         'host': 'www.dw1897.co.kr',
#         'origin': 'https://www.dw1897.co.kr',
#         'os': 'Chrome',
#         'os_ver': '0',
#         'phone_no': '',
#         'referer': 'https://www.dw1897.co.kr/emall/order/balance_pay',
#         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'x-requested-with': 'XMLHttpRequest'
#     }
#     response_dw_coa6 = requests.post("https://www.dw1897.co.kr/emall/proxy/logimax/coa/extstore", data=data_dw_coa6,
#                                      headers=header_dw_coa6)
#     EP_order_no = response_dw_coa6.text[response_dw_coa6.text.find('"OUT_COLLECT_NO"')+18:response_dw_coa6.text.find('"}')]
#     header_dw_payfinish = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'ko-KR,ko;q=0.9',
#         'Cache-Control': 'max-age=0',
#         'Connection': 'keep-alive',
#         'Content-Length': '1557',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Cookie': Cookie_dw,
#         'Host': 'www.dw1897.co.kr',
#         'Origin': 'https://www.dw1897.co.kr',
#         'Referer': 'https://www.dw1897.co.kr/emall/order/balance_pay',
#         'sec-ch-ua' : '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#         'sec-ch-ua-mobile': '?0',
#         'Sec-Fetch-Dest': 'document',
#         'Sec-Fetch-Mode': 'navigate',
#         'Sec-Fetch-Site': 'same-origin',
#         'Sec-Fetch-User': '?1',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
#     data_dw_payfinish = {
#         'EP_mall_nm': '%EB%8F%99%ED%99%94%20eMall',
#         'EP_currency': '00',
#         'EP_return_url': 'https://www.dw1897.co.kr/emall/KiccCard/order_res',
#         'EP_ci_url': '',
#         'EP_lang_flag': 'KOR',
#         'EP_charset': 'UTF-8',
#         'EP_user_id': '1060068',
#         'EP_memb_user_no': '2021050700007',
#         'EP_user_nm': '%EA%B9%80%EC%A7%80%EC%88%98',
#         'EP_user_mail': 'Kixponent@gmail.com',
#         'EP_user_phone1': '032-761-5336',
#         'EP_user_phone2': '',
#         'EP_user_addr': '%EC%9D%B8%EC%B2%9C%20%EB%8F%99%EA%B5%AC%20%EC%86%A1%EB%A6%BC%EB%A1%9C%2084%20(%EC%86%A1%EB%A6%BC%EB%8F%99)%201%EC%B8%B5',
#         'EP_user_define1': '',
#         'EP_user_define2': '',
#         'EP_user_define3': '',
#         'EP_user_define4': '',
#         'EP_user_define5': '',
#         'EP_user_define6': '',
#         'EP_product_type': '0',
#         'EP_product_expr': today,
#         'EP_disp_cash_yn': '',
#         'EP_usedcard_code': '',
#         'EP_quota': '',
#         'EP_os_cert_flag': '2',
#         'EP_noinst_flag': '',
#         'EP_noinst_term': '029-02:03',
#         'EP_set_point_card_yn': '',
#         'EP_point_card': '029-40',
#         'EP_join_cd': '',
#         'EP_kmotion_useyn': 'Y',
#         'EP_vacct_bank': '',
#         'EP_vacct_end_date': '',
#         'EP_vacct_end_time': '',
#         'EP_prepaid_cp': '',
#         'EP_res_cd': '',
#         'EP_res_msg': '',
#         'EP_tr_cd': '00101000',
#         'EP_ret_pay_type': '',
#         'EP_ret_complex_yn': '',
#         'EP_card_code': '',
#         'EP_eci_code': '',
#         'EP_card_req_type': '',
#         'EP_save_useyn': '',
#         'EP_trace_no': '',
#         'EP_sessionkey': '',
#         'EP_encrypt_data': '',
#         'EP_spay_cp': '',
#         'EP_card_prefix': '',
#         'EP_card_no_7': '',
#         'EP_mall_id': '05550167',
#         'KiccMallId': '05550166',
#         'KiccEasyId': '05550167',
#         'EP_order_no': EP_order_no,
#         'EP_pay_type': 'batch',
#         'EP_cert_type': '',
#         'EP_product_nm': '%EC%9E%94%EA%B3%A0%EA%B2%B0%EC%A0%9C',
#         'EP_product_amt': money,
#         'EP_card_no': card.dow_id(),
#         'EP_card_txtype': '41',
#         'EP_req_type': '0',
#         'EP_card_amt': money,
#         'EP_wcc': '@',
#         'EP_noint': '00',
#         'EP_install_period': '00',
#         'EP_tot_amt': money,
#     }
#     response_dw_payfinish = requests.post('https://www.dw1897.co.kr/emall/KiccCard/batch_easypay_request', data = data_dw_payfinish, headers = header_dw_payfinish)
##광동 - 잘작동함
def kd_pay(card,money):
    if card == themore1:
        cardno = 4103
    elif card == themore2:
        cardno = 4106
    elif card == kakao1:
        cardno = 4108
    else:
        pass
    response_kd = requests.get('https://kdshop.co.kr/member/login.do')
    cookie_kd_login = response_kd.headers['Set-Cookie'][:response_kd.headers['Set-Cookie'].find(';')]

    data_kd_login = {
        'mode':'',
        'xpw':'gml!2021',
        'redirect':'',
        'snsType':'',
        'snsId':'',
        'email':'',
        'id':'hm2021',
        'pw':''
    }
    response_kd_login = requests.post("https://kdshop.co.kr/member/login_act.do", data= data_kd_login, cookies = response_kd.cookies)
    response_kd_paypage = requests.get('https://kdshop.co.kr/mypage/deposit_charge_pop.do', cookies= response_kd_login.cookies)
    # response_kd_paypage.encoding = 'euc-kr'
    data_kd_pay = {
        'price': money,
        'payidx': cardno,
        'installPeriod': '00',
        'noint': '00'}

    response_kd_payment = requests.post('https://kdshop.co.kr/mypage/deposit_charge_req.do',  data= data_kd_pay, cookies= response_kd_paypage.cookies)

##팜페이
def ph_pay(com, card, money):
    driver = webdriver.Chrome("./chromedriver")
    driver.get('http://my.pharmpay.co.kr/')
    driver.find_element(By.ID, 'my_pur_taxno').send_keys('5290801603')
    driver.find_element(By.ID, 'my_pur_pw').send_keys('01603',Keys.RETURN)

    while True:
        try:
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/ul/li[3]/a')))
            driver.find_element(By.XPATH, '/html/body/div[5]/div/ul/li[3]/a').click()
            driver.find_element(By.XPATH, '/html/body/div[5]/div/ul/li[3]/ul/li[1]/a').click()
            print('로그인후 메뉴 누르기 성공')
            break
        except:
            print('로딩 미완료')

    #구매창 접속
    #신용카드 버튼 누르기
    driver.implicitly_wait(3)
    while True:
        try:
            print('신용카드 버튼 누르기')
            driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[2]/div/button[2]').click()
            print('신용카드 버튼 누름')
            break
        except:
            print('신용카드 버튼 누르기 실패')
    ##지오팜 카드1
    #지오팜
    driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[3]/td[2]/input').send_keys('5999')
    #카드1
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[1]').send_keys(card.number1())
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[2]').send_keys(card.number2())
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[3]').send_keys(card.number3())
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[4]').send_keys(card.number4())
    #유효기간
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[1]/option[8]').click()
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[2]/option[6]').click()
    #일시불
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[4]/select/option[2]').click()
    #약관동의
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[3]/button[1]/i').click()
    if com == 'gpm':
        com = '2298116607'
    elif com == 'fam':
        com = '1408135543'
    elif com == 'rea':
        com = '5128126399'
    else:
        print('회사를 찾을수 없습니다.')
        driver.close()
    while True:
        try:
            print('거래처 옵션 버튼 누르기')
            driver.find_element(By.NAME,com).click()
            print('거래처 옵션 버튼 누름')
            break
        except:
            print('거래처 누르기 실패')
            driver.close()
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[3]/button').click()
    if '신한엘지카드' in driver.switch_to.alert.text:
        print('결제 실패')
        driver.switch_to.alert.accept()
        driver.close()
        pharm_pay(com,card,money)
    else:
        driver.switch_to.alert.accept()
        driver.implicitly_wait(3)
        print('결제 완료')
        driver.switch_to.alert.accept()
        driver.close()
    #pharm_pay('gpm',themore1,5999)
##레아팜
def rp_pay(card,money):
    login1 = requests.get('http://bmpharm.co.kr/iskyz.aspx')
    login_cookie = login1.cookies
    login2 = requests.get('http://bmpharm.co.kr/iskyz.aspx?AspxAutoDetectCookieSupport=1', cookies = login1.cookies)
    login_cookie.update(login2.cookies)
    login3 = requests.get('http://bmpharm.co.kr/Login/incLogin.aspx?id=hm2021&pwd=gml!2021&s=0', cookies = login2.cookies , )
    login_cookie.update(login3.cookies)
    cardpay = requests.get('http://bmpharm.co.kr/Kicc/SkyzPayAuth.aspx', cookies = login3.cookies)
    login_cookie.update(cardpay.cookies)

    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    driver = webdriver.Chrome("./chromedriver", options=options)
    # driver = webdriver.Chrome("./chromedriver")
    driver.get('http://bmpharm.co.kr/')
    for cookie in login_cookie:
        driver.add_cookie({
            'name': cookie.name,
            'value': cookie.value,
            'path': '/',
            'domain': cookie.domain,
        })
    driver.get('http://bmpharm.co.kr/Kicc/SkyzPayAuth.aspx')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, 'btnCreadit')))
    driver.find_element(By.ID, 'card_no1').send_keys(card.number1())
    driver.find_element(By.ID, 'card_no2').send_keys(card.number2())
    driver.find_element(By.ID, 'card_no3').send_keys(card.number3())
    driver.find_element(By.ID, 'card_no4').send_keys(card.number4())
    driver.find_element(By.XPATH, '//*[@id="expire_mm"]/option[8]').click()
    driver.find_element(By.XPATH, '//*[@id="expire_yy"]/option[6]').click()
    driver.find_element(By.ID, 'EP_product_amt').send_keys('6109')
    driver.find_element(By.XPATH, '//*[@id="selRate"]/option[4]').click()
    driver.find_element(By.ID, 'btnCreadit').click()
    driver.close()
    #rp_pay(themore2,5999)
# def pay_all(card,money):
#     gy_pay(card,money)
#     tj_pay(card,money)
#     dow_pay(card,money)

# gy_pay(themore1,5999)
# tj_pay(themore1,5999)
# kd_pay(themore1,5999)
# rp_pay(themore1,5999)
# gy_pay(themore2,5999)
# tj_pay(themore2,5999)
# kd_pay(themore2,5999)
# rp_pay(themore2,5999)
# gy_pay(kakao1,5000)
# tj_pay(kakao1,5000)
# kd_pay(kakao1,5000)
# ph_pay('gpm',themore1,5999)
# ph_pay('gpm',themore2,5999)
# ph_pay('fam',themore1,5999)
# ph_pay('fam',themore2,5999)
# ph_pay('rea',themore1,5999)
# ph_pay('rea',themore2,5999)
# rp_pay(themore1, 5999)
# rp_pay(themore2, 5999)