import time

from Config import start_fitto
from selenium.webdriver.common.by import By
from testcases import Fitto_Daily


def summaryMG():
    print("\n"
          "<Main> summary_MG flow \n"
          "")

    #MG page 진입

    time.sleep(1)
    swipe = start_fitto.driver.swipe(560, 1608, 560, 820, 0)

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/lyMGBody").click()

    time.sleep(1)
    el =start_fitto.driver.find_element(By.XPATH,"//android.view.ViewGroup[@resource-id='ohc.app.fitto:id/toolbar']/android.widget.FrameLayout/android.widget.LinearLayout[2]")
    if el is not None and el.is_displayed():
        print("case 1: Summary > MG page 진입 버튼 동작 확인\n"
            "\033[34m" +" -----> MG page 진입 성공" + "\033[0m")
    else:
        print("case 1: Summary > MG page 진입 버튼 동작 확인\n"
              "\033[91m" + " -----> MG page 진입 실패" + "\033[0m")

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/txtBestRecordValue")
    if el is not None and el.is_displayed():
        print("case 2: MG 최고 기록 순위 표시 확인\n"
              "\033[34m" + " -----> 최고 기록 항목이 표시됨" + "\033[0m")
    else:
        print("case 2: MG 최고 기록 순위 존재 확인\n"
              "\033[91m" + " -----> 최고 기록 항목이 표시 되지 않음" + "\033[0m")

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/txtUserAlias")
    if el is not None and el.is_displayed():
        print("case 3: MG page > back 버튼 동작 확인\n"
              "\033[34m" + " -----> Summary page로 이동됨" + "\033[0m")
    else:
        print("case 3: MG page > back 버튼 동작 확인\n"
              "\033[91m" + " -----> Summary page로 이동 되지 않음" + "\033[0m")


    Fitto_Daily.FittoDaily()


