import time


from Config import start_fitto
from selenium.webdriver.common.by import By
from testcases import Fitto_summary_MG




def summaryMQ():

    print("\n"
          "<Main> summary_MQ flow \n"
          "")

    #MQ page 진입
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/lyMQBody").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"//android.view.ViewGroup[@resource-id='ohc.app.fitto:id/toolbar']/android.widget.FrameLayout/android.widget.LinearLayout[2]")
    if el is not None and el.is_displayed():
        print("case 1: Summary > MQ page 진입 버튼 동작 확인\n"
            "\033[34m" +" -----> MQ page 진입 성공" + "\033[0m")
    else:
        print("case 1: Summary > MQ page 진입 버튼 동작 확인\n"
              "\033[91m" + " -----> MQ page 진입 실패" + "\033[0m")

    #MQ page back 버튼 동작 확인
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/txtUserAlias")
    if el is not None and el.is_displayed():
        print("case 2: Summary > MQ page 진입 버튼 동작 확인\n"
              "\033[34m" + " -----> MQ page 재 진입 성공" + "\033[0m")
    else:
        print("case 2: Summary > MQ page 진입 버튼 동작 확인\n"
              "\033[91m" + " -----> MQ page 재 진입 실패" + "\033[0m")

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/lyMQBody").click()

    #부위별 페이지 진입 확인(상완 / 가슴(남자만))

    #상완
    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"(//android.widget.ImageView[@resource-id='ohc.app.fitto:id/imgArrow'])[1]").click()


    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"//android.view.ViewGroup[@resource-id='ohc.app.fitto:id/toolbar']/android.widget.FrameLayout/android.widget.LinearLayout[2]")
    if el is not None and el.is_displayed():
        print("case 3: MQ > 상완 부위 진입 버튼 동작 확인\n"
              "\033[34m" + " -----> 상완 부위 진입 성공" + "\033[0m")
    else:
        print("case 3: MQ > 상완 부위 진입 버튼 동작 확인\n"
              "\033[91m" + " -----> 상완 부위 진입 실패" + "\033[0m")

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnClose").click()


    #프로필페이지 성별확인
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/imgThumb").click()

    #남성
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/txtGender")
    text_attribute = el.get_attribute('text')
    if text_attribute == '남성':
        print("case 4: 성별 확인\n"
                "\033[34m" + " -----> 성별=남성" + "\033[0m")

        Male_MQ_breast()
    else:
        print("case 4: 성별 확인\n"
                 "\033[34m" + " -----> 성별=여성" + "\033[0m")

        Female_MQ_breast()




def Male_MQ_breast():
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/lyMQBody").click()

    el = start_fitto.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout")
    time.sleep(1)
    try:
        el = start_fitto.driver.find_element(By.XPATH,"//android.widget.TextView[@resource-id='ohc.app.fitto:id/txtTitle' and @text='가슴']")
        if el.is_displayed():
            print("case 5: MQ > (남성)가슴 부위 항목 존재 유무 확인\n"
                  "\033[34m" + " -----> 가슴 부위 항목 존재" + "\033[0m")
            time.sleep(1)
            el = start_fitto.driver.find_element(By.XPATH,"(//android.widget.ImageView[@resource-id='ohc.app.fitto:id/imgArrow'])[4]").click()

            time.sleep(1)
            el = start_fitto.driver.find_element(By.XPATH,"//android.view.ViewGroup[@resource-id='ohc.app.fitto:id/toolbar']/android.widget.FrameLayout/android.widget.LinearLayout[2]")
            if el is not None and el.is_displayed():
                print("case 6: MQ > (남성)가슴 부위 진입 버튼 동작 확인\n"
                      "\033[34m" + " -----> 가슴 부위 진입 성공" + "\033[0m")
            else:
                print("case 6: MQ > (남성)가슴 부위 진입 버튼 동작 확인\n"
                      "\033[91m" + " -----> 가슴 부위 진입 실패" + "\033[0m")

            time.sleep(1)
            el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

    except:
            print("case 5: MQ > (남성)가슴 부위 항목 존재 유무 확인\n"
                  "\033[91m" + " -----> 가슴 부위 항목 없음" + "\033[0m")


    MQ_scan_step()

def Female_MQ_breast():
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/lyMQBody").click()

    time.sleep(1)
    try:
        el = start_fitto.driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='ohc.app.fitto:id/txtTitle' and @text='가슴']")
        if el.is_displayed():
            print("case 5: MQ > (여성)가슴 부위 항목 존재 유무 확인\n"
                  "\033[91m" + " -----> 가슴 부위 항목 존재" + "\033[0m")

    except:
            print("case 5: MQ > (여성)가슴 부위 항목 존재 유무 확인\n"
                  "\033[34m" + " -----> 가슴 부위 항목 없음" + "\033[0m")

    MQ_scan_step()



def MQ_scan_step():

    #MQ scan 버튼
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnScan").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case 7: MQ > scan 버튼 동작 확인\n"
              "\033[34m" + " -----> 측정 부위 선택 page 진입 성공" + "\033[0m")
    else:
        print("case 7: MQ > Scan 버튼 동작 확인\n"
              "\033[91m" + " -----> 측정 부위 선택 page 진입 실패" + "\033[0m")

    #MQ 측정 page 진입 시 측정 시작(scan start) 버튼 상태 확인
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnStartScan")
    enabled_attribute = el.get_attribute('enabled')
    if enabled_attribute == 'false':
        print("case 8: MQ 측정 page 진입 시,측정 시작 버튼 상태 확인\n"
              "\033[34m" + " -----> 측정 시작 버튼 비 활성화 상태 " + "\033[0m")

    else:
        print("case 8: MQ 측정 page 진입 시,측정 시작 버튼 상태 확인\n"
              "\033[91m" + " -----> 측정 시작 버튼 활성화 상태" + "\033[0m")



    #MQ 측정 시작(scan start) 버튼 상태(항목 선택 시 활성 / 비 활성화 확인)

    # 측정 선택 항목 있을 시 측정 시작 버튼 상태 확인
    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"(//android.widget.CheckBox[@resource-id='ohc.app.fitto:id/chkSelect'])[1]").click()
    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"(//android.widget.CheckBox[@resource-id='ohc.app.fitto:id/chkSelect'])[1]")
    checked_attribute = el.get_attribute('checked')
    if checked_attribute == 'true':
        print("case 9: 측정 부위 선택 시 체크 박스 상태 확인\n"
              "\033[34m" + " -----> 선택한 부위의 체크 박스가 체크된 상태 " + "\033[0m")

        time.sleep(1)
        el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnStartScan")
        enabled_attribute = el.get_attribute('enabled')
        if enabled_attribute == 'true':
            print("case 10: 선택된 측정 부위가 있을 시 측정 시작 버튼 상태 확인\n"
                  "\033[34m" + " -----> 측정 시작(scan start) 버튼 활성화 상태 " + "\033[0m")

        else:
            print("case 10: 선택된 측정 부위가 있을 시 측정 시작 버튼 상태 확인\n"
                  "\033[91m" + " -----> 측정 시작(scan start) 버튼 비 활성화 상태" + "\033[0m")

    else:
        print("case 9: 측정 부위 선택 시 체크 박스 상태 확인\n"
              "\033[91m" + " -----> 선택한 부위의 체크 박스가 체크 되지 않은 상태" + "\033[0m")

    #측정 선택 항목 해제 시

    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"(//android.widget.CheckBox[@resource-id='ohc.app.fitto:id/chkSelect'])[1]").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"(//android.widget.CheckBox[@resource-id='ohc.app.fitto:id/chkSelect'])[1]")
    checked_attribute = el.get_attribute('checked')
    if checked_attribute == 'false':
        print("case 11: 측정 부위 선택 해제 확인\n"
              "\033[34m" + " -----> 선택한 부위의 체크 박스가 해제된 상태 " + "\033[0m")

        time.sleep(1)
        el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnStartScan")
        enabled_attribute = el.get_attribute('enabled')
        if enabled_attribute == 'false':
            print("case 12: 선택된 측정 부위가 없을 시 측정 시작 버튼 상태 확인\n"
                  "\033[34m" + " -----> 측정 시작(scan start) 버튼 비 활성화 상태 " + "\033[0m")

        else:
            print("case 12: 선택된 측정 부위가 없을 시 측정 시작 버튼 상태 확인\n"
                  "\033[91m" + " -----> 측정 시작(scan start) 버튼 활성화 상태" + "\033[0m")


    else:
        print("case 11: 측정 부위 선택 해제 확인\n"
              "\033[91m" + " -----> 선택한 부위의 체크 박스가 해제 되지 않은 상태" + "\033[0m")


    #MQ 측정 시작(scan start)버튼 동작
    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"(//android.widget.CheckBox[@resource-id='ohc.app.fitto:id/chkSelect'])[1]").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnStartScan").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH,"//android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout")
    if el is not None and el.is_displayed():
        print("case 13: 신체 정보(weight) update 창 생성 여부 확인\n"
              "\033[34m" + " -----> 신체 정보(weight) update 창 생성됨" + "\033[0m")

        physical_information_update()


    else:
        print("case 13: 신체 정보(weight) update 창 생성 여부 확인\n"
              "\033[91m" + " -----> 신체 정보(weight) update 창 생성 되지 않음" + "\033[0m")

        time.sleep(1)
        el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnOptions").click()

        time.sleep(1)
        el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/txtLabel")
        if el is not None and el.is_displayed():
            print("case 14: device 연결 page x 버튼 동작 확인\n"
                  "\033[34m" + " -----> 이전 page인 측정 부위 선택 page로 이동됨" + "\033[0m")
        else:
            print("case 14: device 연결 page x 버튼 동작 확인\n"
                  "\033[91m" + " -----> 이전 page인 측정 부위 선택 page로 이동 되지 않음" + "\033[0m")




def physical_information_update():

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/imgLastedUpdateArrow").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/lyKgBody")
    if el is not None and el.is_displayed():
        print("case 14: 몸무게 dropdown 버튼 동작 확인\n"
              "\033[34m" + " -----> 몸무게 입력을 위한 sheet가 생성됨 " + "\033[0m")

        time.sleep(1)
        el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnCancel").click()

        time.sleep(1)
        el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()


        #허리둘레
        time.sleep(1)
        el = start_fitto.driver.find_element(By.XPATH,"//android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout")
        if el is not None and el.is_displayed():
            print("case 15: 신체 정보(waist size) update 창 생성 여부 확인\n"
                  "\033[34m" + " -----> 신체 정보(waist size) update 창 생성됨" + "\033[0m")
            time.sleep(1)
            el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/imgLastedUpdateArrow").click()

            time.sleep(1)
            el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/lyInchBody")
            if el is not None and el.is_displayed():
                print("case 16: 허리 둘레 dropdown 버튼 동작 확인\n"
                      "\033[34m" + " -----> 허리 둘레 입력을 위한 sheet가 생성됨 " + "\033[0m")

                time.sleep(1)
                el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnCancel").click()

                time.sleep(1)
                el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

            else:
                print("case 16: 허리 둘레 dropdown 버튼 동작 확인\n"
                      "\033[91m" + "  -----> 허리 둘레 입력을 위한 sheet가 생성 되지 않음" + "\033[0m")

        else:
            print("case 15: 신체 정보(waist size) update 창 생성 여부 확인\n"
                  "\033[91m" + " -----> 신체 정보(waist size) update 창 생성 되지 않음" + "\033[0m")

        time.sleep(1)
        el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptions").click()

        time.sleep(1)
        el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/txtLabel")
        if el is not None and el.is_displayed():
            print("case 17: device 연결 page x 버튼 동작 확인\n"
                  "\033[34m" + " -----> 이전 page인 측정 부위 선택 page로 이동됨" + "\033[0m")
        else:
            print("case 17: device 연결 page x 버튼 동작 확인\n"
                  "\033[91m" + " -----> 이전 page인 측정 부위 선택 page로 이동 되지 않음" + "\033[0m")

    else:
        print("case 14: 몸무게 dropdown 버튼 동작 확인\n"
              "\033[91m" + " -----> 몸무게 입력을 위한 sheet가 생성 되지 않음" + "\033[0m")



    #MQ Scan page x 버튼
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnOptions").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case 18: MQ > scan page x 버튼 동작 확인\n"
              "\033[34m" + " -----> 이전 page인 MQ page 진입 성공" + "\033[0m")
    else:
        print("case 18: MQ > scan page x 버튼 동작 확인\n"
              "\033[91m" + " -----> 이전 page인 MQ page 진입 실패" + "\033[0m")




    #즐겨찾기

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptions").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case 19: MQ > 즐겨 찾기 버튼 동작 확인\n"
              "\033[34m" + " -----> 즐겨 찾기 page 진입 성공" + "\033[0m")
    else:
        print("case 19: MQ > 즐겨 찾기 버튼 동작 확인\n"
              "\033[91m" + " -----> 즐겨 찾기 page 진입 실패" + "\033[0m")

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case 20: MQ > 즐겨 찾기 page back 버튼 동작 확인\n"
              "\033[34m" + " -----> 이전 page인 MQ page 진입 성공" + "\033[0m")
    else:
        print("case 20: MQ > 즐겨 찾기 page back 버튼 동작 확인\n"
              "\033[91m" + " -----> 이전 page인 MQ page 진입 실패" + "\033[0m")


    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptions").click()


    time.sleep(1)
    try:
        el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/chkFavorite")
        if el is not None and el.is_displayed():
            print("case 21: MQ > 즐겨 찾기 항목 존재 확인\n"
              "\033[34m" + " -----> 기 등록된 즐겨 찾기 항목이 존재" + "\033[0m")


    except:
        print("case 21: MQ > 즐겨 찾기 항목 존재 확인\n"      
              "\033[91m" + " -----> 기 등록된 즐겨 찾기 항목이 존재 하지 않음" + "\033[0m")

        time.sleep(1)
        el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

        time.sleep(1)
        el = start_fitto.driver.find_element(By.XPATH,"(//android.widget.ImageView[@resource-id='ohc.app.fitto:id/imgArrow'])[1]").click()

        # 상완 부위 상세페이지에서 즐겨찾기 버튼 선택
        time.sleep(1)
        el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptions").click()


        time.sleep(1)
        el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

        time.sleep(1)
        el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptions").click()

        time.sleep(1)
        el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/chkFavorite")
        if el is not None and el.is_displayed():
            print("case 22: MQ > 즐겨 찾기 부위 추가 후 항목 존재 확인\n"
                  "\033[34m" + " -----> 즐겨 찾는 부위에 추가된 항목이 표시됨" + "\033[0m")

        else:
            print("case 22: MQ > 즐겨 찾기 부위 추가 후 항목 존재 확인\n"
                  "\033[34m" + " -----> 즐겨 찾는 부위에 추가된 항목이 표시 되지 않음" + "\033[0m")

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

    Fitto_summary_MG.summaryMG()






















































