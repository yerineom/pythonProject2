import time

from Config import start_fitto
from selenium.webdriver.common.by import By

def FittoDaily():

    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"//android.widget.LinearLayout[@content-desc='매일']").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/lyFittoStatus")

