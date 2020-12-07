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


@allure.feature("采购管理")
class TestPchsplan:
    @pytest.fixture(scope='function', autouse=True)
    def open_oms(self, drivers):
        """oms2.0,进入采购管理"""
        # LoginPage = Loginpage(drivers)
        # LoginPage.get_url(ini.url)

    @allure.story("滚动计划")
    @allure.title("滚动计划，添加配件")
    def test_001(self, drivers):
        """滚动计划，添加配件"""
        PchsPage = pchspage(drivers)
        LoginPage = Loginpage(drivers)
        LoginPage.input_username("zw1")
        LoginPage.input_password("123456")
        LoginPage.click_loginButton()
        a = LoginPage.get_title()
        log.info(a)
        assert ("极配OMS系统" in a)
        PchsPage.click_pchsguanli()
        PchsPage.click_pchsgundong()
        PchsPage.click_gdadd()
        PchsPage.click_gdselectsp()
        PchsPage.input_gdsupplier("上海测试有限公司2")
        PchsPage.click_gdsearch()
        PchsPage.doubleclick_gdgys()
        PchsPage.click_gdaddsku()
        PchsPage.input_gdsku("04006664")
        PchsPage.click_gdskusearch()
        PchsPage.doubleclick_gdsku()
        PchsPage.input_gdnum("5")
        PchsPage.input_gdprice("10")
        PchsPage.click_gdskusure()
        PchsPage.click_gdskuclose()
        PchsPage.click_gdsave()
        PchsPage.click_gdcommit()
        gdstatus = PchsPage.gdpchs_status()
        gdorderno = PchsPage.gdpchs_orderno()

        assert ('已审批' in gdstatus)
        if '已审批' in gdstatus:

            print('1，滚动计划单' + gdorderno, "已成功提交")
        else:
            print('1.滚动计划单，提交失败', )

    @allure.story("计划采购订单")
    @allure.title("计划采购订单")
    def test_002(self, drivers):
        """滚动计划，添加配件"""
        PchsPage = pchspage(drivers)
        StockPage = stockpage(drivers)
        LoginPage = Loginpage(drivers)
        a = LoginPage.login_name()
        if a != "测试公司（总部）":
            LoginPage.mouse_stop1()
            LoginPage.click_loginOut()
            LoginPage.input_username("zw1")
            LoginPage.input_password("123456")
            LoginPage.click_loginButton()
            a = LoginPage.get_title()
            log.info(a)
            assert ("极配OMS系统" in a)
            PchsPage.click_pchsguanli()
            PchsPage.click_pchsgundong()
            gdorderno = PchsPage.gdpchs_orderno()
            PchsPage.click_pchsplan()
            PchsPage.click_planadd()
            PchsPage.click_planselectsp()
            PchsPage.input_plansupplier("上海测试有限公司2")
            PchsPage.click_plansearch()
            PchsPage.doubleclick_plangys()
            PchsPage.click_planaddsku()
            PchsPage.input_plansku(gdorderno)
            PchsPage.click_planskusearch()
            PchsPage.click_planselectgd()
            PchsPage.click_planselect()
            # PchsPage.click_planskuNum()
            # PchsPage.input_planskuNum('4')
            PchsPage.click_plansave()
            # 检查在途库存
            StockPage.click_stcok()
            StockPage.click_stcoksearch()
            StockPage.input_stockpartid('04006664')
            StockPage.click_stcokzero()
            StockPage.click_stcoksearch1()
            OnRoadQty = StockPage.stock_onRoadQty()
            PchsPage.click_pchsplan()
            PchsPage.click_plancommit()
            PchsPage.click_plancommitsure()
            planStatus = PchsPage.planpchs_status()
            planOrderNo = PchsPage.planpchs_orderno()
            StockPage.click_stcoksearch()
            StockPage.click_stcoksearch1()
            OnRoadQty1 = StockPage.stock_onRoadQty()
            roadQty = int(OnRoadQty1) - int(OnRoadQty)
            assert ('待收货' in planStatus and roadQty == 5)
            if '已审批' in planStatus:

                print('1，计划采购订单' + planOrderNo, "已成功提交")
            else:
                print('1.计划采购订单，提交失败', )
        else:
            PchsPage.click_pchsguanli()
            PchsPage.click_pchsgundong()
            gdorderno = PchsPage.gdpchs_orderno()
            PchsPage.click_pchsplan()
            PchsPage.click_planadd()
            PchsPage.click_planselectsp()
            PchsPage.input_plansupplier("上海测试有限公司2")
            PchsPage.click_plansearch()
            PchsPage.doubleclick_plangys()
            PchsPage.click_planaddsku()
            PchsPage.input_plansku(gdorderno)
            PchsPage.click_planskusearch()
            PchsPage.click_planselectgd()
            PchsPage.click_planselect()
            # PchsPage.click_planskuNum()
            # PchsPage.input_planskuNum('4')
            PchsPage.click_plansave()
            # 检查在途库存
            StockPage.click_stcok()
            StockPage.click_stcoksearch()
            StockPage.input_stockpartid('04006664')
            StockPage.click_stcokzero()
            StockPage.click_stcoksearch1()
            OnRoadQty = StockPage.stock_onRoadQty()
            PchsPage.click_pchsplan()
            PchsPage.click_plancommit()
            PchsPage.click_plancommitsure()
            planStatus = PchsPage.planpchs_status()
            print(planStatus)
            planOrderNo = PchsPage.planpchs_orderno()
            StockPage.click_stcoksearch()
            StockPage.click_stcoksearch1()
            OnRoadQty1 = StockPage.stock_onRoadQty()
            roadQty = int(OnRoadQty1) - int(OnRoadQty)
            print(roadQty)
            assert ('待收货' in planStatus and roadQty == 5)
            if '待收货' in planStatus:
                print('1，计划采购订单' + planOrderNo, "已成功提交")
            else:
                print('1.计划采购订单，提交失败', )


if __name__ == '__main__':
    import os

    pytest.main(['TestCase/test_pchsplan.py', '--alluredir', './allure'])
    os.system('allure serve allure')
