import time

from Config import start_fitto
from selenium.webdriver.common.by import By

#push테스트

#Intro > Swipe
time.sleep(5)
swipe =start_fitto.driver.swipe(908,828,195,828,0)
swipe =start_fitto.driver.swipe(908,828,195,828,0)
swipe =start_fitto.driver.swipe(908,828,195,828,0)
swipe =start_fitto.driver.swipe(195,828,908,828,0)
swipe =start_fitto.driver.swipe(195,828,908,828,0)
swipe =start_fitto.driver.swipe(195,828,908,828,0)



print("\n"
      "<로그인 flow 테스트>\n"
      "")
#로그인
#가입한 계정이 있어요 버튼 선택
time.sleep(5)
el =start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnHasAccount").click()

time.sleep(1)
el=start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/txtLoginTitle")
if el is not None and el.is_displayed():
      print("Case1: 가입한 계정이 있어요 버튼 동작 확인\n"
            "\033[34m"+"----->로그인 페이지 진입 성공"+"\033[0m")
else:
      print("Case1: 가입한 계정이 있어요 버튼 동작 확인\n"
            "\033[91m"+"----->로그인 페이지 진입 실패"+"\033[0m")


#로그인 페이지 X 버튼 동작 후 로그인 페이지 재 진입 확인
time.sleep(1)
el=start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptions").click()

time.sleep(1)
el=start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnHasAccount").click()

time.sleep(1)
el=start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/txtLoginTitle")
if el is not None and el.is_displayed():
      print("case2: 로그인 페이지 X 버튼 동작\n"
            "\033[34m"+"-----> 로그인 페이지 재 진입 성공"+"\033[0m")
else:
      print("case2: 로그인 페이지 X버튼 동작\n"
            "\033[91m"+"-----> 로그인 페이지 재 진입 실패"+"\033[0m")


#로그인 실패(가입되지 않은 이메일 정보 입력(이메일형식)+ PW 입력)
# 가입되지 않은 이메일 값 입력
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/actEmailAddress").send_keys("godgo4425+12354564@gmail.com")
# 아무 PW 값 입력
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/edtPassword").send_keys("qwer1234")
#로그인 버튼 선택
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnContinue").click()


time.sleep(1)
el = start_fitto.driver.find_element(By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.LinearLayout')
if el is not None and el.is_displayed():
      print("case3: 로그인 오류(가입X) dialog 생성 확인\n"
            "\033[34m"+"-----> Dialog 생성 성공"+"\033[0m")
else: print("case3: 로그인 오류(가입X) dialog 생성 확인\n"
            "\033[91m"+"-----> Dialog 생성 실패"+"\033[0m")

#에러창 확인 버튼 선택
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnTop").click()

#로그인 실패(기존 가입한 이메일 + 잘못된 PW 입력)
# 기존 가입한 이메일 값 입력
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/actEmailAddress").send_keys("shcho4242+888@gmail.com")
# 잘못된 PW 값 입력
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/edtPassword").send_keys("9875456132")
#로그인 버튼 선택
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnContinue").click()

time.sleep(1)
el = start_fitto.driver.find_element(By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.LinearLayout')
if el is not None and el.is_displayed():
      print("case4: 로그인 오류(PW 잘못 입력) dialog 생성 확인\n"
            "\033[34m"+"-----> Dialog 생성 성공"+"\033[0m")
else: print("case4: 로그인 오류(PW 잘못 입력) dialog 생성 확인\n"
            "\033[91m"+"-----> Dialog 생성 실패"+"\033[0m")

#에러창 확인 버튼 선택
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnTop").click()


#로그인 성공(정상)
# 기존 가입한 이메일 값 입력
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/actEmailAddress").send_keys("shcho4242+888@gmail.com")
# 기존 가입한 이메일에 맞는 정상 PW 값 입력
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/edtPassword").send_keys("qwer1234")
#로그인 버튼 선택
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnContinue").click()

#액세스 허용
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()

#건너뛰기 - summary 진입
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnSkip").click()

#Skip 후 Summary 페이지 진입 성공 확인
time.sleep(2)
el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/txtUserAlias")
if el is not None and el.is_displayed():
      print("Case 5: Skip 버튼 동작 확인\n"
            "\033[34m"+"-----> Summary 페이지 진입 성공"+"\033[0m")
else:
      print("Case 5: Skip 버튼 동작 확인\n"
            "\033[91m"+"-----> Summary 페이지 진입 실패"+"\033[0m")