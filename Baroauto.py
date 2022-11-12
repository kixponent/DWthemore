# from telnetlib import EC
import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pickle
import glob
import requests

find_cookie = False
cookie_files = glob.glob('cookies.pkl')
if len(cookie_files) > 0:
    find_cookie = True

login_with_cookie = False
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "./chromedriver" # Your Chrome Driver path
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

def wait_for_new_window(driver, timeout=10):
    handles_before = driver.window_handles
    yield
    WebDriverWait(driver, timeout).until(
        lambda driver: len(handles_before) != len(driver.window_handles))

# while(not login_with_cookie):
#     # 쿠키 정보를 이용해 로그인
#     if find_cookie:
#         # driver = webdriver.Chrome("./chromedriver")
#         cookies = pickle.load(open("cookies.pkl", "rb"))
#         # driver.get("https://www.shop.co.kr/front/theshop/main/main")
#         for cookie in cookies:
#             driver.add_cookie(cookie)
#         # driver.get("https://www.shop.co.kr/front/theshop/main/main")
#         login_with_cookie = True
#     else:
#         driver = webdriver.Chrome("./chromedriver")
#         # driver.get("https://www.shop.co.kr/front/theshop/main/main")
#         while(not find_cookie):
#             cookies = driver.get_cookies()
#             if len(cookies)>0:
#                 find_cookie = True
#         pickle.dump(cookies , open("cookies.pkl","wb"))
#         driver.close()
#         driver.quit()

def baro1():
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    # driver.get("https://www.baropharm.com/order")
    # last_tab = driver.window_handles[-1]
    # driver.switch_to.window(window_name=last_tab)
    money = int(driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[1]/div').text.replace(',','').replace('원','')) - int(driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[2]/div/span').text.replace('원','').replace(',','').replace('-','').replace(' ',''))- 5999
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').send_keys(money)
    #바로결제 카드 클릭
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[1]/ul/li[1]/div/label/div[2]/div[1]/div/div').click()
    #더모아 1 선택
    driver.find_element(By.XPATH, '/html/body/div[51]/ol/li[2]/button').click()
    #결제버튼 누르기
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/button/span').click()
    #결제확인 버튼
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
#바로팜 간편 결제2
def baro2():
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    money = int(driver.find_element(By.XPATH,'//*[@id="popupbaromall_payment"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td/div/p/strong').text.replace('원', '').replace(',', '')) - 5999
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').send_keys(money)
    #바로결제 카드 클릭
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[1]/ul/li[1]/div/label/div[2]/div[1]/div/div').click()
    #더모아 2 선택
    driver.find_element(By.XPATH, '/html/body/div[51]/ol/li[1]/button').click()
    #결제버튼 누르기
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/button/span').click()
    #결제확인 버튼
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()

#바로팜 일반 카드1
def barocard1():
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    #5999세팅
    money = int(driver.find_element(By.XPATH,'//*[@id="popupbaromall_payment"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td/div/p/strong').text.replace('원', '').replace(',', '')) - 5999
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').send_keys(money)

    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    #일반신용카드
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[1]/ul/li[6]/div/label/span[1]').click()
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/button/span').click()
    #결제확인
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
    print('통과')
    #대기
    wait_for_new_window(driver, timeout=10)
    print('새창 확인')

    while True:
        print('새창 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.ID, 'POQ_CARDCODE')))
            print('새창통과')
            break
        except:
            print('새창통과못함')

    #대기

    driver.find_element(By.XPATH, '//*[@id="POQ_CARDCODE"]/option[6]').click()
    driver.find_element(By.XPATH, '//*[@id="contents"]/div/div[5]/ul/li[2]/label').click()
    driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span[2]/a').click()
    #대기
    while True:
        print('프레임 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            driver.switch_to.frame('HiddenArea')
            print('프레임 전환 통과')
            break
        except:
            print('프레임 통과못함')
    while True:
        print('카드결제 클릭')
        try:
            driver.find_element(By.CLASS_NAME, 'card-btn').click()
            print('카드클릭 통과')
            break
        except:
            print('카드클릭 통과못함')

    while True:
        print('카드1결제 클릭')
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/form/div[3]/div[2]/div[2]/div[1]/div/div/button/span').click()
            print('카드1클릭 통과')
            break
        except:
            print('카드1클릭 통과못함')
    #대기

    driver.find_element(By.XPATH, '//*[@id="card"]/ul/li[1]/button').click()  # 카드1
    # driver.find_element(By.XPATH,'//*[@id="card"]/ul/li[2]/button').click() #카드2
    driver.find_element(By.ID, 'app_pwd').click()
    # 비밀번호 입력타임

    while True:
        print('마무리 클릭')
        try:
            driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li/label').click()
            driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span/a').click()
            print('마무리 통과')
            break
        except:
            print('마무리 통과못함')
#바로팜 일반 카드2
def barocard2():
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    #5999세팅
    money = int(driver.find_element(By.XPATH,'//*[@id="popupbaromall_payment"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td/div/p/strong').text.replace('원', '').replace(',', '')) - 5999
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').send_keys(money)

    #일반신용카드
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[1]/ul/li[6]/div/label/span[1]').click()
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/button/span').click()
    #결제확인
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
    print('통과')
    #대기
    wait_for_new_window(driver, timeout=10)
    print('새창 확인')

    while True:
        print('새창 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.ID, 'POQ_CARDCODE')))
            print('새창통과')
            break
        except:
            print('새창통과못함')

    #대기

    driver.find_element(By.XPATH, '//*[@id="POQ_CARDCODE"]/option[6]').click()
    driver.find_element(By.XPATH, '//*[@id="contents"]/div/div[5]/ul/li[2]/label').click()
    driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span[2]/a').click()
    #대기
    while True:
        print('프레임 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            driver.switch_to.frame('HiddenArea')
            print('프레임 전환 통과')
            break
        except:
            print('프레임 통과못함')
    while True:
        print('카드결제 클릭')
        try:
            driver.find_element(By.CLASS_NAME, 'card-btn').click()
            print('카드클릭 통과')
            break
        except:
            print('카드클릭 통과못함')

    while True:
        print('카드1결제 클릭')
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/form/div[3]/div[2]/div[2]/div[1]/div/div/button/span').click()
            print('카드1클릭 통과')
            break
        except:
            print('카드1클릭 통과못함')
    #대기

    #driver.find_element(By.XPATH, '//*[@id="card"]/ul/li[1]/button').click()  # 카드1
    driver.find_element(By.XPATH,'//*[@id="card"]/ul/li[2]/button').click() #카드2
    driver.find_element(By.ID, 'app_pwd').click()

    #비밀번호 입력시간

    #확인후 넘기기
    while True:
        print('마무리 클릭')
        try:
            driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li/label').click()
            driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span/a').click()
            print('마무리 통과')
            break
        except:
            print('마무리 통과못함')
#바로팜 네이버 카드1
def baronaver1():
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    #5999세팅
    money = int(driver.find_element(By.XPATH,'//*[@id="popupbaromall_payment"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td/div/p/strong').text.replace('원', '').replace(',', '')) - 5999
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').send_keys(money)

    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/ul/li[2]/label/img').click()
    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
    # driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
    #네이버페이 클릭
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[1]/ul/li[4]/div/label/span').click()
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/button/span').click()
    #결제확인
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
    while True:
        print('새창 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/ul[2]/li[1]/label')))
            print('새창통과')
            break
        except:
            print('새창통과못함')
    driver.find_element(By.XPATH, '//*[@id="content"]/div/ul[2]/li[1]/label').click()
    driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span[2]/a').click()
    #카드선택 - 기존 선택 유지(1번 우선)
    # driver.find_element(By.XPATH, '//*[@id="anext"]').click()
    #결제
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/a[1]').click()
    #비번 입력타임
    #결제 확인
    WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div/ul/li/label')))
    driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li/label').click()
    driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span/a').click()
#바로팜 네이버 카드2
def baronaver2():
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)

    #5999세팅

    money = int(driver.find_element(By.XPATH,'//*[@id="popupbaromall_payment"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td/div/p/strong').text.replace('원', '').replace(',', '')) - 5999
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').send_keys(money)

    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/ul/li[2]/label/img').click()
    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
    # driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
    #네이버페이 클릭
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[1]/ul/li[4]/div/label/span').click()
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/button/span').click()
    #결제확인
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
    while True:
        print('새창 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/ul[2]/li[1]/label')))
            print('새창통과')
            break
        except:
            print('새창통과못함')
    driver.find_element(By.XPATH, '//*[@id="content"]/div/ul[2]/li[1]/label').click()
    driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span[2]/a').click()
    #카드선택 - 2번카드 선택
    driver.find_element(By.XPATH, '//*[@id="anext"]').click()
    #결제
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/a[1]').click()
    #비번 입력타임
    #결제 확인
    while True:
        print('결제완료 전환')
        try:
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/ul/li/label')))
            print('결제완료 통과')
            break
        except:
            print('결제완료 통과못함')

    WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div/ul/li/label')))
    driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li/label').click()
    driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span/a').click()
#바로팜 카카오 카드
def barokakao():
    #5999 세팅
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    money = int(driver.find_element(By.XPATH,'//*[@id="popupbaromall_payment"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td/div/p/strong').text.replace('원', '').replace(',', '')) - 5999
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').send_keys(money)

    #카카오페이 클릭
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[1]/ul/li[5]/div/label/span').click()
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/button/span').click()
    #결제확인
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()

    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    # driver.find_element(By.XPATH,
    #                     '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/ul/li[3]/label/img').click()
    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
    # driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
    while True:
        print('새창 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/ul/li[1]/label')))
            print('새창통과')
            break
        except:
            print('새창통과못함')
    driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/label').click()
    driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span[2]/a').click()
#바로팜 페이코1
def baropayco1():
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    #5999세팅
    money = int(driver.find_element(By.XPATH,'//*[@id="popupbaromall_payment"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td/div/p/strong').text.replace('원', '').replace(',', '')) - 5999
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').send_keys(money)

    #페이코 클릭
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[1]/ul/li[2]/div/label/span').click()
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/button/span').click()
    #결제확인
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    # driver.find_element(By.XPATH,
    #                     '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/ul/li[4]/label/img').click()
    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
    # driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
    while True:
        print('새창 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contents"]/div[1]/ul/li[1]/label')))
            print('새창통과')
            break
        except:
            print('새창통과못함')

    driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/ul/li[1]/label').click()
    driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span[2]/a').click()
    while True:
        print('새창 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pgCardList_nextBtn"]/span')))
            print('새창통과')
            break
        except:
            print('새창통과못함')

    #카드선택
    driver.find_element(By.XPATH, '//*[@id="pgCardList_nextBtn"]/span').click()
    driver.find_element(By.XPATH, '//*[@id="pgCardList_nextBtn"]/span').click()
    #두번 가야 카드1
    driver.find_element(By.XPATH, '//*[@id="btnPayment"]').click()
    #비밀번호 타임
    while True:
        print('새창 완료 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/ul/li[1]/label').click()
            driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span[2]/a').click()
            print('완료 통과')
            break
        except:
            print('완료통과못함')
#바로팜 페이코2
def baropayco2():
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    # 5999세팅
    money = int(driver.find_element(By.XPATH,
                                    '//*[@id="popupbaromall_payment"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td/div/p/strong').text.replace(
        '원', '').replace(',', '')) - 5999
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').send_keys(
        money)

    #페이코 클릭
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[1]/ul/li[2]/div/label/span').click()
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/button/span').click()
    #결제확인
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    # driver.find_element(By.XPATH,
    #                     '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/ul/li[4]/label/img').click()
    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
    # driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
    while True:
        print('새창 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="contents"]/div[1]/ul/li[1]/label')))
            print('새창통과')
            break
        except:
            print('새창통과못함')

    driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/ul/li[1]/label').click()
    driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span[2]/a').click()
    while True:
        print('새창 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pgCardList_nextBtn"]/span')))
            print('새창통과')
            break
        except:
            print('새창통과못함')

    # 카드선택
    driver.find_element(By.XPATH, '//*[@id="pgCardList_nextBtn"]/span').click()
    # driver.find_element(By.XPATH, '//*[@id="pgCardList_nextBtn"]/span').click()
    # 두번 가야 카드1
    driver.find_element(By.XPATH, '//*[@id="btnPayment"]').click()
    # 비밀번호 타임

    # 완료
    while True:
        print('새창 완료 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/ul/li[1]/label').click()
            driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span[2]/a').click()
            print('완료 통과')
            break
        except:
            print('완료통과못함')
#바로팜 쓱페이1
def barossg():
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    #5999세팅
    money = int(driver.find_element(By.XPATH,'//*[@id="popupbaromall_payment"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td/div/p/strong').text.replace('원', '').replace(',', '')) - 5999
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').send_keys(money)

    # 쓱페이클릭
    driver.find_element(By.XPATH,
                        '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[1]/ul/li[3]/div/label/span').click()
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/button/span').click()
    #결제확인
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()

    # driver.find_element(By.XPATH,
    #                     '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/ul/li[5]/label/img').click()
    # driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
    # driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()

    while True:
        print('새창 전환')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        try:
            WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.ID, 'mobileno')))
            print('새창통과')
            break
        except:
            print('새창통과못함')
    driver.find_element(By.ID, 'mobileno').send_keys('01030333304')
    driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/ul/li[1]/label').click()
    driver.find_element(By.XPATH, '//*[@id="footer"]/div/div/div/span[2]/a').click()
