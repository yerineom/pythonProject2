from appium import webdriver

desired_cap = {
  "appium:deviceName": "2be00d99c81d7ece",
  "platformName": "Android",
  "appium:appPackage": "com.sec.android.app.popupcalculator",
  "appium:appActivity": "com.sec.android.app.popupcalculator.Calculator",
  "newCommandTimeout": 300
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)