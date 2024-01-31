import time

from Config import start_fitto
from selenium.webdriver.common.by import By
from testcases import Fitto_summary_MQ



def summarytotalLM():

    print("\n"
          "<Main> summary_total LM flow>\n"
          "")

    #총 근육량(Total LM) page 진입
    el= start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/lyBtnTLMBody").click()

    time.sleep(1)
    el= start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case 1: Summary > Total LM 진입 버튼 동작 확인\n"
            "\033[34m" +" -----> Total LM 페이지 진입 성공" + "\033[0m")
    else:
        print("case 1: Summary > Total LM  진입 버튼 동작 확인\n"
              "\033[91m" + " -----> Total LM 페이지 진입 실패" + "\033[0m")

    #Total LM 페이지 디폴트 탭 확인
    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"//android.widget.LinearLayout[@content-desc='전신']")
    selected_attribute = el.get_attribute('selected')
    if selected_attribute == 'true':
        print("case 2: Total LM 디폴트 탭 확인\n"
              "\033[34m" + " -----> 디폴트 탭 '전신' " + "\033[0m")

    else:
        print("case 2: Total LM 디폴트 탭 확인\n"
              "\033[91m" + " -----> 디폴트 탭 '전신'이 아님" + "\033[0m")


    #전신 > Fitto status
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/lyFittoStatusBody").click()
    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='ohc.app.fitto:id/txtLabel' and @text='Fitto 상태']")
    if el is not None and el.is_displayed():
        print("case 3: Total LM > Fitto status 버튼 동작 확인\n"
              "\033[34m" + " -----> Fitto status 진입 성공" + "\033[0m")
    else:
        print("case 3: Total LM > Fitto status 버튼 동작 확인\n"
              "\033[91m" + " -----> Fitto status 진입 실패" + "\033[0m")

    #Fitto status back 버튼
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case 4: Fitto status back 버튼 동작 확인\n"
              "\033[34m" + " -----> Total LM 페이지 진입 성공" + "\033[0m")
    else:
        print("case 4: Fitto status back 버튼 동작 확인\n"
              "\033[91m" + " -----> Total LM 페이지 진입 실패" + "\033[0m")

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/lyFittoStatusBody").click()

    #9블럭 테라피
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnSet9BlockTherapy").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"//android.widget.TextView[@resource-id='ohc.app.fitto:id/txtLabel' and @text='9 블럭 테라피']")
    if el is not None and el.is_displayed():
        print("case 5: 9블럭 테라피 설정 버튼 동작 확인\n"
              "\033[34m" + " -----> 9블럭 테라피 페이지 진입 성공" + "\033[0m")
    else:
        print("case 5: 9블럭 테라피 설정 버튼 동작 확인\n"
              "\033[91m" + " -----> 9블럭 테라피 진입 실패" + "\033[0m")

    #9블록 테라피 골 설정 케이스 작성 필요..(추후)




    time.sleep(2)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

    time.sleep(2)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

    #전신 그래프 확인
    #디폴트값 확인(주간) > 월간 > 주간
    time.sleep(2)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/radioWeekly")
    checked_attribute = el.get_attribute('checked')
    if checked_attribute == 'true':
        print("case 6: 전신 그래프 디폴트 확인\n"
              "\033[34m" + " -----> 주간 그래프 버튼이 선택된 상태이며, 디폴트 값으로 표시됨 " + "\033[0m")

    else:
        print("case 6: 전신 그래프 디폴트 확인\n"
              "\033[91m" + " -----> 주간 그래프 버튼이 선택 되지 않은 상태 " + "\033[0m")


    # 주간 그래프 이동 확인(<,>)
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnPrev").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnNext")
    enable_state = el.get_attribute('enabled')
    if enable_state == 'true':
        print("case 7: 주간 그래프 < 버튼 동작 확인\n"
              "\033[34m" + " -----> 지난 주의 그래프가 표시됨 " + "\033[0m")
    else:
        print("case 7: 주간 그래프 < 버튼 동작 확인\n"
              "\033[91m" + " -----> 지난 주의 그래프가 표시되지 않음" + "\033[0m")

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnNext").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnNext")
    enable_state = el.get_attribute('enabled')
    if enable_state == 'false':
        print("case 8: 주간 그래프 > 버튼 동작 확인\n"
              "\033[34m" + " -----> 이번 주의 그래프가 표시됨 " + "\033[0m")
    else:
        print("case 8: 주간 그래프 > 버튼 동작 확인\n"
              "\033[91m" + " -----> 이번 주의 그래프가 표시되지 않음" + "\033[0m")


    #월간 그래프

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/radioMonthly").click()

    time.sleep(1)
    el = start_fitto. driver.find_element(By.ID,"ohc.app.fitto:id/radioMonthly")
    checked_attribute = el.get_attribute('checked')
    if checked_attribute == 'true':
        print("case 9: 월간 그래프 버튼 동작 확인\n"
              "\033[34m" + " -----> 그래프가 월간 형식으로 표시됨 " + "\033[0m")

    else:
        print("case 9: 월간 그래프 버튼 동작 확인\n"
              "\033[91m" + " -----> 그래프가 월간 형식으로 표시되지 않음 " + "\033[0m")


    # 월간 그래프 이동 확인(<,>)
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnPrev").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnNext")
    enable_state = el.get_attribute('enabled')
    if enable_state == 'true':
        print("case 10: 월간 그래프 < 버튼 동작 확인\n"
              "\033[34m" + " -----> 지난 달의 그래프가 표시됨 " + "\033[0m")
    else:
        print("case 10: 월간 그래프 < 버튼 동작 확인\n"
              "\033[91m" + " -----> 지난 달의 그래프가 표시되지 않음" + "\033[0m")

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnNext").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnNext")
    enable_state = el.get_attribute('enabled')
    if enable_state == 'false':
        print("case 11: 월간 그래프 > 버튼 동작 확인\n"
              "\033[34m" + " -----> 이번 달의 그래프가 표시됨 " + "\033[0m")
    else:
        print("case 11: 월간 그래프 > 버튼 동작 확인\n"
              "\033[91m" + " -----> 이번 달의 그래프가 표시되지 않음" + "\033[0m")


    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/radioWeekly").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/radioWeekly")
    checked_attribute = el.get_attribute('checked')
    if checked_attribute == 'true':
        print("case 12: 주간 그래프 버튼 동작 확인\n"
              "\033[34m" + " -----> 그래프가 주간 형식으로 표시됨 " + "\033[0m")

    else:
        print("case 12: 주간 그래프 버튼 동작 확인\n"
              "\033[91m" + " -----> 그래프가 주간 형식으로 표시되지 않음 " + "\033[0m")

    #전신 > 최근기록
    #측정 데이터가 2개 이상일 시 > 버튼 생성 및 페이지 진입 가능 추후 작성 필요


    #부분 탭
    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"//android.widget.LinearLayout[@content-desc='부분']").click()
    el = start_fitto.driver.find_element(By.XPATH,"//android.widget.TextView[@text='분석']")
    if el is not None and el.is_displayed():
        print("case 13: Total LM 부분 탭 동작 확인\n"
              "\033[34m" + " -----> 부분 페이지 진입 성공 " + "\033[0m")

    else:
        print("case 13: Total LM 부분 탭 동작 확인\n"
              "\033[91m" + " -----> 부분 페이지 진입 실패 " + "\033[0m")

    #부분 탭 > 전체기록
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/lyBtnAllRecData").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case 14: 부분 탭 > 전체 기록 버튼 동작 확인\n"
              "\033[34m" + " -----> 전체 기록 페이지 진입 성공 " + "\033[0m")

    else:
        print("case 14: 부분 탭 > 전체 기록 버튼 동작 확인\n"
              "\033[91m" + " -----> 전체 기록 페이지 진입 실패 " + "\033[0m")


    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"//android.widget.TextView[@text='몸통']")
    selected_attribute = el.get_attribute('selected')
    if selected_attribute == 'true':
        print("case 15: 부분 탭 > 전체 기록 > 디폴트 탭 확인\n"
              "\033[34m" + " -----> 디폴트 탭은 몸통이며, 몸통 부위의 근육량이 표시됨 " + "\033[0m")

    else:
        print("case 15: 부분 탭 > 전체 기록 > 디폴트 탭 확인\n"
              "\033[91m" + " -----> 디폴트 탭은 몸통이 아니며, 몸통 부위의 근육량 표시되지 않음 " + "\033[0m")


    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH, "//android.widget.TextView[@text='팔']").click()
    el = start_fitto.driver.find_element(By.XPATH, "//android.widget.TextView[@text='팔']")
    selected_attribute = el.get_attribute('selected')
    if selected_attribute == 'true':
        print("case 16: 팔 부위 탭 선택 동작 확인\n"
              "\033[34m" + " -----> 팔 부위의 근육량이 표시됨 " + "\033[0m")

    else:
        print("case 16: 팔 부위 탭 선택 동작 확인\n"
              "\033[91m" + " -----> 팔 부위의 근육량이 표시되지않음 " + "\033[0m")

    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH, "//android.widget.TextView[@text='다리']").click()
    el = start_fitto.driver.find_element(By.XPATH, "//android.widget.TextView[@text='다리']")
    selected_attribute = el.get_attribute('selected')
    if selected_attribute == 'true':
        print("case 17: 다리 부위 탭 선택 동작 확인\n"
              "\033[34m" + " -----> 다리 부위의 근육량이 표시됨 " + "\033[0m")

    else:
        print("case 17: 다리 부위 탭 선택 동작 확인\n"
              "\033[91m" + " -----> 다리 부위의 근육량이 표시되지않음 " + "\033[0m")


    #전체 기록 Back 버튼
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el=start_fitto.driver.find_element(By.XPATH, "//android.view.ViewGroup[@resource-id='ohc.app.fitto:id/toolbar']/android.widget.FrameLayout/android.widget.LinearLayout[2]")
    if el is not None and el.is_displayed():
        print("case 18: 전체 기록 back 버튼 동작 확인\n"
              "\033[34m" + " -----> 이전 페이지(근육량)로 이동 성공 " + "\033[0m")
    else:
        print("case 18: 전체 기록 back 버튼 동작 확인\n"
              "\033[91m" + " -----> 이전 페이지(근육량)로 이동 실패" + "\033[0m")

    #전체 기록 페이지 재 진입
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/lyBtnAllRecData").click()


    #전체 기록 편집
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptionsTextType").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH, "(//android.widget.ImageButton[@resource-id='ohc.app.fitto:id/btnDelete'])[1]")
    if el is not None and el.is_displayed():
        print("case 19: 전체 기록 편집 버튼 동작 확인\n"
              "\033[34m" + " -----> 삭제 아이콘 생성됨 " + "\033[0m")

    else:
        print("case 19: 전체 기록 편집 버튼 동작 확인\n"
              "\033[91m" + " -----> 삭제 아이콘 생성되지 않음 " + "\033[0m")

    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH, "(//android.widget.ImageButton[@resource-id ='ohc.app.fitto:id/btnDelete'])[1]").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.LinearLayout/android.widget.LinearLayout")
    if el is not None and el.is_displayed():
        print("case 20: 삭제 아이콘 동작 확인\n"
              "\033[34m" + " -----> 데이터 삭제 여부 확인 메시지 생성됨 " + "\033[0m")

    else:
        print("case 20: 삭제 아이콘 동작 확인\n"
              "\033[91m" + " -----> 데이터 삭제 여부 확인 메시지 생성 되지 않음 " + "\033[0m")


    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnBottom").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH, "(//android.widget.ImageButton[@resource-id ='ohc.app.fitto:id/btnDelete'])[1]")
    if el is not None and el.is_displayed():
        print("case 21: 데이터 삭제 여부 메시지 창의 취소 버튼 동작 확인\n"
              "\033[34m" + " -----> 메시지 창이 닫히고, 삭제 아이콘이 생성된 상태 " + "\033[0m")

    else:
        print("case 21: 데이터 삭제 여부 메시지 창의 취소 버튼 동작 확인\n"
              "\033[91m" + " -----> 메시지 창이 닫히지 않거나, 삭제 아이콘이 생성 되지 않은 상태 " + "\033[0m")


    #데이터 삭제 여부 메시지 창의 삭제 버튼 동작 확인 추후 확인할 것. 삭제 성공에 대한 요소를 찾기가 어려


    #완료 버튼 선택
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptionsTextType").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnOptionsTextType")
    text_attribute = el.get_attribute('text')
    if text_attribute == '편집':
        print("case 22: 완료 버튼 동작 확인\n"
              "\033[34m" + " -----> 삭제 아이콘 사라지며, 편집이 완료됨" + "\033[0m")

    else:
        print("case 22: 완료 버튼 동작 확인\n"
              "\033[91m" + " -----> 편집이 완료되지 않음 " + "\033[0m")

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnClose").click()


    #SNS 공유 기능
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptions").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "android:id/resolver_list")
    if el is not None and el.is_displayed():
        print("case 23: SNS 공유 버튼 동작 확인\n"
              "\033[34m" + " -----> 공유 가능한 app 목록이 표시됨 " + "\033[0m")

    else:
        print("case 23:  SNS 공유 버튼 동작 확인\n"
              "\033[91m" + " -----> 공유 가능한 app 목록이 표시되지 않음 " + "\033[0m")

    #SNS 목록 Swipe하여 올리고 / 내리고 / 닫기
    time.sleep(3)
    swipe = start_fitto.driver.swipe(560, 1290, 560, 751, 0)
    swipe = start_fitto.driver.swipe(560, 115, 560, 790, 0)
    swipe = start_fitto.driver.swipe(560, 874, 560, 1740, 0)

    Fitto_summary_MQ.summaryMQ()


















