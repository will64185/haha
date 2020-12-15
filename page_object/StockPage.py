#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

search = Element('stock')


class stockpage(WebPage):
    """库存管理"""

    def click_stcok(self):
        """库存管理库"""
        self.is_click(search['库存管理'])

    def click_stcoksearch(self):
        """库存查询"""
        self.is_click(search['库存查询'])

    def input_stockpartid(self, content):
        """内码输入"""
        self.input_text(search['内码输入'], txt=content)

    def click_stcokzero(self):
        """勾选显示零库存"""
        self.is_click(search['勾选显示零库存'])

    def click_stcoksearch1(self):
        """库存点击查询"""
        self.is_click(search['库存点击查询'])
        sleep(3)

    def stock_qty(self):
        """库存数量"""
        stock_qty = self.element_text(search['库存数量'])
        return stock_qty

    def stock_outQty(self):
        """可售数量"""
        stock_outQty = self.element_text(search['可售数量'])
        return stock_outQty

    def stock_onRoadQty(self):
        """合计在途库存"""
        stock_outQty = self.element_text(search['合计在途库存'])
        return stock_outQty

    def click_stockSku(self):
        """汇总库存"""
        self.is_click(search['汇总库存'])
        sleep()

    def click_batchSku(self):
        """批次配件"""
        self.is_click(search['批次配件'])
        sleep()

    def input_stockCode(self, content):
        """批次编码输入"""
        self.input_text(search['批次编码输入'], txt=content)

    def click_batchSkuZero(self):
        """批次显示零库存"""
        self.is_click(search['批次显示零库存'])

    def click_batchSkuSearch(self):
        """批次查询"""
        self.is_click(search['批次查询'])
        sleep(3)

    def click_batchSkuDateAscending(self):
        """批次入库日期升序排序"""
        self.is_click(search['批次入库日期升序排序'])
        sleep(5)

    def batchStock_qty(self):
        """批次库存"""
        batchStock_qty = self.element_text(search['批次库存'])
        return batchStock_qty

    def batchStock_outQty(self):
        """批次可售库存"""
        batchStock_outQty = self.element_text(search['批次可售库存'])
        return batchStock_outQty







if __name__ == '__main__':
    pass
