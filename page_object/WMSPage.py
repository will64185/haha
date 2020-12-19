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
        sleep()

    def click_receivingNo(self):
        """wms点击收货单号"""
        self.is_click(wms['wms点击收货单号'])
        sleep()

    def receiving_no(self):
        """wms点击收货单号"""
        receiving_no = self.element_text(wms['wms点击收货单号'])
        return receiving_no

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

    def click_receivingDetail(self):
        """wms添加明细"""
        self.is_click(wms['wms添加明细'])

    def click_receivingDetailNum(self):
        """wms收货数量"""
        self.is_click(wms['wms收货数量'])

    def click_receivingDetailSure(self):
        """wms收货确定"""
        self.is_click(wms['wms收货确定'])

    def click_receivingchayiSure(self):
        """wms收货差异确定"""
        self.is_click(wms['wms收货差异确定'])

    def input_receivingDetailNum(self, content):
        """wms收货数量"""
        self.input_text(wms['wms收货数量'], txt=content)

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
        sleep(3)

    def ruku_status(self):
        """WMS入库单状态"""
        ruku_status = self.element_text(wms['WMS入库单状态'])
        return ruku_status

    def click_receivingDifference(self):
        """WMS收货差异"""
        self.is_click(wms['WMS收货差异'])

    def input_receivingOn(self, content):
        """WMS输入收货单号"""
        self.input_text(wms['WMS输入收货单号'], txt=content)

    def click_receivingSearch(self):
        """WMS收货单号查询按钮"""
        self.is_click(wms['WMS收货单号查询按钮'])

    def click_difference(self):
        """WMS确认差异"""
        self.is_click(wms['WMS确认差异'])

    def click_differenceSure(self):
        """WMS确认差异确定"""
        self.is_click(wms['WMS确认差异确定'])
        sleep(3)

    # 出库管理
    def click_outManager(self):
        """出库管理"""
        self.is_click(wms['出库管理'])
        sleep(2)

    def click_outTask(self):
        """出库任务"""
        self.is_click(wms['出库任务'])
        sleep()

    def wms_outStatus(self):
        """获取出库单状态"""
        wms_outStatus = self.element_text(wms['获取出库单状态'])
        return wms_outStatus

    def click_orderClass(self):
        """订单类型"""
        self.is_click(wms['订单类型'])

    def click_allotOut(self):
        """调拨出库"""
        self.is_click(wms['调拨出库'])

    def click_search(self):
        """搜索条件"""
        self.is_click(wms['搜索条件'])

    def click_searchYewuNo(self):
        """选择业务单号"""
        self.is_click(wms['选择业务单号'])

    def input_YewuNo(self, content):
        """输入业务单号"""
        self.input_text(wms['输入业务单号'], txt=content)

    def click_searchButton(self):
        """查询按钮"""
        self.is_click(wms['查询按钮'])
        sleep(2)

    def click_sortinglistButton(self):
        """生成分拣清单"""
        self.is_click(wms['生成分拣清单'])
        sleep(3)

    def click_sortinglist(self):
        """分拣清单"""
        self.is_click(wms['分拣清单'])
        sleep()

    def click_sortingButton(self):
        """点击分拣"""
        self.is_click(wms['点击分拣'])
        sleep()

    def input_sortingNum(self, content):
        """修改分拣数量"""
        self.input_text(wms['修改分拣数量'], txt=content)

    def click_sortingDetailSave(self):
        """明细保存"""
        self.is_click(wms['明细保存'])
        sleep()

    def click_sortingOver(self):
        """拣货完成"""
        self.is_click(wms['拣货完成'])

    def input_sortingRemark(self, content):
        """输入备注"""
        self.input_text(wms['输入备注'], txt=content)

    def click_sortingRemarkSave(self):
        """备注保存"""
        self.is_click(wms['备注保存'])
        sleep(3)

    def click_packingTask(self):
        """装箱任务"""
        self.is_click(wms['装箱任务'])
        sleep()

    def click_packingButton(self):
        """点击装箱"""
        self.is_click(wms['点击装箱'])

    def click_oneKeyPacking(self):
        """点击一键装箱"""
        self.is_click(wms['点击一键装箱'])
        sleep(3)

    def click_packingOver(self):
        """点击拣货完成"""
        self.is_click(wms['点击拣货完成'])
        sleep(4)

    def click_packSureButton(self):
        """点击确定按钮"""
        self.is_click(wms['点击确定按钮'])
        sleep(2)

    def click_deliveryList(self):
        """点击确认生成发货清单"""
        self.is_click(wms['点击确认生成发货清单'])
        sleep(2)

    def click_deliveryManager(self):
        """点击发货管理"""
        self.is_click(wms['点击发货管理'])
        sleep(3)

    def click_quickSearch(self):
        """点击快速查询"""
        self.is_click(wms['点击快速查询'])

    def click_selectToday(self):
        """选择今天"""
        self.is_click(wms['选择今天'])
        sleep(3)

    def click_deliveryButton(self):
        """点击发运"""
        self.is_click(wms['点击发运'])
        sleep(2)

    def click_deliveryMethod(self):
        """选择配送方式"""
        self.is_click(wms['选择配送方式'])

    def click_selfMentioned(self):
        """选择客服自提"""
        self.is_click(wms['选择客服自提'])

    def click_deliverySureButton(self):
        """点击确认发运"""
        self.is_click(wms['点击确认发运'])

    def click_deliverySureSure(self):
        """点击确定"""
        self.is_click(wms['点击确定'])
        sleep(7)

    def wms_outOrderNo(self):
        """获取出库单号"""
        wms_outOrderNo = self.element_text(wms['获取出库单号'])
        return wms_outOrderNo

    def wms_YewuNo(self):
        """获取业务单号"""
        wms_YewuNo = self.element_text(wms['获取业务单号'])
        return wms_YewuNo

    def click_outDifference(self):
        """出库差异"""
        self.is_click(wms['出库差异'])
        sleep(2)

    def input_outOrderNo(self, content):
        """输入出库单号"""
        self.input_text(wms['输入出库单号'], txt=content)

    def click_outDifferenceSearch(self):
        """点击查询"""
        self.is_click(wms['点击查询'])
        sleep()

    def click_DifferenceSure(self):
        """确认差异"""
        self.is_click(wms['确认差异'])
        sleep()

    def click_DifferenceSureButton(self):
        """确认差异确定"""
        self.is_click(wms['确认差异确定'])
        sleep(3)

