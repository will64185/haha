#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

allot = Element('allot')


class allotpage(WebPage):
    """调拨管理"""

    def click_allotmanager(self):
        """调拨管理"""
        self.is_click(allot['调拨管理'])

    # 调拨申请
    def click_allotdan(self):
        """调拨单"""
        self.is_click(allot['调拨单'])

    def click_alloapply(self):
        """调拨申请"""
        self.is_click(allot['调拨申请'])
        sleep()

    def click_alloadd(self):
        """调拨申请新增"""
        self.is_click(allot['调拨申请新增'])

    def click_allotguest(self):
        """调拨申请选择调出方"""
        self.is_click(allot['调拨申请选择调出方'])

    def input_allotguest(self, content):
        """调拨申请输入调出方"""
        self.input_text(allot['调拨申请输入调出方'], txt=content)

    def click_allotguestsearch(self):
        """调拨申请点击查询"""
        self.is_click(allot['调拨申请点击查询'])

    def doubleclick_wcgys(self):
        """调拨申请双击调出方"""
        self.is_doubleclick(allot['调拨申请双击调出方'])
        sleep()

    def click_allotSkuadd(self):
        """调拨申请点击添加配件"""
        self.is_click(allot['调拨申请点击添加配件'])

    def input_allotSku(self, content):
        """调拨申请输入配件"""
        self.input_text(allot['调拨申请输入配件'], txt=content)

    def click_allotSkusearch(self):
        """点击配件查询"""
        self.is_click(allot['点击配件查询'])
        self.driver.implicitly_wait(10)

    def doubleclick_allotsku(self):
        """调拨申请双击配件"""
        self.is_doubleclick(allot['调拨申请双击配件'])
        sleep()

    def input_allotNum(self, content):
        """输入调拨数量"""
        self.input_text(allot['输入调拨数量'], txt=content)

    def click_allotSkusure(self):
        """输入数量点击确定"""
        self.is_click(allot['输入数量点击确定'])

    def click_allotSkuclose(self):
        """关闭添加配件弹框"""
        self.is_click(allot['关闭添加配件弹框'])

    def click_allotsave(self):
        """调拨申请点击保存"""
        self.is_click(allot['调拨申请点击保存'])
        sleep(3)

    def click_allotadress(self):
        """调拨申请编辑收货信息"""
        self.is_click(allot['调拨申请编辑收货信息'])

    def click_allotadressf(self):
        """选择配送方式"""
        self.is_click(allot['选择配送方式'])

    def click_allotadressfzp(self):
        """选择自配"""
        self.is_click(allot['选择自配'])

    def click_allotadresssave(self):
        """配送方式点击保存"""
        self.is_click(allot['配送方式点击保存'])

    def click_allotcommit(self):
        """点击提交"""
        self.is_click(allot['点击提交'])
        sleep()

    def click_allotcommitsure(self):
        """调拨申请提交确定"""
        self.is_click(allot['调拨申请提交确定'])
        sleep(3)

    def allot_status(self):
        """调拨申请单状态"""
        stock_qty = self.element_text(allot['调拨申请单状态'])
        return stock_qty

    def allot_orderno(self):
        """调拨申请单号"""
        stock_outQty = self.element_text(allot['调拨申请单号'])
        return stock_outQty

    def click_allotOut(self):
        """调出调拨出库"""
        self.is_click(allot['调出调拨出库'])
        sleep(3)

    def click_allotOutMore(self):
        """调出更多"""
        self.is_click(allot['调出更多'])

    def input_allotOutOn(self, content):
        """调出输入受理单号"""
        self.input_text(allot['调出输入受理单号'], txt=content)

    def click_allotOutMoreSUre1(self):
        """调出更多确定1"""
        self.is_click(allot['调出更多确定1'])
        sleep(3)

    def input_allotApplyOn(self, content):
        """调出输入申请单号"""
        self.input_text(allot['调出输入申请单号'], txt=content)

    def click_allotOutMoreSUre(self):
        """调出更多确定"""
        self.is_click(allot['调出更多确定'])
        sleep(2)

    def allot_allotStatus(self):
        """调出获取状态"""
        allot_allotStatus = self.element_text(allot['调出获取状态'])
        return allot_allotStatus

    def allot_outOrderOn(self):
        """调出获取单号"""
        allot_outOrderOn = self.element_text(allot['调出获取单号'])
        return allot_outOrderOn

    def click_allotOutOrder(self):
        """调出点击调拨出库单"""
        self.is_click(allot['调出点击调拨出库单'])
        sleep()

    def allot_allotOutCancelNum(self):
        """调出获取取消数量"""
        allot_allotOutCancelNum = self.element_text(allot['调出获取取消数量'])
        return allot_allotOutCancelNum





if __name__ == '__main__':
    pass
