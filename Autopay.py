import time
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

#카드 클래스 선언
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

#카드 정보 입력

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
##광동 - 작동됨
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
##팜페이 - 작동됨
def ph_pay(com, card, money):
    driver = webdriver.Chrome("./chromedriver")
    driver.get('http://my.pharmpay.co.kr/')
    driver.find_element(By.ID, 'my_pur_taxno').send_keys('5290801603')
    driver.find_element(By.ID, 'my_pur_pw').send_keys('01603',Keys.RETURN)

    while True:
        try:
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, '/html/body/div[5]/div/ul/li[3]/a').click()
            driver.find_element(By.XPATH, '/html/body/div[5]/div/ul/li[3]/ul/li[1]/a').click()
            print('로그인후 메뉴 누르기 성공')
            break
        except:
            print('로딩 미완료')

    #구매창 접속
    #신용카드 버튼 누르기
    time.sleep(2)
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
    driver.implicitly_wait(3)
    if com == 'gpm':
        com = '2298116607'
    elif com == 'fam':
        com = '1408135543'
    elif com == 'rea':
        com = '5128126399'
    else:
        print('회사를 찾을수 없습니다.')
        driver.close()
        driver.close()
        ph_pay(com,card,money)
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
        ph_pay(com,card,money)
    else:
        WebDriverWait(driver,3).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        WebDriverWait(driver,3).until(EC.alert_is_present())
        print('결제 완료')
        driver.switch_to.alert.accept()
        driver.close()
    #pharm_pay('gpm',themore1,5999)
##레아팜 - 작동됨
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

gy_pay(themore1,5999)
tj_pay(themore1,5999)
kd_pay(themore1,5999)
rp_pay(themore1,5999)
gy_pay(themore2,5999)
tj_pay(themore2,5999)
kd_pay(themore2,5999)
rp_pay(themore2,5999)
gy_pay(kakao1,5000)
tj_pay(kakao1,5000)
kd_pay(kakao1,5000)
rp_pay(themore2, 5999)
rp_pay(themore1, 5999)
ph_pay('gpm',themore1,5999)
ph_pay('gpm',themore2,5999)
ph_pay('fam',themore1,5999)
ph_pay('fam',themore2,5999)
ph_pay('rea',themore1,5999)
ph_pay('rea',themore2,5999)
