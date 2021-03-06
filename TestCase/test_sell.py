#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.LoginPage import Loginpage
from page_object.PchsPage import pchspage
from page_object.StockPage import stockpage
from page_object.SellPage import Sellpage

from utils.times import sleep
import os


@allure.feature("销售管理")
class TestPchswc:
    @pytest.fixture(scope='function', autouse=True)
    def open_oms(self, drivers):
        """oms2.0,进入销售管理"""
        # LoginPage = Loginpage(drivers)
        # LoginPage.input_username("h1")
        # LoginPage.input_password("123456")
        # LoginPage.click_loginButton()
        # a = LoginPage.get_title()
        # log.info(a)
        # assert ("极配OMS系统" in a)

    @allure.story("销售订单")
    @allure.title("门店销售订单，添加配件，保存并出库")
    def test_001(self, drivers):
        """门店销售订单，添加配件，保存占用可售数量，出库减库存数量"""
        StockPage = stockpage(drivers)
        LoginPage = Loginpage(drivers)
        a = LoginPage.login_name()
        SellPage = Sellpage(drivers)
        if a != "XXX":
            LoginPage.mouse_stop1()
            LoginPage.click_loginOut()
            LoginPage.input_username("h1")
            LoginPage.input_password("123456")
            LoginPage.click_loginButton()
            a = LoginPage.get_title()
            log.info(a)
            assert ("极配OMS系统" in a)
            StockPage.click_stcok()
            StockPage.click_stcoksearch()
            StockPage.input_stockpartid('05001221')
            StockPage.click_stcokzero()
            StockPage.click_stcoksearch1()
            stock_qty_before = StockPage.stock_qty()
            stock_outQty_before = StockPage.stock_outQty()
            SellPage.click_sellManager()
            SellPage.click_sellOrder()
            SellPage.click_sellAdd()
            SellPage.input_sellGuest("一号协议客户")
            SellPage.enter_guest()
            SellPage.click_sellSelectGuest()
            SellPage.click_sellAddSku()
            SellPage.input_sellInputPartId("05001221")
            SellPage.click_sellSkusearch()
            SellPage.doubleClick_sellSKu()
            SellPage.input_sellNum("10")
            SellPage.input_sellPrice("11")
            SellPage.click_sellSkuSure()
            SellPage.click_sellCancel()
            SellPage.click_sellSave()
            StockPage.click_stcoksearch()
            StockPage.click_stcoksearch1()
            stock_outQty_after = StockPage.stock_outQty()
            SellPage.click_sellOrder()
            SellPage.click_sellCommit()
            SellPage.click_sellCommitSure()
            SellPage.click_sellOut()
            SellPage.click_sellOutSure()
            sell_Status = SellPage.sell_Status()
            sell_orderNo = SellPage.sell_orderNo()
            StockPage.click_stcoksearch()
            StockPage.click_stcoksearch1()
            stock_qty_after = StockPage.stock_qty()
            outQty = int(stock_outQty_before) - int(stock_outQty_after)
            qty = int(stock_qty_before) - int(stock_qty_after)
            assert ('已出库' in sell_Status and outQty == 10 and qty == 10)
            if '已出库' in sell_Status and outQty == 10 and qty == 10:

                print('1，销售订单' + sell_orderNo, '已成功出库，出库数量10')
            else:
                print('1.销售订单，出库失败', )

    @allure.story("销售订单")
    @allure.title("门店销售订单，添加批次配件，保存并出库")
    def test_002(self, drivers):
        """门店销售订单，添加批次配件，保存占用可售数量以及批次的可售库存，出库减库存数量"""
        SellPage = Sellpage(drivers)
        StockPage = stockpage(drivers)
        StockPage.click_stcoksearch1()
        stock_qty_before = StockPage.stock_qty()
        stock_outQty_before = StockPage.stock_outQty()
        StockPage.click_batchSku()
        StockPage.input_stockCode("05001221")
        StockPage.click_batchSkuSearch()
        StockPage.click_batchSkuDateAscending()
        batchStock_qty_before = StockPage.batchStock_qty()
        batchStock_outQty_before = StockPage.batchStock_outQty()
        SellPage.click_sellOrder()
        SellPage.click_sellAdd()
        SellPage.input_sellGuest("一号协议客户")
        SellPage.enter_guest()
        SellPage.click_sellSelectGuest()
        SellPage.click_batchSku()
        SellPage.input_batchCode("05001221")
        SellPage.click_batchSkuSearch()
        SellPage.click_batchSelectSku()
        SellPage.click_batchSkuSelect()
        SellPage.click_batchSkuNum()
        SellPage.input_batchSkuNum("5")
        SellPage.click_sellSave()
        StockPage.click_stcoksearch()
        StockPage.click_batchSkuSearch()
        batchStock_outQty_after = StockPage.batchStock_outQty()
        StockPage.click_stockSku()
        StockPage.click_stcoksearch1()
        stock_outQty_after = StockPage.stock_outQty()
        SellPage.click_sellOrder()
        SellPage.click_sellCommit()
        SellPage.click_sellCommitSure()
        SellPage.click_sellOut()
        SellPage.click_sellOutSure()
        sell_Status = SellPage.sell_Status()
        sell_orderNo = SellPage.sell_orderNo()
        StockPage.click_stcoksearch()
        StockPage.click_stcoksearch1()
        stock_qty_after = StockPage.stock_qty()
        StockPage.click_batchSku()
        StockPage.click_batchSkuZero()
        StockPage.click_batchSkuSearch()
        batchStock_qty_after = StockPage.batchStock_qty()
        stock_outQty = int(stock_outQty_before) - int(stock_outQty_after)
        batchStock_outQty = int(batchStock_outQty_before) - int(batchStock_outQty_after)
        stock_qty = int(stock_qty_before) - int(stock_qty_after)
        batchStock_qty = int(batchStock_qty_before) - int(batchStock_qty_after)
        assert ('已出库' in sell_Status and stock_outQty == 5 and batchStock_outQty == 5
                and stock_qty == 5 and batchStock_qty == 5)
        if ('已出库' in sell_Status and stock_outQty == 5 and batchStock_outQty == 5
                and stock_qty == 5 and batchStock_qty == 5):
            print('1，销售订单' + sell_orderNo, '已成功出库，出库数量5')
        else:
            print('1.销售订单，出库失败', )

    @allure.story("销售订单")
    @allure.title("门店销售订单，选择入库单，保存并出库")
    def test_003(self, drivers):
        """门店销售订单，选择入库单，保存占用可售数量以及批次的可售库存，出库减库存数量"""
        SellPage = Sellpage(drivers)
        LoginPage = Loginpage(drivers)
        # LoginPage.input_username("h1")
        # LoginPage.input_password("123456")
        # LoginPage.click_loginButton()
        a = LoginPage.get_title()
        log.info(a)
        assert ("极配OMS系统" in a)
        if a != "XXX":
            StockPage = stockpage(drivers)
            LoginPage.mouse_stop1()
            LoginPage.click_loginOut()
            LoginPage.input_username("h1")
            LoginPage.input_password("123456")
            LoginPage.click_loginButton()
            a = LoginPage.get_title()
            log.info(a)
            assert ("极配OMS系统" in a)
            StockPage.click_stcok()
            StockPage.click_stcoksearch()
            StockPage.input_stockpartid('05001221')
            StockPage.click_stcokzero()
            StockPage.click_stcoksearch1()
            stock_qty_before = StockPage.stock_qty()
            stock_outQty_before = StockPage.stock_outQty()
            StockPage.click_batchSku()
            StockPage.input_stockCode("05001221")
            StockPage.click_batchSkuSearch()
            batchStock_qty_before = StockPage.batchStock_qty()
            batchStock_outQty_before = StockPage.batchStock_outQty()
            SellPage.click_sellManager()
            SellPage.click_sellOrder()
            SellPage.click_sellAdd()
            SellPage.input_sellGuest("一号协议客户")
            SellPage.enter_guest()
            SellPage.click_sellSelectGuest()
            SellPage.click_enterOrder()
            SellPage.click_outEnterOrder()
            SellPage.click_selectEnterOrder()
            SellPage.click_enterOrderCost()
            # SellPage.click_outNum()
            # SellPage.input_outNum("1")
            SellPage.click_sellSave()
            StockPage.click_stcoksearch()
            StockPage.click_batchSkuSearch()
            batchStock_outQty_after = StockPage.batchStock_outQty()
            StockPage.click_stockSku()
            StockPage.click_stcoksearch1()
            stock_outQty_after = StockPage.stock_outQty()
            SellPage.click_sellOrder()
            SellPage.click_sellCommit()
            SellPage.click_sellCommitSure()
            SellPage.click_sellOut()
            SellPage.click_sellOutSure()
            sell_Status = SellPage.sell_Status()
            sell_orderNo = SellPage.sell_orderNo()
            StockPage.click_stcoksearch()
            StockPage.click_stcoksearch1()
            stock_qty_after = StockPage.stock_qty()
            StockPage.click_batchSku()
            StockPage.click_batchSkuZero()
            StockPage.click_batchSkuSearch()
            batchStock_qty_after = StockPage.batchStock_qty()
            stock_outQty = int(stock_outQty_before) - int(stock_outQty_after)
            batchStock_outQty = int(batchStock_outQty_before) - int(batchStock_outQty_after)
            stock_qty = int(stock_qty_before) - int(stock_qty_after)
            batchStock_qty = int(batchStock_qty_before) - int(batchStock_qty_after)
            assert ('已出库' in sell_Status and stock_outQty == 5 and batchStock_outQty == 5
                    and stock_qty == 5 and batchStock_qty == 5)
            if ('已出库' in sell_Status and stock_outQty == 5 and batchStock_outQty == 5
                    and stock_qty == 5 and batchStock_qty == 5):
                print('1，销售订单' + sell_orderNo, '已成功出库，出库数量5')
            else:
                print('1.销售订单，出库失败', )

    @allure.story("销售退货")
    @allure.title("销售退货，添加配件，销退入库")
    def test_004(self, drivers):
        """销售退货，添加配件，销退入库"""
        SellPage = Sellpage(drivers)
        LoginPage = Loginpage(drivers)
        # LoginPage.input_username("h1")
        # LoginPage.input_password("123456")
        # LoginPage.click_loginButton()
        a = LoginPage.get_title()
        log.info(a)
        assert ("极配OMS系统" in a)
        if a != "XXX":
            StockPage = stockpage(drivers)
            LoginPage.mouse_stop1()
            LoginPage.click_loginOut()
            LoginPage.input_username("h1")
            LoginPage.input_password("123456")
            LoginPage.click_loginButton()
            a = LoginPage.get_title()
            log.info(a)
            assert ("极配OMS系统" in a)
            StockPage.click_stcok()
            StockPage.click_stcoksearch()
            StockPage.input_stockpartid('05001221')
            StockPage.click_stcokzero()
            StockPage.click_stcoksearch1()
            stock_qty_before = StockPage.stock_qty()
            stock_outQty_before = StockPage.stock_outQty()
            SellPage.click_sellManager()
            SellPage.click_salesReturns()
            SellPage.salesReturnsAdd()
            SellPage.input_salesReturnsGuest("一号协议客户")
            SellPage.enter_salesReturnsGuest()
            SellPage.click_salesReturnsGuest()
            SellPage.click_salesReturnsReason()
            SellPage.click_salesReturnsChooseReason()
            SellPage.click_salesReturnsAddSku()
            SellPage.input_salesReturnsInputPartId("05001221")
            SellPage.click_salesReturnsSearch()
            SellPage.click_salesReturnsSku1()
            SellPage.click_salesReturnsSku2()
            SellPage.click_salesReturnsSku3()
            SellPage.click_click_salesReturnsChoose()
            SellPage.click_click_salesReturnsClose()
            SellPage.click_click_salesReturnsSave()
            SellPage.click_click_salesReturnsCommit()
            SellPage.click_click_salesReturnsCommitSure()
            salesReturns_Status = SellPage.salesReturns_Status()
            salesReturns_orderNo = SellPage.salesReturns_orderNo()
            StockPage.click_stcoksearch()
            StockPage.click_stcoksearch1()
            stock_qty_after = StockPage.stock_qty()
            stock_outQty_after = StockPage.stock_outQty()
            qty = int(stock_qty_after) - int(stock_qty_before)
            outQty = int(stock_outQty_after) - int(stock_outQty_before)
            assert ('已入库' in salesReturns_Status and qty == 15 and outQty == 15)
            if ('已入库' in salesReturns_Status
                    and qty == 15 and outQty == 15):
                print('1，销售退货单号' + salesReturns_orderNo, '已成功入库，入库数量5')
            else:
                print('1.销售退货，入库失败', )


if __name__ == '__main__':
    import os

    pytest.main(['TestCase/test_sell.py', '--alluredir', './allure'])
    os.system('allure serve allure')
