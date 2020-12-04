#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

search = Element('search')


class pchspage(WebPage):
    """采购管理"""

    def click_pchsguanli(self):
        """点击采购管理"""
        self.is_click(search['采购管理'])
        sleep()

    # 外采订单
    def click_pchswaicai(self):
        """点击外采订单"""
        self.is_click(search['外采订单'])
        sleep(2)

    def click_wcadd(self):
        """点击新增按钮"""
        self.is_click(search['新增按钮'])

    def click_wcselectsp(self):
        """点击选择供应商按钮"""
        self.is_click(search['选择供应商按钮'])

    def input_supplier(self, content):
        """输入供应商"""
        self.input_text(search['输入供应商弹框'], txt=content)

    def click_wcsearch(self):
        """点击选择供应商按钮"""
        self.is_click(search['查询供应商按钮'])

    def doubleclick_wcgys(self):
        """双击选择供应商"""
        self.is_doubleclick(search['双击选择供应商'])

    def click_waaddsku(self):
        """点击添加配件"""
        self.is_click(search['点击添加添加配件'])

    def input_wcsku(self, content):
        """输入内码"""
        self.input_text(search['输入内码'], txt=content)

    def click_wcskusearch(self):
        """点击查询"""
        self.is_click(search['点击查询'])

    def doubleclick_wcsku(self):
        """双击内码"""
        self.is_doubleclick(search['双击内码'])

    def input_wcnum(self, content):
        """输入数量"""
        self.input_text(search['输入数量'], txt=content)

    def input_wcprice(self, content):
        """输入采购价格"""
        self.input_text(search['输入采购价格'], txt=content)

    def click_wcskusure(self):
        """点击确定按钮"""
        self.is_click(search['点击确定按钮'])

    def click_wcskuclose(self):
        """关闭添加配件弹框"""
        self.is_click(search['关闭添加配件弹框'])

    def click_wcsave(self):
        """外采订单-保存"""
        self.is_click(search['保存'])

    def click_wccommit(self):
        """外采订单-提交并入库"""
        self.is_click(search['提交并入库'])

    def click_wccommitsure(self):
        """提交确定"""
        self.is_click(search['提交确定'])
        sleep(6)

    def wcpchs_status(self):
        """外采订单状态"""
        wcpchs_status = self.element_text(search['外采订单状态'])
        return wcpchs_status

    def wcpchs_orderno(self):
        """外采单号"""
        wcpchs_orderno = self.element_text(search['外采单号'])
        return wcpchs_orderno

    def click_wcimport(self):
        """导入"""
        self.is_click(search['导入'])

    def click_wcpartidimport(self):
        """配件内码导入"""
        self.is_click(search['配件内码导入'])
        sleep(2)



if __name__ == '__main__':
    pass
