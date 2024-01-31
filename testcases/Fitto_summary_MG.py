import time

from Config import start_fitto
from selenium.webdriver.common.by import By



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
        print("case 1: Summary > MQ page 진입 버튼 동작 확인\n"
            "\033[34m" +" -----> MQ page 진입 성공" + "\033[0m")
    else:
        print("case 1: Summary > MQ page 진입 버튼 동작 확인\n"
              "\033[91m" + " -----> MQ page 진입 실패" + "\033[0m")



