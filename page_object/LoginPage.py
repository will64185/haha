#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

login = Element('login')


class Loginpage(WebPage):
    """登录页面"""

    def input_username(self, content):
        """输入账号"""
        self.input_text(login['输入账号'], txt=content)

    def input_password(self, content):
        """输入密码"""
        self.input_text(login['输入密码'], txt=content)

    def click_loginButton(self):
        """点击登录"""
        self.is_click(login['登录按钮'])
        sleep()

    def login_name(self):
        """获取当前登录公司"""
        login_name = self.element_text(login['当前登录公司'])
        return login_name

    def mouse_stop1(self):
        """鼠标悬停当前登录人"""
        self.mouse_stop(login['当前登录人'])

    def click_loginOut(self):
        """退出登录"""
        self.is_click(login['退出登录'])
        sleep(2)


if __name__ == '__main__':
    pass
