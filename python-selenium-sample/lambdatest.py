import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

username = os.getenv("eduardonaquira")  # Replace the username
access_key = os.getenv("LT_KQY5B9VYf9A6RzlT4uMDAUU1iMnPFe6AMokC9bkSWklJAOT")  # Replace the access key


# paste your capibility options below

options = ChromeOptions()
options.browser_version = "latest"
options.platform_name = "Windows 10"
lt_options = {}
lt_options["username"] = username
lt_options["accessKey"] = access_key
# lt_options["video"] = True
# lt_options["resolution"] = "1920x1080"
lt_options["network"] = True
lt_options["build"] = "Selenium 4 Example"
# lt_options["project"] = "unit_testing"
lt_options["smartUI.project"] = "test"
lt_options["name"] = "Selenium 4 Sample Test"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"
options.set_capability("LT:Options", lt_options)


# Steps to run Smart UI project (https://beta-smartui.lambdatest.com/)
# Step - 1 : Change the hub URL to @beta-smartui-hub.lambdatest.com/wd/hub
# Step - 2 : Add "smartUI.project": "<Project Name>" as a capability above
# Step - 3 : Run "driver.execute_script("smartui.takeScreenshot")" command wherever you need to take a screenshot
# Note: for additional capabilities navigate to https://www.lambdatest.com/support/docs/test-settings-options/


class FirstSampleTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="https://eduardonaquira:LT_KQY5B9VYf9A6RzlT4uMDAUU1iMnPFe6AMokC9bkSWklJAOT@hub.lambdatest.com/wd/hub",
            options=options,
        )

    # """ You can write the test cases here """
    def test_demo_site(self):
        # try:
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        # Url
        print("Loading URL")
        driver.get(
            "https://stage-lambda-devops-use-only.lambdatestinternal.com/To-do-app/index.html"
        )

        # Let's click on a element
        driver.find_element(By.NAME, "li1").click()
        location = driver.find_element(By.NAME, "li2")
        location.click()
        print("Clicked on the second element")

        # Take Smart UI screenshot
        # driver.execute_script("smartui.takeScreenshot")

        # Let's add a checkbox
        driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
        add_button = driver.find_element(By.ID, "addbutton")
        add_button.click()
        print("Added LambdaTest checkbox")

        # print the heading
        search = driver.find_element(By.CSS_SELECTOR, ".container h2")
        assert search.is_displayed(), "heading is not displayed"
        print(search.text)
        search.click()
        driver.implicitly_wait(3)

        # Let's download the invoice
        heading = driver.find_element(By.CSS_SELECTOR, ".container h2")
        if heading.is_displayed():
            heading.click()
            driver.execute_script("lambda-status=passed")
            print("Tests are run successfully!")
        else:
            driver.execute_script("lambda-status=failed")

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()