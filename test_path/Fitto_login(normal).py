import time

from Config import start_fitto
from selenium.webdriver.common.by import By
#from testcases import Fitto_summary
#from testcases import Fitto_summary_profile
#from testcases import Fitto_summry_totalLM
#from testcases import Fitto_summary_MQ
#from testcases import Fitto_summary_MG
from testcases import Fitto_Daily


#로그인
#가입한 계정이 있어요 버튼 선택

time.sleep(7)
el =start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnHasAccount").click()

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

#Fitto_summary.mainsummary()
#Fitto_summary_profile.summaryprofile()
#Fitto_summry_totalLM.totalLM()
#Fitto_summary_MQ.summaryMQ()
#Fitto_summary_MG.summaryMG()
Fitto_Daily.FittoDaily()