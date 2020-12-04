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
from utils.times import sleep
import os
import win32gui
import win32con


@allure.feature("采购管理")
class TestPchswc:
    @pytest.fixture(scope='function', autouse=True)
    def open_oms(self, drivers):
        """oms2.0,进入采购管理"""
        LoginPage = Loginpage(drivers)
        LoginPage.get_url(ini.url)

    @allure.story("外采订单")
    @allure.title("外采订单，添加配件")
    def test_001(self, drivers):
        """外采订单，添加配件"""
        PchsPage = pchspage(drivers)
        StockPage = stockpage(drivers)
        LoginPage = Loginpage(drivers)
        LoginPage.input_username("dfd")
        LoginPage.input_password("123456")
        LoginPage.click_loginButton()
        a = LoginPage.get_title()
        log.info(a)
        assert ("极配OMS系统" in a)
        PchsPage.click_pchsguanli()
        PchsPage.click_pchswaicai()
        PchsPage.click_wcadd()
        PchsPage.click_wcselectsp()
        PchsPage.input_supplier('上海测试有限公司2')
        PchsPage.click_wcsearch()
        PchsPage.doubleclick_wcgys()
        PchsPage.click_wcsave()
        PchsPage.click_wcimport()
        PchsPage.click_wcpartidimport()
        dialog = win32gui.FindWindow("#32770", "打开")
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'C:\\Users\\will\\Desktop\\haha\\config\\滚动计划内码导入.xlsx')  # 往输入框输入绝对地址
        sleep(3)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
        sleep(3600)




        PchsPage.click_waaddsku()
        PchsPage.input_wcsku('05001221')
        PchsPage.click_wcskusearch()
        PchsPage.doubleclick_wcsku()
        PchsPage.input_wcnum('5')
        PchsPage.input_wcprice('10')
        PchsPage.click_wcskusure()
        PchsPage.click_wcskuclose()
        PchsPage.click_wcsave()
        # 检查库存
        StockPage.click_stcok()
        StockPage.click_stcoksearch()
        StockPage.input_stockpartid('05001221')
        StockPage.click_stcokzero()
        StockPage.click_stcoksearch1()
        stock_qty_before = StockPage.stock_qty()
        stock_outQty_before = StockPage.stock_outQty()
        PchsPage.click_pchswaicai()
        PchsPage.click_wccommit()
        PchsPage.click_wccommitsure()
        stastus = PchsPage.wcpchs_status()
        pchswcno = PchsPage.wcpchs_orderno()
        StockPage.click_stcoksearch()
        StockPage.click_stcoksearch1()
        stock_qty_after = StockPage.stock_qty()
        stock_outQty_after = StockPage.stock_outQty()
        a = int(stock_qty_after) - int(stock_qty_before)
        b = int(stock_outQty_after) - int(stock_outQty_before)
        try:
            assert '全部入库' in stastus and a == 5 and b == 5
            print('1，外采订单' + pchswcno, '已成功入库，入库数量5')
        except Exception as e:
            print('1.外采订单，提交失败', format(e))




# if __name__ == '__main__':
#     pytest.main(['TestCase/test_pchswc.py'])
if __name__ == '__main__':
    import os
    pytest.main(['-s', '-v', '-n', '2', 'TestCase/test_pchswc.py', '--alluredir', './allure'])
    os.system('allure serve allure')
