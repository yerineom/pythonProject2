from appium import webdriver

desired_cap = {
    "appium:deviceName": "2be00d99c81d7ece",
    "platformName": "Android",
    "appium:appPackage": "ohc.app.fitto",
    "appium:appActivity": "ohc.app.fitto.ui.activity.ActSplash",
    "newCommandTimeout": 300
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
