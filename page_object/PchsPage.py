#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

search = Element('pchs')


class pchspage(WebPage):
    """采购管理"""

    def click_pchsguanli(self):
        """点击采购管理"""
        self.is_click(search['采购管理'])
        sleep(2)

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
        sleep(2)

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

    """滚动计划"""

    def click_pchsgundong(self):
        """滚动计划单"""
        self.is_click(search['滚动计划单'])
        self.driver.implicitly_wait(10)

    def click_gdadd(self):
        """滚动新增"""
        self.is_click(search['滚动新增'])

    def click_gdselectsp(self):
        """滚动选择供应商"""
        self.is_click(search['滚动选择供应商'])

    def input_gdsupplier(self, content):
        """滚动输入供应商"""
        self.input_text(search['滚动输入供应商'], txt=content)

    def click_gdsearch(self):
        """滚动供应商查询"""
        self.is_click(search['滚动供应商查询'])
        sleep()

    def doubleclick_gdgys(self):
        """滚动双击选择供应商"""
        self.is_doubleclick(search['滚动双击选择供应商'])
        sleep()

    def click_gdaddsku(self):
        """滚动添加配件"""
        self.is_click(search['滚动添加配件'])
        sleep()

    def input_gdsku(self, content):
        """滚动输入内码"""
        self.input_text(search['滚动输入内码'], txt=content)

    def click_gdskusearch(self):
        """滚动点击查询"""
        self.is_click(search['滚动点击查询'])
        sleep(2)

    def doubleclick_gdsku(self):
        """滚动双击内码"""
        self.is_doubleclick(search['滚动双击内码'])

    def input_gdnum(self, content):
        """滚动输入采购数量"""
        self.input_text(search['滚动输入采购数量'], txt=content)

    def input_gdprice(self, content):
        """滚动输入采购价格"""
        self.input_text(search['滚动输入采购价格'], txt=content)

    def click_gdskusure(self):
        """滚动点击确定按钮"""
        self.is_click(search['滚动点击确定按钮'])
        sleep(1)

    def click_gdskuclose(self):
        """滚动关闭添加配件弹框"""
        self.is_click(search['滚动关闭添加配件弹框'])

    def click_gdsave(self):
        """滚动保存"""
        self.is_click(search['滚动保存'])
        sleep()

    def click_gdcommit(self):
        """滚动提交"""
        self.is_click(search['滚动提交'])
        sleep(5)

    def gdpchs_status(self):
        """滚动计划单状态"""
        gdpchs_status = self.element_text(search['滚动计划单状态'])
        return gdpchs_status

    def gdpchs_orderno(self):
        """滚动计划单单号"""
        gdpchs_orderno = self.element_text(search['滚动计划单单号'])
        return gdpchs_orderno

    def click_gdselectfirst(self):
        """滚动选中第一个滚动计划单"""
        self.is_click(search['滚动选中第一个滚动计划单'])

    def gdpchs_orderquxiaonum(self):
        """滚动获取计划取消数量"""
        gdpchs_orderquxiaonum = self.element_text(search['滚动获取计划取消数量'])
        return gdpchs_orderquxiaonum

    def click_gdtiaozheng(self):
        """滚动计划调整"""
        self.is_click(search['滚动计划调整'])
        sleep()

    def click_gdquxiaonum(self):
        """滚动点击本次调整数量"""
        self.is_click(search['滚动点击本次调整数量'])
        sleep()

    def input_gdquxiaonum(self, content):
        """滚动点击本次调整数量"""
        self.input_text(search['滚动点击本次调整数量'], txt=content)

    def click_gdtzsave(self):
        """滚动调整数量保存"""
        self.is_click(search['滚动调整数量保存'])
        sleep()

    def click_gdtzchose(self):
        """滚动点击取消数量"""
        self.is_click(search['滚动点击取消数量'])
        sleep()

    """计划采购订单"""

    def click_pchsplan(self):
        """计划采购订单"""
        self.is_click(search['计划采购订单'])
        sleep(3)
    def click_planadd(self):
        """计划新增"""
        self.is_click(search['计划新增'])

    def click_planselectsp(self):
        """计划选择供应商"""
        self.is_click(search['计划选择供应商'])

    def input_plansupplier(self, content):
        """计划输入供应商"""
        self.input_text(search['计划输入供应商'], txt=content)

    def click_plansearch(self):
        """计划供应商查询"""
        self.is_click(search['计划供应商查询'])
        sleep()

    def doubleclick_plangys(self):
        """计划双击选择供应商"""
        self.is_doubleclick(search['计划双击选择供应商'])
        sleep(2)

    #####################

    def input_plansupplier1(self, content):
        """计划输入供应商"""
        self.input_text(search['计划输入供应商1'], txt=content)

    def click_plansearch1(self):
        """计划供应商查询"""
        self.is_click(search['计划供应商查询1'])
        sleep()

    def doubleclick_plangys1(self):
        """计划双击选择供应商"""
        self.is_doubleclick(search['计划双击选择供应商1'])
        sleep()

    #####################

    def click_planaddsku(self):
        """计划点击选择滚动计划单"""
        self.is_click(search['计划点击选择滚动计划单'])
        sleep()

    def input_plansku(self, content):
        """计划输入滚动计划单"""
        self.input_text(search['计划输入滚动计划单'], txt=content)

    def click_planskusearch(self):
        """计划查询滚动计划单"""
        self.is_click(search['计划查询滚动计划单'])
        sleep()

    def click_planselectgd(self):
        """计划选择滚动计划单"""
        self.is_click(search['计划选择滚动计划单'])
        sleep()

    def click_planselectgd1(self):
        """计划选择滚动计划单"""
        self.is_click(search['计划选择滚动计划单1'])
        sleep()

    def click_planselect(self):
        """计划点击选择"""
        self.is_click(search['计划点击选择'])
        sleep()

    def click_planskuNum(self):
        """点击采购数量"""
        self.is_click(search['计划数量'])
        sleep()

    def input_planskuNum(self, content):
        """修改采购数量"""
        self.input_text(search['修改采购数量'], txt=content)

    def click_plansave(self):
        """计划保存"""
        self.is_click(search['计划保存'])
        sleep()

    def click_plancommit(self):
        """计划提交"""
        self.is_click(search['计划提交'])
        sleep()

    def click_plancommitsure(self):
        """计划提交确定"""
        self.is_click(search['计划提交确定'])
        sleep(5)

    def planpchs_status(self):
        """计划状态"""
        gdpchs_status = self.element_text(search['计划状态'])
        return gdpchs_status

    def planpchs_orderno(self):
        """计划单号"""
        gdpchs_orderno = self.element_text(search['计划单号'])
        return gdpchs_orderno

    def click_planMore(self):
        """计划更多"""
        self.is_click(search['计划更多'])

    def input_planOrder(self, content):
        """计划输入订单编号"""
        self.input_text(search['计划输入订单编号'], txt=content)

    def click_moreSure(self):
        """计划更多确定"""
        self.is_click(search['计划更多确定'])
        sleep()

# 临时采购订单
    def click_pchsls(self):
        """临时采购订单"""
        self.is_click(search['临时采购订单'])
        sleep(3)

    def click_lsAdd(self):
        """临时新增按钮"""
        self.is_click(search['临时新增按钮'])

    def click_lsselectsp(self):
        """临时选择供应商按钮"""
        self.is_click(search['临时选择供应商按钮'])

    def input_lssupplier(self, content):
        """临时输入供应商弹框"""
        self.input_text(search['临时输入供应商弹框'], txt=content)

    def click_lssearch(self):
        """临时查询供应商按钮"""
        self.is_click(search['临时查询供应商按钮'])

    def doubleclick_lsgys(self):
        """临时双击选择供应商"""
        self.is_doubleclick(search['临时双击选择供应商'])
        sleep(2)

    def click_lswaaddsku(self):
        """临时点击添加添加配件"""
        self.is_click(search['临时点击添加添加配件'])

    def input_lssku(self, content):
        """临时输入内码"""
        self.input_text(search['临时输入内码'], txt=content)

    def click_lsskusearch(self):
        """临时点击查询"""
        self.is_click(search['临时点击查询'])

    def doubleclick_lssku(self):
        """临时双击内码"""
        self.is_doubleclick(search['临时双击内码'])

    def input_lsnum(self, content):
        """临时输入数量"""
        self.input_text(search['临时输入数量'], txt=content)

    def input_lsprice(self, content):
        """临时输入采购价格"""
        self.input_text(search['临时输入采购价格'], txt=content)

    def click_lsskusure(self):
        """临时点击确定按钮"""
        self.is_click(search['临时点击确定按钮'])

    def click_lsskuclose(self):
        """临时关闭添加配件弹框"""
        self.is_click(search['临时关闭添加配件弹框'])

    def click_lssave(self):
        """临时保存"""
        self.is_click(search['临时保存'])

    def click_lscommit(self):
        """临时提交并入库"""
        self.is_click(search['临时提交并入库'])

    def click_lscommitsure(self):
        """临时提交确定"""
        self.is_click(search['临时提交确定'])
        sleep(3)

    def lspchs_status(self):
        """临时外采订单状态"""
        wcpchs_status = self.element_text(search['临时外采订单状态'])
        return wcpchs_status

    def lspchs_orderno(self):
        """临时外采单号"""
        wcpchs_orderno = self.element_text(search['临时外采单号'])
        return wcpchs_orderno

    def click_lsMore(self):
        """临时更多"""
        self.is_click(search['临时更多'])

    def input_lsOrder(self, content):
        """临时输入订单编号"""
        self.input_text(search['临时输入订单编号'], txt=content)

    def click_lsSure(self):
        """临时更多确定"""
        self.is_click(search['临时更多确定'])
        sleep()

    def lspchs_cancelNum(self):
        """临时取消数量"""
        lspchs_cancelNum = self.element_text(search['临时取消数量'])
        return lspchs_cancelNum

    def lspchs_checkNum(self):
        """临时验收数量"""
        lspchs_checkNum = self.element_text(search['临时验收数量'])
        return lspchs_checkNum










if __name__ == '__main__':
    pass
