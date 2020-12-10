#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

wms = Element('wms')


class wmspage(WebPage):
    """wms-登录界面"""

    def input_username(self, content):
        """输入账号"""
        self.input_text(wms['wms用户名'], txt=content)

    def input_password(self, content):
        """输入密码"""
        self.input_text(wms['wms密码'], txt=content)

    def click_loginButton(self):
        """点击登录"""
        self.is_click(wms['wms登录'])
        sleep(2)

    def click_system(self):
        """wms系统管理"""
        self.is_click(wms['wms系统管理'])

    def click_systemSet(self):
        """wms系统设置"""
        self.is_click(wms['wms系统设置'])

    def click_systemStore(self):
        """wms默认仓"""
        self.is_click(wms['wms默认仓'])

    def click_systemDefaultStore(self):
        """wms选择默认仓库"""
        self.is_click(wms['wms选择默认仓库'])

    def click_enterManager(self):
        """wms入库管理"""
        self.is_click(wms['wms入库管理'])

    def click_enterTask(self):
        """wms入库任务"""
        self.is_click(wms['wms入库任务'])
        sleep(2)

    def click_orderType(self):
        """wms选择订单类型"""
        self.is_click(wms['wms选择订单类型'])

    def click_selectPchsEnter(self):
        """wms选择采购入库"""
        self.is_click(wms['wms选择采购入库'])

    def click_select(self):
        """wms选择查询条件"""
        self.is_click(wms['wms选择查询条件'])

    def click_yewuNo(self):
        """wms选择业务单号"""
        self.is_click(wms['wms选择业务单号'])

    def input_yewuNo(self, content):
        """wms输入业务单号"""
        self.input_text(wms['wms输入业务单号'], txt=content)

    def click_enterTaskSearch(self):
        """wms入库任务查询"""
        self.is_click(wms['wms入库任务查询'])
        sleep()

    def click_selectEnterNo(self):
        """wms选择入库单号"""
        self.is_click(wms['wms选择入库单号'])

    def click_BatchReceiving(self):
        """wms点击批量收货"""
        self.is_click(wms['wms点击批量收货'])
        sleep(2)

    def obtain_enterNo(self):
        """wms获取入库单号"""
        obtain_enterNo = self.element_text(wms['wms获取入库单号'])
        return obtain_enterNo

    def click_receivingManager(self):
        """wms收货管理"""
        self.is_click(wms['wms收货管理'])
        sleep(2)

    def click_receivingSelectNo(self):
        """wms收货管理选择单据"""
        self.is_click(wms['wms收货管理选择单据'])

    def click_confirmArrival(self):
        """wms点击确认到货"""
        self.is_click(wms['wms点击确认到货'])

    def click_confirmArrivalSure(self):
        """wms确认到货确定"""
        self.is_click(wms['wms确认到货确定'])

    def click_receivingNo(self):
        """wms点击收货单号"""
        self.is_click(wms['wms点击收货单号'])
        sleep()

    def click_receivingOneKey(self):
        """wms点击一键收货"""
        self.is_click(wms['wms点击一键收货'])
        sleep()

    def click_receivingSure(self):
        """wms点击确定"""
        self.is_click(wms['wms点击确定'])
        sleep(2)

    def click_receivingOver(self):
        """wms点击收货完成"""
        self.is_click(wms['wms点击收货完成'])

    def click_receivingSure1(self):
        """wms点击确定1"""
        self.is_click(wms['wms点击确定1'])
        sleep(2)

    def click_shangjiaOrder(self):
        """wms点击生成上架单"""
        self.is_click(wms['wms点击生成上架单'])
        sleep(2)

    def click_shangjiaManager(self):
        """wms点击上架管理"""
        self.is_click(wms['wms点击上架管理'])
        sleep(1)

    def click_shangjiaNo(self):
        """wms点击上架单号"""
        self.is_click(wms['wms点击上架单号'])
        sleep(2)

    def click_shangjiaOver(self):
        """wms点击上架完成"""
        self.is_click(wms['wms点击上架完成'])

    def click_shangjiaOverSure(self):
        """WMS确认上架确定"""
        self.is_click(wms['WMS确认上架确定'])
        sleep()

    def ruku_status(self):
        """WMS入库单状态"""
        ruku_status = self.element_text(wms['WMS入库单状态'])
        return ruku_status
