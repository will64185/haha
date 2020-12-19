from page.webpage import WebPage, sleep
from common.readelement import Element

sell = Element('sell')


class Sellpage(WebPage):
    """销售管理"""

    def click_sellManager(self):
        """销售管理"""
        self.is_click(sell['销售管理'])
        sleep()

    # 销售订单
    def click_sellOrder(self):
        """销售订单"""
        self.is_click(sell['销售订单'])
        sleep(3)

    def click_sellAdd(self):
        """销售新增"""
        self.is_click(sell['销售新增'])

    def input_sellGuest(self, content):
        """销售输入客户"""
        self.input_text(sell['销售输入客户'], txt=content)
        sleep()

    def enter_guest(self):
        """销售输入客户,回车键"""
        self.key_enter(sell['销售输入客户'])
        sleep()

    def click_sellSelectGuest(self):
        """销售选择客户"""
        self.is_click(sell['销售选择客户'])

    def click_sellAddSku(self):
        """销售添加配件"""
        self.is_click(sell['销售添加配件'])

    def input_sellInputPartId(self, content):
        """销售输入内码"""
        self.input_text(sell['销售输入内码'], txt=content)

    def click_sellSkusearch(self):
        """销售点击查询"""
        self.is_click(sell['销售点击查询'])
        sleep(2)

    def doubleClick_sellSKu(self):
        """销售双击配件"""
        self.is_doubleclick(sell['销售双击配件'])
        sleep()

    def input_sellNum(self, content):
        """销售输入数量"""
        self.input_text(sell['销售输入数量'], txt=content)

    def input_sellPrice(self, content):
        """销售输入单价"""
        self.input_text(sell['销售输入单价'], txt=content)

    def click_sellSkuSure(self):
        """销售点击确定"""
        self.is_click(sell['销售点击确定'])
        sleep()

    def click_sellCancel(self):
        """销售点击取消"""
        self.is_click(sell['销售点击取消'])
        sleep()

    def click_sellSave(self):
        """销售保存按钮"""
        self.is_click(sell['销售保存按钮'])
        sleep(2)

    def click_sellCommit(self):
        """销售提交按钮"""
        self.is_click(sell['销售提交按钮'])

    def click_sellCommitSure(self):
        """销售提交确定按钮"""
        self.is_click(sell['销售提交确定按钮'])
        sleep()

    def click_sellOut(self):
        """销售出库"""
        self.is_click(sell['销售出库'])

    def click_sellOutSure(self):
        """销售出库确定"""
        self.is_click(sell['销售出库确定'])
        sleep(3)

    def sell_Status(self):
        """销售单状态"""
        allot_allotStatus = self.element_text(sell['销售单状态'])
        return allot_allotStatus

    def sell_orderNo(self):
        """销售单号"""
        allot_outOrderOn = self.element_text(sell['销售单号'])
        return allot_outOrderOn

    def click_batchSku(self):
        """批次库存"""
        self.is_click(sell['批次库存'])

    def input_batchCode(self, content):
        """批次输入编码"""
        self.input_text(sell['批次输入编码'], txt=content)
        sleep(2)

    def click_batchSkuSearch(self):
        """批次查询"""
        self.is_click(sell['批次查询'])
        sleep(2)

    def click_batchSelectSku(self):
        """批次选择配件"""
        self.is_click(sell['批次选择配件'])

    def click_batchSkuSelect(self):
        """批次选择"""
        self.is_click(sell['批次选择'])
        sleep(2)

    def click_batchSkuNum(self):
        """批次数量1"""
        self.is_click(sell['批次数量1'])
        sleep()

    def input_batchSkuNum(self, content):
        """批次数量"""
        self.input_text(sell['批次数量'], txt=content)

    def click_enterOrder(self):
        """选择入库单"""
        self.is_click(sell['选择入库单'])
        sleep()

    def click_outEnterOrder(self):
        """选择出库的入库单"""
        self.is_click(sell['选择出库的入库单'])
        sleep(2)

    def click_selectEnterOrder(self):
        """入库单选入"""
        self.is_click(sell['入库单选入'])
        sleep()

    def click_enterOrderCost(self):
        """按入库成本取值"""
        self.is_click(sell['按入库成本取值'])
        sleep()

    def click_outNum(self):
        """点击出库数量"""
        self.is_click(sell['点击出库数量'])
        sleep()

    def input_outNum(self, content):
        """输入出库数量"""
        self.input_text(sell['输入出库数量'], txt=content)
        sleep(2)

    # 销售退货
    def click_salesReturns(self):
        """销售退货"""
        self.is_click(sell['销售退货'])
        sleep()

    def salesReturnsAdd(self):
        """销退新增"""
        self.is_click(sell['销退新增'])
        sleep()

    def input_salesReturnsGuest(self, content):
        """销退输入客户"""
        self.input_text(sell['销退输入客户'], txt=content)
        sleep(2)

    def enter_salesReturnsGuest(self):
        """销退输入客户,回车键"""
        self.key_enter(sell['销退输入客户'])
        sleep()

    def click_salesReturnsGuest(self):
        """销退选择客户"""
        self.is_click(sell['销退选择客户'])

    def click_salesReturnsReason(self):
        """销退点击退货原因"""
        self.is_click(sell['销退点击退货原因'])

    def click_salesReturnsChooseReason(self):
        """销退选择退货原因"""
        self.is_click(sell['销退选择退货原因'])

    def click_salesReturnsAddSku(self):
        """销退添加配件"""
        self.is_click(sell['销退添加配件'])
        sleep()

    def input_salesReturnsInputPartId(self, content):
        """销退输入内码"""
        self.input_text(sell['销退输入内码'], txt=content)

    def click_salesReturnsSearch(self):
        """销退点击查询"""
        self.is_click(sell['销退点击查询'])
        sleep(3)

    def click_salesReturnsSku1(self):
        """销退选择退货配件1"""
        self.is_click(sell['销退选择退货配件1'])

    def click_salesReturnsSku2(self):
        """销退选择退货配件2"""
        self.is_click(sell['销退选择退货配件2'])

    def click_salesReturnsSku3(self):
        """销退选择退货配件3"""
        self.is_click(sell['销退选择退货配件3'])

    def click_click_salesReturnsChoose(self):
        """销退点击选择"""
        self.is_click(sell['销退点击选择'])

    def click_click_salesReturnsClose(self):
        """销退关闭添加配件弹框"""
        self.is_click(sell['销退关闭添加配件弹框'])

    def click_click_salesReturnsSave(self):
        """销退保存"""
        self.is_click(sell['销退保存'])
        sleep(2)

    def click_click_salesReturnsCommit(self):
        """销退点击提交并入库"""
        self.is_click(sell['销退点击提交并入库'])
        sleep()

    def click_click_salesReturnsCommitSure(self):
        """销退点击确定"""
        self.is_click(sell['销退点击确定'])
        sleep(3)

    def salesReturns_Status(self):
        """销退状态"""
        salesReturns_Status = self.element_text(sell['销退状态'])
        return salesReturns_Status

    def salesReturns_orderNo(self):
        """销退单号"""
        salesReturns_orderNo = self.element_text(sell['销退单号'])
        return salesReturns_orderNo
