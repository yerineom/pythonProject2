from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from configuration import config
import time
import summary




    #Intro > welcome card swipe 동작
time.sleep(7)
swipe = config.driver.swipe(203,654,885,654,0)
swipe = config.driver.swipe(203,654,885,654,0)
swipe = config.driver.swipe(885,654,203,654,0)
swipe = config.driver.swipe(885,654,203,654,0)
swipe = config.driver.swipe(885,654,203,654,0)


print("\n"
      "<로그인 Flow 테스트>\n"
      "")


    #로그인 버튼 선택 > 로그인페이지 진입
time.sleep(2)
el = config.driver.find_element(by=AppiumBy.ID, value=btnaccount)
el.click()

time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/txtLabel")
if el is not None and el.is_displayed():
    print("case1 : 가입한 계정이 있어요 버튼 선택 동작\n"
          "\033[34m"+">> 로그인페이지 진입 성공"+"\033[0m")
else:
    print("case1 : 가입한 계정이 있어요 버튼 선택 동작\n"
          "\033[31m"+">> 로그인페이지 진입 실패"+"\033[0m")


    #로그인 페이지 X버튼 동작 후 로그인 페이지 재진입 확인
time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/btnOptions")
el.click()
time.sleep(1)

el = config.driver.find_element(by=AppiumBy.ID, value=btnaccount)
el.click()

time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/txtLoginTitle")
if el is not None and el.is_displayed():
    print("case2 : 로그인 페이지 X버튼 동작\n"
          "\033[34m"+">> 로그인페이지 재진입 성공"+"\033[0m")
else:
    print("case2 : 로그인 페이지 X버튼 동작\n"
          "\033[31m"+">> 로그인페이지 재진입 실패"+"\033[0m")


    # 비밀번호 찾기버튼 동작 후 로그인 페이지 재진입 확인
time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/txtFindPassword")
el.click()
time.sleep(1)

el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/btnClose")
el.click()

time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/txtLoginTitle")
if el is not None and el.is_displayed():
    print("case3 : 비밀번호 찾기 진입 후 뒤로가기 동작\n"
          "\033[34m"+">> 로그인페이지 재진입 성공"+"\033[0m")
else:
    print("case3 : 비밀번호 찾기 진입 후 뒤로가기 동작\n"
          "\033[31m"+">> 로그인페이지 재진입 실패"+"\033[0m")


    # 회원가입페이지 이동 후 로그인 페이지 재진입 확인
time.sleep(1)

el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/txtSignUp")
el.click()
time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/btnOptions")
el.click()
time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value=btnaccount)
el.click()
time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/txtSignUp")
el.click()
time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/btnDontAgree")
el.click()
time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/btnBottom")
el.click()

time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/txtLoginTitle")
if el is not None and el.is_displayed():
    print("case4 : 회원가입 페이지 이동 후 로그인 재진입\n"
          "\033[34m"+">> 로그인페이지 재진입 성공"+"\033[0m")
else:
    print("case4 : 회원가입 페이지 이동 후 로그인 재진입\n"
          "\033[31m"+">> 로그인페이지 재진입 실패"+"\033[0m")



    # 가입되지 않은 ID, PW 입력
time.sleep(2)
el = config.driver.find_element(by=AppiumBy.ID, value=emailaddress).send_keys('shcho4242+8888@gmail.com')
el = config.driver.find_element(by=AppiumBy.ID, value=edtpw).send_keys('qwer1234')

time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value=btncontinue)
el.click()

time.sleep(1)
el = config.driver.find_element(by=MobileBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout")
if el is not None and el.is_displayed():
    print("case5 : 가입되지 않은 이메일 로그인 오류 Dialog\n"
          "\033[34m"+">> 생성 성공"+"\033[0m")
else:
    print("case5 : 가입되지 않은 이메일 로그인 오류 Dialog\n"
          "\033[31m"+">> 생성 실패"+"\033[0m")

time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/btnTop")
el.click()

    # 잘못된 PW 입력
time.sleep(2)
el = config.driver.find_element(by=AppiumBy.ID, value=emailaddress).send_keys('shcho4242+888@gmail.com')
el = config.driver.find_element(by=AppiumBy.ID, value=edtpw).send_keys('qwer123456')

time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value=btncontinue)
el.click()

time.sleep(1)
el = config.driver.find_element(by=MobileBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout")
if el is not None and el.is_displayed():
    print("case6 : 잘못된 PW 입력 오류 Dialog\n"
          "\033[34m"+">> 생성 성공"+"\033[0m")
else:
    print("case6 : 잘못된 PW 입력 오류 Dialog\n"
          "\033[31m"+">> 생성 실패"+"\033[0m")

time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/btnTop")
el.click()

    #가입된 ID, PW 입력
time.sleep(2)
el = config.driver.find_element(by=AppiumBy.ID, value=emailaddress).send_keys('shcho4242+888@gmail.com')
el = config.driver.find_element(by=AppiumBy.ID, value=edtpw).send_keys('qwer1234')

    #PW 표시
el = config.driver.find_element(by=AppiumBy.ID, value=pwicon)
el.click()
time.sleep(1)
el.click()

    #로그인버튼 동작 확인 > Device 연결하기 페이지 진입 확인
time.sleep(2)
el = config.driver.find_element(by=AppiumBy.ID, value=btncontinue)
el.click()

time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/content_container")
if el is not None and el.is_displayed():
    print("case7 : Device 연결하기 진입 확인\n"
          "\033[34m"+">> Fitto 연결하기 페이지 진입 성공"+"\033[0m")
else:
    print("case7 : Device 연결하기 진입 확인\n"
          "\033[31m"+">> Fitto 연결하기 페이지 진입 실패"+"\033[0m")


    #디바이스 연결 페이지 진입 _ 권한설정 다이얼로그 동작 확인
time.sleep(2)
el = config.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/content_container")
if el and el.is_displayed():
    el = config.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    el.click()


    #건너뛰기 선택 후 로그인 결과 확인
time.sleep(2)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/btnSkip")
el.click()

time.sleep(1)
el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/action_bar_root")
if el is not None and el.is_displayed():
    print("case8 : 로그인 및 메인페이지 진입 확인\n"
          "\033[34m"+">> 로그인 성공 및 메인페이지 진입 성공"+"\033[0m")

    summary.mainSummary()
    #profile.main_profile()
else:
    print("case8 : 로그인 및 메인페이지 진입 확인\n"
          "\033[31m"+">> 로그인 실패 및 메인페이지 진입 실패"+"\033[0m")