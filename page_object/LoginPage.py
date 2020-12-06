#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

search = Element('login')


class Loginpage(WebPage):
    """登录页面"""

    def input_username(self, content):
        """输入账号"""
        self.input_text(search['输入账号'], txt=content)

    def input_password(self, content):
        """输入密码"""
        self.input_text(search['输入密码'], txt=content)

    def click_loginButton(self):
        """点击登录"""
        self.is_click(search['登录按钮'])
        sleep()




if __name__ == '__main__':
    pass
