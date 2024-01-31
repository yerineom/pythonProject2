time.sleep(1)
el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

time.sleep(1)
el = start_fitto.driver.find_element(By.XPATH,
                                     "(//android.widget.ImageView[@resource-id='ohc.app.fitto:id/imgArrow'])[1]").click()

# 상완 부위 상세페이지에서 즐겨찾기 버튼 선택
time.sleep(1)
el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptions").click()

# time.sleep(1)
# el = start_fitto.driver.find_element(By.XPATH,)
# 즐겨찾기 설정 유무 확인할 요소가 없는데????? 어떻게 해야할지?????

time.sleep(1)
el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnClose").click()

time.sleep(1)
el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/btnOptions").click()

time.sleep(1)
el = start_fitto.driver.find_element(By.ID, "ohc.app.fitto:id/chkFavorite")
if el is not None and el.is_displayed():
    print("case 20: MQ > 즐겨찾는 부위 추가 후 항목 존재 확인\n"
          "\033[34m" + " -----> 즐겨 찾는 부위에 추가된 항목이 표시됨" + "\033[0m")

else:
    print("case 20: MQ > 즐겨찾는 부위 추가 후 항목 존재 확인\n"
          "\033[34m" + " -----> 즐겨 찾는 부위에 추가된 항목이 표시 되지 않음" + "\033[0m")

#dkdkdkdk


#하2하2

