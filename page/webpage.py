#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
selenium基类
本文件存放了selenium基类的封装方法
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains  # 引入 ActionChains 类
from selenium.webdriver.common.keys import Keys
from config.conf import cm
from utils.times import sleep
from utils.logger import log
from common.read_excel import ReadExcel

from selenium import webdriver
import os


class WebPage(object):
    """selenium基类"""

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    def open_newPage(self, url):
        """打开新的页面"""
        js = "window.open(" + '"' + url + '"' + ")"  # 打开wms
        try:
            self.driver.execute_script(js)
            window = self.driver.window_handles
            self.driver.switch_to.window(window[-1])
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(cm.LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)

    def find_elements(self, locator):
        """查找多个相同的元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def is_click(self, locator):
        """点击"""

        text = self.find_element(locator).text
        self.find_element(locator).click()
        sleep(0.5)
        log.info("点击元素：\'%s\' {}".format(locator) % text)

    def is_doubleclick(self, locator):
        """双击"""
        text = self.find_element(locator).text
        el = self.find_element(locator)
        try:
            ActionChains(self.driver).double_click(el).perform()
            log.info("点击元素：\'%s\' {}".format(locator) % text)
        except Exception as e:
            print(text + 'fail')

    def mouse_stop(self, locator):
        text = self.find_element(locator).text
        mouse = self.find_element(locator)
        try:
            ActionChains(self.driver).move_to_element(mouse).perform()
            log.info("鼠标悬停元素：\'%s\' {}".format(locator) % text)
        except Exception as e:
            print(text + 'fail')

    def get_title(self):
        """获取网页标题"""
        log.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    def element_text(self, locator):
        """获取当前的text"""
        text = self.find_element(locator).text
        log.info("获取文本{}".format(text))
        return text

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)

    def get_data(self):
        filepath = "C://Users//will//Desktop//haha//config//data.xlsx"
        data = ReadExcel(filepath)
        log.info("获取文本{}".format(data))
        print(data.dict_data())
        return self.get_data

    def skip_first(self):
        window = self.driver.window_handles
        self.driver.switch_to.window(window[-0])
        sleep(2)
        log.info("打开网页" + self.driver.title)

    def skip_second(self):
        window = self.driver.window_handles
        self.driver.switch_to.window(window[-1])
        sleep(2)
        log.info("打开网页" + self.driver.title)

    def close_web(self):
        self.driver.quit()

    def key_enter(self, locator):

        ele = self.find_element(locator)
        ele.send_keys(Keys.ENTER)
        sleep()


if __name__ == "__main__":
    pass
