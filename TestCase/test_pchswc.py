#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.LoginPage import Loginpage
from page_object.PchsPage import pchspage
from page_object.StockPage import stockpage
from utils.times import sleep
import os


@allure.feature("采购管理")
class TestPchswc:
    @pytest.fixture(scope='function', autouse=True)
    def open_oms(self, drivers):
        """oms2.0,进入采购管理"""
        # LoginPage = Loginpage(drivers)
        # LoginPage.input_username("h1")
        # LoginPage.input_password("123456")
        # LoginPage.click_loginButton()
        # a = LoginPage.get_title()
        # log.info(a)
        # assert ("极配OMS系统" in a)

    @allure.story("外采订单")
    @allure.title("外采订单，添加配件")
    def test_001(self, drivers):
        """外采订单，添加配件"""
        PchsPage = pchspage(drivers)
        StockPage = stockpage(drivers)
        LoginPage = Loginpage(drivers)
        a = LoginPage.login_name()
        if a != "XXX":
            LoginPage.mouse_stop1()
            LoginPage.click_loginOut()
            LoginPage.input_username("h1")
            LoginPage.input_password("123456")
            LoginPage.click_loginButton()
            a = LoginPage.get_title()
            log.info(a)
            assert ("极配OMS系统" in a)
            PchsPage.click_pchsguanli()
            PchsPage.click_pchswaicai()
            PchsPage.click_wcadd()
            PchsPage.click_wcselectsp()
            PchsPage.input_supplier('上海测试有限公司')
            PchsPage.click_wcsearch()
            PchsPage.doubleclick_wcgys()
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
            # try:
            #     assert ('全部入库1' in stastus and a == 5 and b == 5)
            #     print('1，外采订单' + pchswcno, '已成功入库，入库数量5')
            # except Exception as e:
            #     print('1.外采订单，提交失败', format(e))
            assert ('全部入库' in stastus and a == 5 and b == 5)
            if '全部入库' in stastus and a == 5 and b == 5:
                print('1，外采订单' + pchswcno, '已成功入库，入库数量5')
            else:
                print('1.外采订单，提交失败', )
        else:
            print("异常")

    @allure.story("采购退货")
    @allure.title("门店-采购退货，添加配件")
    def test_002(self, drivers):
        """门店采购退货，添加配件，提交退货"""
        PchsPage = pchspage(drivers)
        StockPage = stockpage(drivers)
        LoginPage = Loginpage(drivers)
        # LoginPage.input_username("h1")
        # LoginPage.input_password("123456")
        # LoginPage.click_loginButton()
        a = LoginPage.login_name()
        if a != "XXX":
            LoginPage.mouse_stop1()
            LoginPage.click_loginOut()
            LoginPage.input_username("h1")
            LoginPage.input_password("123456")
            LoginPage.click_loginButton()
            StockPage.click_stcok()
            StockPage.click_stcoksearch()
            StockPage.input_stockpartid('05001221')
            StockPage.click_stcokzero()
            StockPage.click_stcoksearch1()
            stock_qty_before = StockPage.stock_qty()
            stock_outQty_before = StockPage.stock_outQty()
            PchsPage.click_pchsguanli()
            PchsPage.click_pchsReturn()
            PchsPage.click_pchsReturnAdd()
            PchsPage.input_pchsReturnInputSupplier("上海测试有限公司")
            PchsPage.enter_pchsReturnInputSupplier()
            PchsPage.click_pchsReturnChooseSupplier()
            PchsPage.click_pchsReturnReason()
            PchsPage.click_pchsReturnSelectReason()
            PchsPage.click_pchsReturnSku()
            PchsPage.input_pchsReturnInputPartId("05001221")
            PchsPage.click_pchsReturnSkuSearch()
            PchsPage.click_pchsReturnEnterOrder()
            PchsPage.click_pchsReturnSelectButton()
            PchsPage.click_pchsReturnCloseButton()
            PchsPage.click_pchsReturnSave()
            PchsPage.click_pchsReturnCommit()
            PchsPage.click_pchsReturnCommitSure()
            PchsPage.click_pchsReturnButton()
            PchsPage.click_pchsReturnSure()
            pchsReturn_returnNum = PchsPage.pchsReturn_returnNum()
            pchsReturn_status = PchsPage.pchsReturn_status()
            pchsReturn_orderno = PchsPage.pchsReturn_orderno()
            StockPage.click_stcoksearch()
            StockPage.click_stcoksearch1()
            stock_qty_after = StockPage.stock_qty()
            stock_outQty_after = StockPage.stock_outQty()
            qty = int(stock_qty_before) - int(stock_qty_after)
            outQty = int(stock_outQty_before) - int(stock_outQty_after)
            assert ('已退货' in pchsReturn_status and qty == int(pchsReturn_returnNum))
            if '已退货' in pchsReturn_status and outQty == int(pchsReturn_returnNum):
                print('1，外采订单' + pchsReturn_orderno, '已成功入库，入库数量5')
            else:
                print('1.外采订单，提交失败', )


if __name__ == '__main__':
    import os

    pytest.main(['TestCase/test_pchswc.py', '--alluredir', './allure'])
    os.system('allure serve allure')
