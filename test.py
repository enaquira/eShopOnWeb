from selenium import webdriver
from selenium.webdriver.chrome.options import Options

try:
    print("Starting test...")

    options = Options()
    options.set_capability("browserName", "Chrome")
    options.set_capability("browserVersion", "latest")
    options.set_capability("LT:Options", {
        "username": "eduardonaquira",
        "accessKey": "LT_KQY5B9VYf9A6RzlT4uMDAUU1iMnPFe6AMokC9bkSWklJAOT",
        "platformName": "Windows 11",
        "build": "Debug Build",
        "name": "Silent Issue Test"
    })

    driver = webdriver.Remote(
        command_executor="https://hub.lambdatest.com/wd/hub",
        options=options
    )

    driver.get("https://www.google.com")
    print("Page title:", driver.title)
    driver.quit()

except Exception as e:
    print("⚠️ There was an error:", e)