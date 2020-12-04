#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.LoginPage import Loginpage
from page_object.PchsPage import pchspage
from page_object.StockPage import stockpage
from page_object.AllotPage import allotpage

from utils.times import sleep
import os


@allure.feature("调拨管理")
class TestPchswc:
    @pytest.fixture(scope='function', autouse=True)
    def open_oms(self, drivers):
        """oms2.0,进入采购管理"""
        LoginPage = Loginpage(drivers)
        LoginPage.get_url(ini.url)

    @allure.story("调拨申请")
    @allure.title("调拨申请，门店向总部调拨，非紧俏品")
    def test_001(self, drivers):
        """调拨申请，门店向总部调拨，非紧俏品"""
        AllotPage = allotpage(drivers)
        PchsPage = pchspage(drivers)
        StockPage = stockpage(drivers)
        LoginPage = Loginpage(drivers)
        LoginPage.input_username("dfd")
        LoginPage.input_password("123456")
        LoginPage.click_loginButton()
        a = LoginPage.get_title()
        log.info(a)
        assert ("极配OMS系统" in a)
        AllotPage.click_allotmanager()
        AllotPage.click_allotdan()
        AllotPage.click_alloapply()
        AllotPage.click_alloadd()
        AllotPage.click_allotguest()
        AllotPage.input_allotguest('测试公司（总部）')
        AllotPage.click_allotguestsearch()
        AllotPage.doubleclick_wcgys()
        AllotPage.click_allotSkuadd()
        AllotPage.input_allotSku('02000034')
        AllotPage.click_allotSkusearch()
        AllotPage.doubleclick_allotsku()
        AllotPage.input_allotNum("5")
        AllotPage.click_allotSkusure()
        AllotPage.click_allotSkuclose()
        AllotPage.click_allotsave()
        AllotPage.click_allotadress()
        AllotPage.click_allotadressf()
        AllotPage.click_allotadressfzp()
        AllotPage.click_allotadresssave()
        AllotPage.click_allotcommit()
        AllotPage.click_allotcommitsure()
        status = AllotPage.allot_status()
        allotorderno = AllotPage.allot_orderno()
        try:
            assert '已受理' in status
            print('1，调拨申请单' + allotorderno, '提交成功')
        except Exception as e:
            print('1.调拨申请单，提交失败', format(e))


if __name__ == '__main__':
    import os
    pytest.main(['TestCase/test_pchswc.py', '--alluredir', './allure'])
    os.system('allure serve allure')
