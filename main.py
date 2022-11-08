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



# 팜페이 사이트 결제
def pharmpay(ppid,pppw):
    # driver.get("http://my.pharmpay.co.kr/pur/login/login.html")
    driver.find_element(By.ID,'my_pur_taxno').send_keys('5290801603') #ppid
    driver.find_element(By.ID, 'my_pur_pw').send_keys('01603',Keys.RETURN) #pppw
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
    # while True:
    #     try:
    #         print('거래처 옵션 버튼 누르기')
    #         driver.find_element(By.NAME,'2298116607').click()
    #         print('거래처 옵션 버튼 누름')
    #         break
    #     except:
    #         print('신용카드 버튼 누르기 실패')

    driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[2]/td[2]/select/option[3]').click()
    driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[3]/td[2]/input').send_keys('5999')
    #카드1
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[1]').send_keys('9410')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[2]').send_keys('6186')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[3]').send_keys('4696')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[4]').send_keys('6220')
    #유효기간
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[1]/option[8]').click()
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[2]/option[6]').click()
    #일시불
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[4]/select/option[2]').click()
    #약관동의
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[3]/button[1]/i').click()
    while True:
        try:
            print('거래처 옵션 버튼 누르기')
            driver.find_element(By.NAME,'2298116607').click()
            print('거래처 옵션 버튼 누름')
            break
        except:
            print('신용카드 버튼 누르기 실패')

    #결제하기
    driver.find_element(By.CLASS_NAME, 'btn btn-primary btn_payment btn_now_pay').click()
    ##지오팜 카드2
    while True:
        try:
            print('신용카드 버튼 누르기')
            driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[2]/div/button[2]').click()
            print('신용카드 버튼 누름')
            break
        except:
            print('신용카드 버튼 누르기 실패')
    ##지오팜 카드2
    #지오팜
    while True:
        try:
            print('거래처 옵션 누르기')
            driver.find_element(By.NAME,'2298116607').click()
            print('거래처 옵션 누름')
            break
        except:
            print('거래처 옵션 누르기 실패')
    driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[2]/td[2]/select/option[3]').click()
    driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[3]/td[2]/input').send_keys('5999')
    #카드1
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[1]').send_keys('9410')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[2]').send_keys('6186')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[3]').send_keys('4704')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[4]').send_keys('6626')
    #유효기간
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[1]/option[8]').click()
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[2]/option[6]').click()
    #일시불
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[4]/select/option[2]').click()
    #약관동의
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[3]/button[1]/i').click()
    while True:
        try:
            print('거래처 옵션 누르기')
            driver.find_element(By.NAME,'2298116607').click()
            print('거래처 옵션 누름')
            break
        except:
            print('거래처 옵션 누르기 실패')
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[4]/td[2]/button').click()
    #훼밀리팜
    while True:
        try:
            print('신용카드 버튼 누르기')
            driver.find_element(By.NAME,'//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[2]/div/button[2]').click()
            print('신용카드 버튼 누름')
            break
        except:
            print('신용카드 버튼 누르기 실패')
    while True:
        try:
            driver.find_element(By.NAME, '1408135543').click()
            print('회사 버튼 누름')
            break
        except:
            print('회사 버튼 누르기 실패')

    print('카드 회사 누름')
    driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[3]/td[2]/input').send_keys('5999')
    print('5999입력')
    #카드1
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[1]').send_keys('9410')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[2]').send_keys('6186')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[3]').send_keys('4696')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[4]').send_keys('6220')
    #유효기간
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[1]/option[8]').click()
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[2]/option[6]').click()
    #일시불
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[4]/select/option[2]').click()
    #약관동의
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[3]/button[1]/i').click()
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[4]/td[2]/button').click()

    ##훼밀리 카드2
    while True:
        try:
            print('신용카드 버튼 누르기')
            driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[2]/div/button[2]').click()
            print('신용카드 버튼 누름')
            break
        except:
            print('신용카드 버튼 누르기 실패')
    while True:
        try:
            driver.find_element(By.NAME, '1408135543').click()
            print('회사 버튼 누름')
            break
        except:
            print('회사 버튼 누르기 실패')

    print('카드 회사 누름')
    driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[3]/td[2]/input').send_keys('5999')
    print('5999입력')
    #카드2
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[1]').send_keys('9410')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[2]').send_keys('6186')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[3]').send_keys('4704')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[4]').send_keys('6626')
    #유효기간
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[1]/option[8]').click()
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[2]/option[6]').click()
    #일시불
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[4]/select/option[2]').click()
    #약관동의
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[3]/button[1]/i').click()
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[4]/td[2]/button').click()
    #레아팜 카드1
    while True:
        try:
            print('신용카드 버튼 누르기')
            driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[2]/div/button[2]').click()
            print('신용카드 버튼 누름')
            break
        except:
            print('신용카드 버튼 누르기 실패')
    while True:
        try:
            driver.find_element(By.NAME, '5128126399').click()
            print('회사 버튼 누름')
            break
        except:
            print('회사 버튼 누르기 실패')

    print('카드 회사 누름')
    driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[3]/td[2]/input').send_keys('5999')
    print('5999입력')
    #카드1
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[1]').send_keys('9410')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[2]').send_keys('6186')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[3]').send_keys('4696')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[4]').send_keys('6220')
    #유효기간
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[1]/option[8]').click()
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[2]/option[6]').click()
    #일시불
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[4]/select/option[2]').click()
    #약관동의
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[3]/button[1]/i').click()
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[4]/td[2]/button').click()
    #레아팜 카드2
    while True:
        try:
            print('신용카드 버튼 누르기')
            driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[2]/div/button[2]').click()
            print('신용카드 버튼 누름')
            break
        except:
            print('신용카드 버튼 누르기 실패')
    while True:
        try:
            driver.find_element(By.NAME, '5128126399').click()
            print('회사 버튼 누름')
            break
        except:
            print('회사 버튼 누르기 실패')

    print('카드 회사 누름')
    driver.find_element(By.XPATH,'//*[@id="right_content"]/div[1]/table/tbody/tr[3]/td[2]/input').send_keys('5999')
    print('5999입력')
    #카드2
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[1]').send_keys('9410')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[2]').send_keys('6186')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[3]').send_keys('4704')
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[5]/td[2]/input[4]').send_keys('6626')
    #유효기간
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[1]/option[8]').click()
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[2]/select[2]/option[6]').click()
    #일시불
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[6]/td[4]/select/option[2]').click()
    #약관동의
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[3]/button[1]/i').click()
    #결제하기
    driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[4]/td[2]/button').click()
    #pharmpay('5290801603','01603')

# 레아팜 결제

# 바로팜 간편 결제1
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
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/div[1]/div/div/button').click()
    #더모아 1 선택
    driver.find_element(By.XPATH, '/html/body/div[51]/ol/li[2]/button').click()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
#바로팜 간편 결제2
def baro2():
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    money = int(driver.find_element(By.XPATH,'//*[@id="popupbaromall_payment"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td/div/p/strong').text.replace('원', '').replace(',', '')) - 5999

    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').send_keys(money)
    #바로결제 카드 클릭
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/div[1]/div/div/button').click()
    #더모아 2 선택
    driver.find_element(By.XPATH, '/html/body/div[51]/ol/li[1]/button').click()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
#바로팜 일반 카드1
def barocard1():
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    #5999세팅
    money = int(driver.find_element(By.XPATH,'//*[@id="popupbaromall_payment"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td/div/p/strong').text.replace('원', '').replace(',', '')) - 5999
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[1]/ul/li[4]/div/input').send_keys(money)

    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
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

    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
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

    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/ul/li[2]/label/img').click()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
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

    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/ul/li[2]/label/img').click()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
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

    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    driver.find_element(By.XPATH,
                        '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/ul/li[3]/label/img').click()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
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

    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    driver.find_element(By.XPATH,
                        '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/ul/li[4]/label/img').click()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
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

    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    driver.find_element(By.XPATH,
                        '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/ul/li[4]/label/img').click()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()
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

    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[2]/div[2]/label/span').click()
    driver.find_element(By.XPATH,
                        '//*[@id="popupbaromall_payment"]/div/div[2]/div[2]/div[3]/ul/li[5]/label/img').click()
    driver.find_element(By.XPATH, '//*[@id="popupbaromall_payment"]/div/div[2]/div[3]/button/span').click()
    driver.find_element(By.XPATH, '/html/body/div[51]/div/div[3]/button[3]').click()

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

#레아팜 카드1 (request문으로 업글할것)
def Reapharm1():
    requests.get('http://bmpharm.co.kr/Login/incLogin.aspx?id=hm2021&pwd=gml!2021&s=0')


    driver.find_element(By.ID, 'txtid').send_keys('hm2021')
    driver.find_element(By.ID, 'txtPwd').send_keys('gml!2021', Keys.RETURN)
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="usrWosTop1_TblMenu"]/tbody/tr/td[8]/a').click()
            print('카드결제창 진입')
            break
        except:
            print('카드결제창 진입실패')
            pass
    driver.find_element(By.ID, 'card_no1').send_keys('9410')
    driver.find_element(By.ID, 'card_no2').send_keys('6186')
    driver.find_element(By.ID, 'card_no3').send_keys('4696')
    driver.find_element(By.ID, 'card_no4').send_keys('6220')
    driver.find_element(By.XPATH, '//*[@id="expire_mm"]/option[8]').click()
    driver.find_element(By.XPATH, '//*[@id="expire_yy"]/option[6]').click()
    driver.find_element(By.ID, 'EP_product_amt').send_keys('6109')
    driver.find_element(By.XPATH, '//*[@id="selRate"]/option[4]').click()
    driver.find_element(By.ID, 'btnCreadit').click()
    print('카드1 결제 끗')
#레아팜 카드2
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="usrWosTop1_TblMenu"]/tbody/tr/td[8]/a').click()
            print('카드결제창 진입')
            break
        except:
            pass
    driver.find_element(By.ID, 'card_no1').send_keys('9410')
    driver.find_element(By.ID, 'card_no2').send_keys('6186')
    driver.find_element(By.ID, 'card_no3').send_keys('4704')
    driver.find_element(By.ID, 'card_no4').send_keys('6626')
    driver.find_element(By.XPATH, '//*[@id="expire_mm"]/option[8]').click()
    driver.find_element(By.XPATH, '//*[@id="expire_yy"]/option[6]').click()
    driver.find_element(By.ID, 'EP_product_amt').send_keys('6109')
    driver.find_element(By.XPATH, '//*[@id="selRate"]/option[4]').click()
    driver.find_element(By.ID, 'btnCreadit').click()
    print('카드2 결제 끗')


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

# def pharmpay():
#     driver.get("http://my.pharmpay.co.kr/pur/login/login.html")
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "my_pur_taxno")))
#     driver.find_element(By.ID, "my_pur_taxno").send_keys("5290801603")
#     driver.find_element(By.ID, "my_pur_pw").send_keys("01603", Keys.RETURN)
#
#     driver.find_element(By.XPATH, '//*[@id="right_content"]/div[1]/table/tbody/tr[1]/td[2]/div/button[2]').click()
#     driver.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[3]/td[2]/input').send_keys('5999')
#
#     driver.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[5]/td[2]/input[1]').send_keys('9410')
#     driver.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[5]/td[2]/input[2]').send_keys('6186')
#     driver.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[5]/td[2]/input[3]').send_keys('4696')
#     driver.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[5]/td[2]/input[4]').send_keys('6220')


def dotest():
    diabex()
    diabex250()
    gocart()
    themoreready()
    themore1()
    back()
    diabex()
    diabex1000x2()
    gocart()
    themoreready()
    themore2()
    back()

def dotest1():
    diabex()
    diabex500()
    gocart()
    themoreready()
    normore1()

def dotest2():
    diabex()
    diabex1000()
    gocart()
    themoreready()
    normore1()

def test(dose,unit,card):
    diabex()
    if dose == 250:
        diabex250()

    elif dose == 500:
        if unit == 30:
            diabex500x3()
        elif unit == 100:
            diabex500()
        else:
            print('다이아벡스 500 단위 오류')
    elif dose == 1000:
        if unit == 30:
            diabex1000x2()
        elif unit == 100:
            diabex1000()
        else:
            print('다이아벡스 1000 단위 오류')
    else:
        print('다이아벡스 용량 오류')
    gocart()
    themoreready()
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