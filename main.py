## 대웅 메인화면 & 로그인 ##
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def login(dwid, dwpw):
    #hm2021, gmlakd!2021
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://www.shop.co.kr/front/theshop/main/main")

    driver.find_element(By.ID,'userId').send_keys(dwid)
    driver.find_element(By.ID, 'userPwd').send_keys(dwpw,Keys.RETURN)

## 다이아벡스 검색 & 담기 ##

    driver.find_element(By.ID,'header_searchVal').send_keys("다이아벡스",Keys.RETURN)

    #다이아벡스 250mg 100정 + 30정
    driver.find_element(By.ID, "search_li_64258").click()
    driver.find_element(By.ID, "btn_cartInsert").click()
    driver.switch_to.alert.accept()
    driver.switch_to.alert.accept()

    #다이아벡스 500mg 100정
    driver.find_element(By.ID, "search_li_64258").click()
    driver.find_element(By.ID, "btn_cartInsert").click()
    driver.switch_to.alert.accept()
    driver.switch_to.alert.accept()

    #다이아벡스 1000mg 100정
    driver.find_element(By.ID, "search_li_64546").click()
    driver.find_element(By.ID, "btn_cartInsert").click()
    driver.switch_to.alert.accept()
    driver.switch_to.alert.accept()

    #다이아벡스 1000mg 30정 x 2
    driver.find_element(By.ID, "search_li_64385").click()
    driver.find_element(By.ID, "button_plus").click()
    driver.find_element(By.ID, "btn_cartInsert").click()
    driver.switch_to.alert.accept()
    driver.switch_to.alert.accept()
## 장바구니 결제 ##
# 장바구니로 이동
    driver.find_element(By.CLASS_NAME, "btn_cartlist").click()
# 다이아벡스 외의 담긴것 확인 및 제외 (금액이 12000원 이하인지 체크하는것으로 메커니즘 변경)
    total = int(driver.find_element(By.ID, "totCartOrderSum").text.replace(",",""))
    money = int(driver.find_element(By.ID, "btn-deposit-chk").text.replace(",", ""))
    if total > 12000:
        driver.find_element(By.CLASS_NAME,"btn_empty").click()
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
        # 필요 예치금 확인 (10000원이상 동작)
    elif money < 10000:
        return()


# 예치금 충분한지 확인

# 간편결제 더모아1
# 간편결제 더모아2
# 일반결제 더모아1
 # 결제 비밀번호 입력
# 일반결제 더모아2
 # 결제 비밀번호 입력
