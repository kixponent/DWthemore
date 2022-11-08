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

while(not login_with_cookie):
    # 쿠키 정보를 이용해 로그인
    if find_cookie:
        # driver = webdriver.Chrome("./chromedriver")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        driver.get("https://www.shop.co.kr/front/theshop/main/main")
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://www.shop.co.kr/front/theshop/main/main")
        login_with_cookie = True
    else:
        driver = webdriver.Chrome("./chromedriver")
        driver.get("https://www.shop.co.kr/front/theshop/main/main")
        while(not find_cookie):
            cookies = driver.get_cookies()
            if len(cookies)>0:
                find_cookie = True
        pickle.dump(cookies , open("cookies.pkl","wb"))
        driver.close()
        driver.quit()

def hmp_simpay1():
    #주문 경고창
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    driver.find_element(By.XPATH, '//*[@id="purchaseM1button"]/button').click()
    driver.switch_to.alert.accept()
    while True:
        print('새창 전환')
        try:
            money = int(driver.find_element(By.XPATH, '//*[@id="paymentAmountDd"]').text.replace(',', '')) - 5999
            driver.find_element(By.XPATH, '//*[@id="hMoneyUseAmount"]').send_keys(money)
            print('새창통과')
            break
        except:
            print('새창통과못함')
    #더모아 세팅


    #간편카드1

    driver.find_element(By.XPATH, '//*[@id="b_pay0001"]').click()
    driver.find_element(By.XPATH,'//*[@id="210706498010220B|210706498010180B|CCLG"]').click()
    driver.find_element(By.XPATH, '//*[@id="smartInstallment"]/option[2]').click()
    driver.find_element(By.XPATH, '//*[@id="imgPaymentPay"]').click()

    driver.switch_to.alert.accept()
def hmp_simpay2():
    #주문 경고창
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    driver.find_element(By.XPATH, '//*[@id="purchaseM1button"]/button').click()
    driver.switch_to.alert.accept()
    while True:
        print('새창 전환')
        try:
            money = int(driver.find_element(By.XPATH, '//*[@id="paymentAmountDd"]').text.replace(',', '')) - 5999
            driver.find_element(By.XPATH, '//*[@id="hMoneyUseAmount"]').send_keys(money)
            print('새창통과')
            break
        except:
            print('새창통과못함')
    #더모아 세팅


    #간편카드1

    driver.find_element(By.XPATH, '//*[@id="b_pay0001"]').click()
    driver.find_element(By.XPATH,'//*[@id="21070849875857F9|21070849875856F9|CCLG"]').click()
    driver.find_element(By.XPATH, '//*[@id="smartInstallment"]/option[2]').click()
    driver.find_element(By.XPATH, '//*[@id="imgPaymentPay"]').click()

    driver.switch_to.alert.accept()
def hmp_card1():
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    driver.find_element(By.XPATH, '//*[@id="purchaseM1button"]/button').click()
    driver.switch_to.alert.accept()
    while True:
        print('새창 전환')
        try:
            money = int(driver.find_element(By.XPATH, '//*[@id="paymentAmountDd"]').text.replace(',', '')) - 5999
            driver.find_element(By.XPATH, '//*[@id="hMoneyUseAmount"]').send_keys(money)
            print('새창통과')
            break
        except:
            print('새창통과못함')
    #더모아 세팅
    driver.find_element(By.XPATH, '//*[@id="b_pay0002"]').click()
    driver.find_element(By.XPATH, '//*[@id="cardSelect"]/option[6]').click()
    driver.find_element(By.XPATH, '//*[@id="cardInstallment"]/option[2]').click()
    driver.find_element(By.XPATH, '//*[@id="imgPaymentPay"]').click()
    #대기
    while True:
        print('경고 전환')
        try:
            driver.switch_to.alert.accept()
            print('경고 통과')
            break
        except:
            print('경고 못함')


    #결제 페이누름
    while True:
        print('페이결제클릭')
        try:
            driver.switch_to.frame('MPI_cert')
            print('페이결제 통과')
            break
        except:
            print('페이결제 못함')
    # WebDriverWait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'MPI_cert')))
    #
    #대기
    while True:
        print('페이결제 이후')
        try:
            driver.find_element(By.XPATH, '//*[@id="fanView"]/div[3]/div[2]/div/a').click()
            print('페이결제 이후 통과')
            break
        except:
            print('페이결제 이후 못함')

    #카드선택
    while True:
        print('카드선택')
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/form/div[3]/div[2]/div[2]/div[1]/div/div/button/span').click()
            driver.find_element(By.XPATH, '//*[@id="card"]/ul/li[2]/button').click()
            print('카드선택 통과')
            break
        except:
            print('카드선택 못함')

    #비밀번호 누르기
    driver.find_element(By.XPATH, '//*[@id="app_pwd"]').click()

    #비밀번호 타임

    #결제완료
def hmp_card2():
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    driver.find_element(By.XPATH, '//*[@id="purchaseM1button"]/button').click()
    driver.switch_to.alert.accept()
    while True:
        print('새창 전환')
        try:
            money = int(driver.find_element(By.XPATH, '//*[@id="paymentAmountDd"]').text.replace(',', '')) - 5999
            driver.find_element(By.XPATH, '//*[@id="hMoneyUseAmount"]').send_keys(money)
            print('새창통과')
            break
        except:
            print('새창통과못함')
    #더모아 세팅
    driver.find_element(By.XPATH, '//*[@id="b_pay0002"]').click()
    driver.find_element(By.XPATH, '//*[@id="cardSelect"]/option[6]').click()
    driver.find_element(By.XPATH, '//*[@id="cardInstallment"]/option[2]').click()
    driver.find_element(By.XPATH, '//*[@id="imgPaymentPay"]').click()
    #대기
    while True:
        print('경고 전환')
        try:
            driver.switch_to.alert.accept()
            print('경고 통과')
            break
        except:
            print('경고 못함')


    #결제 페이누름
    while True:
        print('페이결제클릭')
        try:
            driver.switch_to.frame('MPI_cert')
            print('페이결제 통과')
            break
        except:
            print('페이결제 못함')
    # WebDriverWait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'MPI_cert')))
    #
    #대기
    while True:
        print('페이결제 이후')
        try:
            driver.find_element(By.XPATH, '//*[@id="fanView"]/div[3]/div[2]/div/a').click()
            print('페이결제 이후 통과')
            break
        except:
            print('페이결제 이후 못함')

    #카드선택
    while True:
        print('카드선택')
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/form/div[3]/div[2]/div[2]/div[1]/div/div/button/span').click()
            driver.find_element(By.XPATH, '//*[@id="card"]/ul/li[1]/button').click()
            print('카드선택 통과')
            break
        except:
            print('카드선택 못함')

    #비밀번호 누르기
    driver.find_element(By.XPATH, '//*[@id="app_pwd"]').click()

    #비밀번호 타임

    #결제완료
