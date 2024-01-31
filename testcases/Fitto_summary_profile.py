import time

from Config import start_fitto
from selenium.webdriver.common.by import By
from testcases import Fitto_summry_totalLM


def summaryprofile():

    print("\n"
        "<Main> summary_profile flow>\n"
        "")

#프로필 수정 사항 없을 시 저장 버튼 상태 확인
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/imgThumb").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptionsTextType").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptionsTextType")
    enable_state = el.get_attribute('enabled')
    if enable_state == 'false':
        print("case 1: 프로필 수정 사항 없을 시 저장 버튼 상태 확인\n"
               "\033[34m" + " -----> 저장 버튼 비 활성화 상태" + "\033[0m")
    else:
        print("case 1: 프로필 수정 사항 없을 시 저장 버튼 상태 확인\n"
              "\033[91m" + " -----> 저장 버튼 활성화 상태" + "\033[0m")

#프로필 수정 사항 있을 시 저장 버튼 상태 확인
    #프로필 수정 진행
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/edtName").send_keys("프로필 이름 수정")
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptionsTextType")
    enable_state = el.get_attribute('enabled')
    if enable_state == 'true':
        print("case 2: 프로필 수정 사항 있을 시 저장 버튼 상태 확인\n"
               "\033[34m" + " -----> 저장 버튼 활성화 상태" + "\033[0m")
    else:
        print("case 2: 프로필 수정 사항 있을 시 저장 버튼 상태 확인\n"
              "\033[91m" + " -----> 저장 버튼 비 활성화 상태" + "\033[0m")


#프로필 수정 사항 있을 시 Back 버튼 선택 동작 확인
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.LinearLayout/android.widget.LinearLayout")
    if el is not None and el.is_displayed():
        print("case 3: 프로필 정보 수정 사항 있을 시 Back 버튼 동작 확인\n"
          "\033[34m" + " -----> 변경사항 저장 여부 Dialog 생성됨" + "\033[0m")

    else:
        print("case 3: 프로필 정보 수정 사항 있을 시 Back 버튼 동작 확인\n"
          "\033[91m" + " -----> 변경사항 저장 여부 Dialog 생성되지 않음" + "\033[0m")


#변경사항 저장 여부 dialog에서 취소 시
    time.sleep(2)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnBottom").click()

    time.sleep(1)
    el= start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case 4: 프로필 수정 저장 여부 dialog의 취소 버튼 동작 확인\n"
              "\033[34m" + " -----> Dialog가 닫히고, 변경된 정보가 입력된 상태" + "\033[0m")

    else:
        print("case 4: 프로필 수정 저장 여부 dialog의 취소 버튼 동작 확인\n"
              "\033[91m" + " -----> Dialog가 닫히지 않음" + "\033[0m")


#변경사항 저장 여부 dialog에서 삭제 시

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnClose").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnTop").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/txtLabel")
    if el is not None and el.is_displayed():
        print("case 5: 프로필 수정 저장 여부 dialog의 삭제 버튼 동작 확인\n"
              "\033[34m" + " -----> 변경 사항 저장 없이 내 계정 페이지로 이동" + "\033[0m")

    else:
        print("case 5: 프로필 수정 저장 여부 dialog의 삭제 버튼 동작 확인\n"
             "\033[91m" + " -----> 변경 사항 저장 없이 내 계정 페이지로 이동 실패" + "\033[0m")

############

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptionsTextType").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/edtName").send_keys("프로필 이름 수정")
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptionsTextType").click()


# 프로필 수정 사항 있을 시 저장 버튼 선택 >
    time.sleep(5)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnOptionsTextType").click()

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/edtName").send_keys("자동화 테스트")

    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID,"ohc.app.fitto:id/btnOptionsTextType").click()

    #저장 버튼 선택 시 토스트 메시지 생성 및 정보 업데이트 여부 확인
    time.sleep(1)
    el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/tv_message")
    text_attribute = el.get_attribute('text')
    if text_attribute == '성공적으로 업데이트되었습니다':
        print("case 6: 프로필 변경에 대한 토스트 메시지 확인\n"
              "\033[34m" + " -----> '성공적으로 업데이트되었습니다' 생성 및 정보 업데이트 성공 " + "\033[0m")

    else:
        print("case 6: 프로필 변경 적용 확인\n"
              "\033[91m" + " -----> '문제가 발생했습니다. 다시 시도해 주세요' 생성 및 정보 업데이트 실패 " + "\033[0m")

    Fitto_summry_totalLM.summarytotalLM()
