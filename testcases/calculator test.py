from Config import start_calculator
from Config.start_calculator import driver
from appium.webdriver.common.touch_action import TouchAction


#tab
action = TouchAction(driver)
action.tap(x=170, y=1312).perform() # 7
action.tap(x=900, y=1800).perform() # +
action.tap(x=600, y=1710).perform() # 3
action.tap(x=950, y=2000).perform() # =



#테스트테스트




