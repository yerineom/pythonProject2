import time

from Config import start_fitto
from selenium.webdriver.common.by import By
from testcases import Fitto_summary_profile

def mainsummary():

#20240129

#프로필 페이지 진입 여부 확인
    print("\n"
        "<Main> summary 탭 flow>\n"
        "")

    time.sleep(5)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/imgThumb").click()

    time.sleep(1)
    el=start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case 1: 내 계정 페이지 진입 확인\n"
            "\033[34m"+" -----> 내 계정 페이지 진입 성공"+"\033[0m")

    else:
        print("case 1: 내 계정 페이지 진입 확인\n"
            "\033[91m" + " -----> 내 계정 페이지 진입 실패" + "\033[0m")


#내 계정 페이지 편집 버튼 선택
    time.sleep(1)
    el=start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnOptionsTextType").click()

    time.sleep(1)
    el=start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case 2: 내 계정 페이지 편집 버튼 동작 확인\n"
              "\033[34m" + " -----> 계정 수정 페이지 진입 성공" + "\033[0m")

    else:
        print("case 2: 내 계정 페이지 편집 버튼 동작 확인\n"
              "\033[91m" + " -----> 계정 수정 페이지 진입 실패" + "\033[0m")


#계정 수정 페이지에서 Back 버튼 선택
    time.sleep(1)
    el=start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el=start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case 3: 계정 수정 페이지 Back 버튼 동작 확인\n"
              "\033[34m" + " -----> 내 계정 페이지 진입 성공" + "\033[0m")
    else:
        print("case 3: 계정 수정 페이지 Back 버튼 동작 확인\n"
              "\033[91m" + " -----> 내 계정 페이지 진입 실패" + "\033[0m")

#내 계정 페이지 Back 버튼 선택
    time.sleep(1)
    el=start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/txtUserAlias")

    if el is not None and el.is_displayed():
        print("case 4: 내 계정 페이지 Back 버튼 동작 확인\n"
              "\033[34m" + " -----> Summary 페이지 진입 성공" + "\033[0m")

    else:
        print("case 4: 내 계정 페이지 Back 버튼 동작 확인\n"
              "\033[91m" + " -----> Summary 페이지 진입 실패" + "\033[0m")



#알림 페이지 진입
    time.sleep(1)
    el= start_fitto.driver.find_element(By.XPATH,"//android.widget.FrameLayout[@resource-id='ohc.app.fitto:id/frNotification']/android.widget.ImageView[1]")
    el.click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/txtLabel")

    if el is not None and el.is_displayed():
        print("case 5: 알림 버튼 동작 확인\n"
              "\033[34m" + " -----> 알림 페이지 진입 성공" + "\033[0m")
    else:
        print("case 5: 알림 버튼 동작 확인\n"
              "\033[91m" + " -----> 알림 페이지 진입 실패" + "\033[0m")

#알림 페이지 Back 버튼 선택
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/txtUserAlias")

    if el is not None and el.is_displayed():
        print("case 6: 알림 페이지 Back 버튼 동작 확인\n"
          "\033[34m" + " -----> Summary 페이지 진입 성공" + "\033[0m")

    else:
        print("case 6: 알림 페이지 Back 버튼 동작 확인\n"
          "\033[91m" + " -----> Summary 페이지 진입 실패" + "\033[0m")

 #SNS 진입
    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"//android.widget.LinearLayout[@resource-id='ohc.app.fitto:id/lyFacebookBody']/android.widget.ImageView")
    el.click()

    time.sleep(3)
    el = start_fitto.driver.find_element(By.ID, "com.android.chrome:id/url_bar")
    if el is not None and el.is_displayed():
        print("case 7: SNS 버튼 동작 확인\n"
              "\033[34m" + " -----> SNS 페이지 진입 성공(로그인 Dialog 생성)" + "\033[0m")

    else:
        print("case 7: SNS 버튼 동작 확인\n"
              "\033[91m" + " -----> SNS 페이지 진입 실패" + "\033[0m")

#facebook에서 OS 네비 키로 fitto 재 진입
    time.sleep(1)
    start_fitto.driver.press_keycode(4)

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/imgThumb")
    if el is not None and el.is_displayed():
        print("case 8: SNS page에서 device back 버튼 동작 확인\n"
            "\033[34m" + " -----> Fitto Summary 진입 성공" + "\033[0m")

    else:
        print("case 8: SNS page에서 device back 버튼 동작 확인\n"
          "\033[91m" + " -----> Fitto Summary 진입 실패" + "\033[0m")


    Fitto_summary_profile.summaryprofile()


