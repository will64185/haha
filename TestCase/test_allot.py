#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.LoginPage import Loginpage
from page_object.PchsPage import pchspage
from page_object.StockPage import stockpage
from page_object.AllotPage import allotpage
from page_object.WMSPage import wmspage
from utils.times import sleep
import os


@allure.feature("调拨管理")
class TestAllot:
    @pytest.fixture(scope='function', autouse=True)
    def open_oms(self, drivers):
        """oms2.0,进入采购管理"""
        # LoginPage = Loginpage(drivers)
        # LoginPage.get_url(ini.url)
        # LoginPage.input_username("h1")
        # LoginPage.input_password("123456")
        # LoginPage.click_loginButton()
        # a = LoginPage.get_title()
        # log.info(a)
        # assert ("极配OMS系统" in a)

    @allure.story("调拨申请")
    @allure.title("调拨申请，门店向总部调拨，非紧俏品")
    def test_001(self, drivers):
        """调拨申请，门店向总部调拨，非紧俏品,提交后，总部自动受理"""
        AllotPage = allotpage(drivers)
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
            allotorderno = AllotPage.allot_orderno()
            LoginPage.click_shopName()
            LoginPage.input_shopName("测试公司（总部）")
            LoginPage.click_loginSearch()
            LoginPage.click_selectShop()
            LoginPage.click_shopSure()
            StockPage.click_stcok()
            StockPage.click_stcoksearch()
            StockPage.input_stockpartid('02000034')
            StockPage.click_stcokzero()
            StockPage.click_stcoksearch1()
            stock_outQty_before = StockPage.stock_outQty()
            LoginPage.click_shopName()
            LoginPage.input_shopName1("虹梅")
            LoginPage.click_loginSearch1()
            LoginPage.click_selectShop1()
            LoginPage.click_shopSure1()
            AllotPage.click_allotmanager()
            AllotPage.click_allotdan()
            AllotPage.click_alloapply()
            AllotPage.click_allotcommit()
            AllotPage.click_allotcommitsure()
            status = AllotPage.allot_status()
            LoginPage.click_shopName()
            LoginPage.input_shopName1("测试公司（总部）")
            LoginPage.click_loginSearch1()
            LoginPage.click_selectShop1()
            LoginPage.click_shopSure1()
            StockPage.click_stcok()
            StockPage.click_stcoksearch()
            StockPage.input_stockpartid('02000034')
            StockPage.click_stcokzero()
            StockPage.click_stcoksearch1()
            stock_outQty_after = StockPage.stock_outQty()
            outQty = int(stock_outQty_before) - int(stock_outQty_after)

            assert ('已受理' in status and outQty == 5)
            if '已受理' in status:
                print('1，调拨申请单' + allotorderno, '提交成功')
            else:
                print('1.调拨申请单，提交失败')
        else:
            print("异常")

    @allure.story("调拨申请")
    @allure.title("调拨申请，门店向总部调拨，受理后，wms部分发货并回传oms")
    def test_002(self, drivers):
        """调拨申请，门店向总部调拨，非紧俏品,提交后，总部自动受理,wms出库后回传oms"""
        AllotPage = allotpage(drivers)
        StockPage = stockpage(drivers)
        LoginPage = Loginpage(drivers)
        WMSPage = wmspage(drivers)
        LoginPage.click_shopName()
        LoginPage.input_shopName1("虹梅")
        LoginPage.click_loginSearch1()
        LoginPage.click_selectShop1()
        LoginPage.click_shopSure1()
        AllotPage.click_allotmanager()
        AllotPage.click_allotdan()
        AllotPage.click_alloapply()
        allotorderno = AllotPage.allot_orderno()
        LoginPage.click_shopName()
        LoginPage.input_shopName1("测试公司（总部）")
        LoginPage.click_loginSearch1()
        LoginPage.click_selectShop1()
        LoginPage.click_shopSure1()
        AllotPage.click_allotOut()
        AllotPage.click_allotOutMore()
        AllotPage.input_allotApplyOn(allotorderno)
        AllotPage.click_allotOutMoreSUre()
        allot_outOrderOn = AllotPage.allot_outOrderOn()
        StockPage.click_stcok()
        StockPage.click_stcoksearch()
        StockPage.input_stockpartid('02000034')
        StockPage.click_stcokzero()
        StockPage.click_stcoksearch1()
        stock_qty_before = StockPage.stock_qty()
        AllotPage.skip_second()
        # StockPage.open_newPage(ini.wms_url)
        # WMSPage.input_username("zw1")
        # WMSPage.input_password("123456")
        # WMSPage.click_loginButton()
        # WMSPage.click_system()
        # WMSPage.click_systemSet()
        # WMSPage.click_systemStore()
        # WMSPage.click_systemDefaultStore()
        WMSPage.click_enterManager()
        WMSPage.click_outManager()
        WMSPage.click_outTask()
        WMSPage.click_orderClass()
        WMSPage.click_allotOut()
        WMSPage.click_search()
        WMSPage.click_searchYewuNo()
        WMSPage.input_YewuNo(allot_outOrderOn)
        WMSPage.click_searchButton()
        WMSPage.click_sortinglistButton()
        WMSPage.click_sortinglist()
        WMSPage.click_sortingButton()
        WMSPage.input_sortingNum("4")
        WMSPage.click_sortingDetailSave()
        WMSPage.click_sortingOver()
        WMSPage.input_sortingRemark("少拣1个")
        WMSPage.click_sortingRemarkSave()
        WMSPage.click_packingTask()
        WMSPage.click_packingButton()
        WMSPage.click_oneKeyPacking()
        WMSPage.click_packingOver()
        WMSPage.click_packSureButton()
        WMSPage.click_deliveryList()
        WMSPage.click_deliveryManager()
        WMSPage.click_quickSearch()
        WMSPage.click_selectToday()
        WMSPage.click_deliveryButton()
        WMSPage.click_deliveryMethod()
        WMSPage.click_selfMentioned()
        WMSPage.click_deliverySureButton()
        WMSPage.click_deliverySureSure()
        WMSPage.click_outTask()
        wms_outStatus = WMSPage.wms_outStatus()
        AllotPage.skip_first()
        StockPage.click_stcoksearch1()
        stock_qty_after = StockPage.stock_qty()
        # AllotPage.click_allotmanager()
        # AllotPage.click_allotdan()
        AllotPage.click_allotOut()
        AllotPage.click_allotOutMore()
        AllotPage.input_allotApplyOn(allot_outOrderOn)
        AllotPage.click_allotOutMoreSUre()
        allot_allotStatus = AllotPage.allot_allotStatus()
        qty = int(stock_qty_before) - int(stock_qty_after)

        assert ('已完成' in wms_outStatus and '部分出库' in allot_allotStatus and qty == 4)
        if '部分出库' in allot_allotStatus:
            print('1，调拨出库单' + allot_outOrderOn, 'wms成功出库并回传oms，出库数量为4')
        else:
            print('1.调拨出库单，出库失败')


if __name__ == '__main__':
    import os

    pytest.main(['TestCase/test_pchswc.py', '--alluredir', './allure'])
    os.system('allure serve allure')
