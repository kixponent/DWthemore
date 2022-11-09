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
#         driver.get("https://www.shop.co.kr/front/theshop/main/main")
#         for cookie in cookies:
#             driver.add_cookie(cookie)
#         driver.get("https://www.shop.co.kr/front/theshop/main/main")
#         login_with_cookie = True
#     else:
#         driver = webdriver.Chrome("./chromedriver")
#         driver.get("https://www.shop.co.kr/front/theshop/main/main")
#         while(not find_cookie):
#             cookies = driver.get_cookies()
#             if len(cookies)>0:
#                 find_cookie = True
#         pickle.dump(cookies , open("cookies.pkl","wb"))
#         driver.close()
#         driver.quit()
## 대웅 메인화면 & 로그인 ##
def login(dwid, dwpw):
    #hm2021, gmlakd!2021
    driver.find_element(By.ID,'userId').send_keys(dwid)
    driver.find_element(By.ID, 'userPwd').send_keys(dwpw,Keys.RETURN)
## 기존 장바구니 비우기 ##
def clearbag():
    driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[2]/div/a[4]').click()
    driver.find_element(By.CLASS_NAME, "btn_empty").click()
    while True:
        try:
            driver.switch_to.alert.accept()
            print('비우기 경고창1')
            break
        except:
            pass
    while True:
        try:
            driver.switch_to.alert.accept()
            print('비우기 경고창1')
            break
        except:
            pass
## 다이아벡스 검색 & 담기 ##
def diabex():
    print('다이아벡스검색')
    while True:
        try:
            driver.find_element(By.ID,'header_searchVal').send_keys("다이아벡스",Keys.RETURN)
            break
        except:
            try:
                driver.find_element(By.XPATH, '//*[@id="autoCompleteText"]').clear()
                driver.find_element(By.XPATH, '//*[@id="autoCompleteText"]').send_keys('다이아벡스', Keys.RETURN)
                break
            except:
                pass
    WebDriverWait(driver,timeout=5).until(EC.presence_of_element_located((By.ID,'h2_search_title')))
#driver.find_element(By.ID,'autoCompleteText').send_keys("다이아벡스",Keys.RETURN)
def diabex250():
    print('250 하는중')
    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID,"search_li_64540")))
    #다이아벡스 250mg 100정 + 30정
    #다이아벡스 250mg 100정
    driver.find_element(By.ID, "search_li_64540").click()
    driver.find_element(By.ID, "btn_cartInsert").click()
    try:
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
    except:
        pass
    try:
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
    except:
        pass
    #다이아벡스 250mg 30정
    driver.find_element(By.ID, "search_li_64264").click()
    driver.find_element(By.ID, "btn_cartInsert").click()
    try:
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
    except:
        pass
    try:
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
    except:
        pass
def diabex500():
    #다이아벡스 500mg 100정
    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID,"search_li_64258")))
    driver.find_element(By.ID, "search_li_64258").click()
    driver.find_element(By.ID, "btn_cartInsert").click()
    try:
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
    except:
        pass
    try:
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
    except:
        pass

def diabex500x3():
    #다이아벡스 500mg 30정 x 3
    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID,"search_li_64375")))
    driver.find_element(By.ID, "search_li_64375").click()
    driver.find_element(By.ID, "button_plus").click()
    driver.find_element(By.ID, "button_plus").click()
    driver.find_element(By.ID, "btn_cartInsert").click()
    try:
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
    except:
        pass
    try:
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
    except:
        pass

def diabex1000():
    #다이아벡스 1000mg 100정
    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID,"search_li_64546")))
    driver.find_element(By.ID, "search_li_64546").click()
    driver.find_element(By.ID, "btn_cartInsert").click()
    while True:
        try:
            driver.switch_to.alert.accept()
            print('다이아벡스 1000 경고창 1')
            break
        except:
            pass
    while True:
        try:
            driver.switch_to.alert.accept()
            print('다이아벡스 1000 경고창 2')
            break
        except:
            pass
    try:
        driver.switch_to.alert.accept()
        print('다이아벡스 1000 경고창 3')
    except:
        pass
def diabex1000x2():
    #다이아벡스 1000mg 30정 x 2
    WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID,"search_li_64385")))
    driver.find_element(By.ID, "search_li_64385").click()
    driver.find_element(By.ID, "button_plus").click()
    driver.find_element(By.ID, "btn_cartInsert").click()
    try:
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
    except:
        pass
    try:
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
    except:
        pass

## 장바구니 결제 ##
# 장바구니로 이동
def gocart():
    print('장바구니 하는중')
    while True:
        try:
            driver.find_element(By.CLASS_NAME, "btn_cartlist").click()
            break
        except:
            pass
        try:
            driver.find_element(By.CLASS_NAME, "btn_cart").click()
            break
        except:
            pass
# 다이아벡스 외의 담긴것 확인 및 제외 (금액이 12000원 이하, 6000원 이상인지 체크하는것으로 메커니즘 변경)
    total = int(driver.find_element(By.ID, "totCartOrderSum").text.replace(",",""))
    money = int(driver.find_element(By.ID, "btn-deposit-chk").text.replace(",", ""))
    if total > 12000:
        driver.find_element(By.CLASS_NAME,"btn_empty").click()
        try:
            driver.switch_to.alert.accept()
            driver.switch_to.alert.accept()
            driver.switch_to.alert.accept()
        except:
            pass
    elif total < 6000:
        driver.find_element(By.CLASS_NAME,"btn_empty").click()
        try:
            driver.switch_to.alert.accept()
            driver.switch_to.alert.accept()
            driver.switch_to.alert.accept()
        except:
            pass
        # 필요 예치금 확인 (10000원이상 동작)
    elif money < 10000:
        return()


# 예치금 충분한지 확인

#  더모아 준비
def themoreready():
    driver.execute_script("window.scrollTo(0, 500)")
    while True:
        try:
            try:
                driver.find_element(By.ID,"goOrderSubmit").click()
                print('주문하기1 찾음')
                break
            except:
                driver.find_element(By.ID, "goOrder").click()
                print('주문하기2 찾음')
                break
        except:
            pass
    while True:
        try:
            totalmoney = int(driver.find_element(By.ID,"totalOrderPrice").get_property('value').replace(",",""))
            themoremoney = totalmoney-5999
            driver.find_element(By.ID,"reserveAmt").send_keys(themoremoney)
            driver.find_element(By.ID,"useReserveAmtBtn").click()
            print('예치금 사용 찾음')
            break
        except:
            pass

# 간편결제 더모아1
def themore1():
    driver.find_element(By.XPATH,'//*[@id="cardtype"]/option[5]').click()
    driver.find_element(By.XPATH,'//*[@id="payButtonDiv"]/div/button[1]').click()
    while True:
        try:
            driver.switch_to.alert.accept()
            print('더모아 알림창 찾음')
            break
        except:
            pass

# 간편결제 더모아2
def themore2():
    driver.find_element(By.XPATH,'//*[@id="cardtype"]/option[4]').click()
    driver.find_element(By.XPATH,'//*[@id="payButtonDiv"]/div/button[1]').click()
    while True:
        try:
            driver.switch_to.alert.accept()
            print('더모아 알림창 찾음')
            break
        except:
            pass

# 일반결제 더모아1
def normore1():
    driver.find_element(By.ID, 'payMethod_card').click()
    driver.find_element(By.XPATH,'//*[@id="paymentCard"]/option[5]').click()
    driver.find_element(By.XPATH,'//*[@id="payButtonDiv"]/div/button[1]').click()

    # 결제 비밀번호 입력
    while True:
        try:
            driver.switch_to.frame('kiccFrame')
            print('간편결제 프레임1 찾음')
            break
        except:
            pass
    while True:
        try:
            driver.switch_to.frame('frame_content')
            print('간편결제 프레임2 찾음')
            break
        except:
            pass
    driver.execute_script('f_allCheck()')
    driver.execute_script('f_next()')
    driver.execute_script("f_select_card('029', '')")
    driver.execute_script('f_next()')

    driver.switch_to.parent_frame()
    driver.switch_to.frame('KICC_LAYER_TARGET')
    while True:
        try:
            driver.switch_to.frame('v3dframe')
            print('간편결제 프레임3 찾음')
            break
        except:
            pass

    # 간편결제 비밀번호 클릭
    driver.find_element(By.ID, 'app_pwd').click()

    # driver.find_element(By.XPATH, '//*[@id="fanView"]/div[2]/ul/li[2]/a').click()
    # driver.find_element(By.XPATH, '//*[@id="otherView"]/div[3]/ul/li[2]/a/span').click()
    return
    # while True:
    #     try:
    #         driver.find_element(By.XPATH, '//*[@id="fanView"]/div[3]/div[2]/div/a/span').click()
    #         break
    #     except:
    #         pass
    # ## 다른 결제 창이 겨지면
    # if driver.find_element(By.CLASS_NAME)
    #     driver.switch_to.parent_frame()
    #     driver.switch_to.parent_frame()
    #     driver.switch_to.parent_frame()
    #     driver.switch_to.frame('kiccFrame')
    # else:
    # driver.find_element(By.XPATH,'//*[@id="KICC_CARD_POPUP_CLOSE"]/img').click()
    #
    # driver.find_element(By.XPATH, '//*[@id="app_pwd"]').click()
    # driver.maximize_window()
    # os.system('C:\\Users\\user\\PycharmProjects\\DWthemore\\passcheck.exe')
    #
    # # 비밀번호 입력 도전2
    # driver.switch_to.parent_frame()
    # driver.switch_to.parent_frame()
    # driver.switch_to.frame('kiccFrame')
    # driver.switch_to.frame('KICC_LAYER_TARGET')
    # driver.switch_to.frame('v3dframe')
    # key = driver.find_elements(By.CLASS_NAME, "kpd-data")
    # key[5].click()
    # key[2].click()
    # key[11].click()
    # key[4].click()
    # key[2].click()
    # key[6].click()
# 일반결제 더모아2
def normore2():
    driver.find_element(By.ID,'payMethod_card').click()
    driver.find_element(By.XPATH, '//*[@id="paymentCard"]/option[5]').click()
    driver.find_element(By.XPATH,'//*[@id="payButtonDiv"]/div/button[1]').click()

def initial():
    back()
# 결제 비밀번호 입력

# 메인으로 복귀
def back():
    driver.get("https://www.shop.co.kr/front/theshop/main/main")
    cookies = driver.get_cookies()
    if len(cookies) > 0:
        find_cookie = True
    pickle.dump(cookies, open("cookies.pkl", "wb"))

def test(dose,unit,card):
    while True:
        try:
            diabex()
            break
        except:
            print('오류발생')
            pass
    while True:
        try:
            if dose == 250:
                diabex250()

            elif dose == 500:
                if unit == 30:
                    diabex500x3()
                    break
                elif unit == 100:
                    diabex500()
                    break
                else:
                    print('다이아벡스 500 단위 오류')
                    break
            elif dose == 1000:
                if unit == 30:
                    diabex1000x2()
                    break
                elif unit == 100:
                    diabex1000()
                    break
                else:
                    print('다이아벡스 1000 단위 오류')
                    break
            else:
                print('다이아벡스 용량 오류')
                break
        except:
            pass
    while True:
        try:
            gocart()
            break
        except:
            pass
    while True:
        try:
            themoreready()
            break
        except:
            pass

    if card == 'themore1':
        themore1()
        back()
    elif card == 'themore2':
        themore2()
        back()
    elif card == 'normore':
        normore1()
    else:
        print('카드입력오류')
    return('완료')
    #test(250 500 1000,30 100,themore12 normore)
    #test(1000,30,'themore1')