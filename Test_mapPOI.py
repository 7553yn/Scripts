import unittest
import os
import HTMLTestRunner
from datetime import time
from appium import webdriver
from time import sleep
from appium.webdriver import WebElement
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


class HSRTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'iOS',
                'platformVersion': '15.1',
                'deviceName': 'HotaiConnected',
                'noReset': 'true',
                'automationName': 'XCUITest',
                'bundleId': 'tw.com.yoxi.rider.uat',
                'udid': '00008030-001661411EE3402E',
                'xcodeOrgId': '2U3546YDFH',
                'xcodeSigningId': 'iPhone Developer',
            }
        )

    def tearDown(self):
        self.driver.quit()

    def test_1_Firstpage(self):
        self.driver.find_element_by_accessibility_id('我已是會員，立即登入').click()

    def test_2_PhoneField(self):
        sleep(1)
        phoneTF = self.driver.find_element_by_accessibility_id('請輸入手機號碼')
        phoneTF.send_keys("0900000115")

    def test_3_PasswordField(self):
        passwordTF = self.driver.find_element_by_accessibility_id('請輸入密碼')
        passwordTF.send_keys("Aa1234")

    def test_4_LoginBtn(self):
        self.driver.find_element_by_accessibility_id('登入').click()

    def test_5_usualTrip(self):
        sleep(4)
        TouchAction(self.driver).tap(x=39, y=77).perform()
        TouchAction(self.driver).tap(x=162, y=385).perform()
        self.driver.find_element_by_accessibility_id('常用旅程 設定常用旅程可在首頁一鍵叫車').click()

    def test_6_mapPOI(self):
        sleep(1)
        TouchAction(self.driver).tap(x=198, y=344).perform()
        sleep(1)
        TouchAction(self.driver).tap(x=381, y=151).perform()
        TouchAction(self.driver).tap(x=381, y=151).perform()
        sleep(1)
        TouchAction(self.driver).tap(x=301, y=103).perform()

        location_tf = self.driver.find_element_by_xpath(
            "(//XCUIElementTypeOther[@name=\"設定上車地點 松江路433號 台灣 在地圖上設定地點 Vertical scroll bar, 1 page Horizontal scroll "
            "bar, 1 page\"])[3]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]")

        location_hsr = ['高鐵台中', '高鐵台中站', '台中高鐵', '台中高鐵站', '高鐵烏日', '高鐵烏日站', '烏日高鐵', '烏日高鐵站']

        for i in location_hsr:
            location_tf.send_keys(Keys.DELETE * 5)
            location_tf.send_keys(i)
            sleep(2)

            try:
                self.driver.find_element_by_accessibility_id('高鐵台中站-下手扶梯右轉7號出口(P2停車場內)會面點4 台中市烏日區').is_displayed()
                print('{}，PASS'.format(i))

            except NoSuchElementException:
                print('{}，FAIL'.format(i))

        location_hsr2 = ['高鐵台南', '高鐵台南站', '台南高鐵', '台南高鐵站']
        print('----------------------------------------------')

        for j in location_hsr2:
            location_tf.send_keys(Keys.DELETE * 5)
            location_tf.send_keys(j)
            sleep(2)

            try:
                self.driver.find_element_by_accessibility_id('高鐵台南站-3號出口(請至3號出口外，第二車道搭乘) 台南市歸仁區').is_displayed()
                print('{}，PASS'.format(j))
            except NoSuchElementException:
                print('{}，FAIL'.format(j))

        location_hsr3 = ['高鐵高雄', '高鐵高雄站', '高雄高鐵', '高雄高鐵站', '高鐵左營', '高鐵左營站', '左營高鐵', '左營高鐵站']
        print('----------------------------------------------')

        for x in location_hsr3:
            location_tf.send_keys(Keys.DELETE * 5)
            location_tf.send_keys(x)
            sleep(2)

            try:
                self.driver.find_element_by_accessibility_id(
                    '高鐵左營站-5號出口(請至5號出口外，上手扶梯，於4樓臨停接送區搭乘) 高雄市左營區').is_displayed()
                print('{}，PASS'.format(x))
            except NoSuchElementException:
                print('{}，FAIL'.format(x))

        location_hsr4 = ['高鐵桃園', '高鐵桃園站', '桃園高鐵', '桃園高鐵站']
        print('----------------------------------------------')

        for y in location_hsr4:
            location_tf.send_keys(Keys.DELETE * 5)
            location_tf.send_keys(y)
            sleep(2)

            try:
                self.driver.find_element_by_accessibility_id(
                    '高鐵桃園站-3號出口(請至人行道右轉，過YouBike站，計程車招呼站搭乘) 桃園市中壢區').is_displayed() \
                    and self.driver.find_element_by_accessibility_id(
                    '高鐵桃園站-1號出口(請至車道對面P1停車場內搭乘) 桃園市中壢區').is_displayed() \
                    and self.driver.find_element_by_accessibility_id(
                    '高鐵桃園站-8號出口(請至車道對面P2停車場內搭乘) 桃園市中壢區').is_displayed()
                print('{}，PASS'.format(y))
            except NoSuchElementException:
                print('{}，FAIL'.format(y))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(HSRTests("test_6_mapPOI"))
    now = time.strftime('%Y-%m-%d-%H_%M_%S')
    report_dir = '/Users/leo/Desktop/yoxiUAT/TestCases/testReport'
    os.makedirs(report_dir, exist_ok=True)
    report_name = '{0}/{1}.html'.format(report_dir, now)

    with open(report_name, 'w') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="測試報告", description="電子圍籬測試")

    runner.run(suite)
    f.close()
