from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from configuration import config
import time
import summary_totalLM


def mainSummary():

    # 프로필 진입 여부 확인
    print("\n"
          "<Main_summary 탭 Flow 테스트>\n"
          "")
    time.sleep(1)
    el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/imgThumb")
    el.click()

    time.sleep(1)
    el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case1 : 내 계정 진입 동작\n"
              "\033[34m" + ">> 내 계정 진입 성공" + "\033[0m")
    else:
        print("case1 : 내 계정 진입 동작\n"
              "\033[31m" + ">> 내 계정 진입 실패" + "\033[0m")

    time.sleep(1)
    el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/btnClose")
    el.click()

    # 알림 진입 여부 확인
    time.sleep(1)
    el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/frNotification")
    el.click()

    time.sleep(1)
    el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case2 : 알림 진입 동작\n"
              "\033[34m" + ">> 알림 진입 성공" + "\033[0m")
    else:
        print("case2 : 알림 진입 동작\n"
              "\033[31m" + ">> 알림 진입 실패" + "\033[0m")

    time.sleep(1)
    el = config.driver.find_element(by=AppiumBy.ID, value="ohc.app.fitto:id/btnClose")
    el.click()

    summary_totalLM.totalLM()