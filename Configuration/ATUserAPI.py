# coding:utf-8
"""
# Copyright (c) 2018-2020 ThunderSoft
# All Rights Reserved by Thunder Software Technology Co., Ltd and its affiliates.
# You may not use, copy, distribute, modify, transmit in any form this file
# except in compliance with ThunderSoft in writing by applicable law.
"""
# 自定义API方法, 请参照模版方法在此类中添加自定义方法, 测试工具内置方法通过self即可访问
# 基础工程引用，请勿修改
from ATScripts import ATAPI as AT  # 基础API引用，请勿修改
from ATScripts.ATCommon.apiutil import apiwrapper
from ATScripts.ATCommon.apiutil import StepDesc

# 自定义API类
# 方法类注册器，用于将方法注册到系统当中(如果没有装饰器，则API执行信息将不会再IDE上显示，切记！)
@apiwrapper
def demo1(test, desc):
    """
    类型:用户自定义Demo
    说明:
        模版方法
    参数:
        test: 模版参数
        desc: 描述方法操作功能，更具体的展示在测试报告
    返回: False, 描述： 失败
          True, 描述： 成功
          描述： 成功，并返回描述内容
    """
    # 调用系统内置sleep方法
    AT.sleep(sleepTime=10)
    # 返回执行结果成功，并返回描述信息
    return True, "Sleep 10 seconds success"
    # 返回执行结果失败，并返回描述信息
    # return False, "Sleep 10 seconds failed"

@apiwrapper
def wake_up_by_clicking_icon():
    """
        类型:点击方式激活VA
        说明:
            点击方式激活VA
        参数:
            test: 模版参数
            desc: 描述方法操作功能，更具体的展示在测试报告
        返回: False
              True
    """
    global wakeup
    wakeup = False

    #StepDesc(step_desc="1.Click the VA resident area.",expect_value="VA could be waked up.")
    StepDesc(step_desc="1.点击VA常驻区域",expect_value="VA被唤醒")
    AT.ClickElementBy_id(id="com.baidu.che.codriver:id/vpa_view",target="None",timeout="2000")

    #.判断是否唤醒,且唤醒成功后直到播报完并且dialog_flew_hot_layout出现再退出while循环
    #StepDesc(step_desc="2.Check the VA status",expect_value="Waked up")
    StepDesc(step_desc="2.确认VA是否被唤醒",expect_value="VA被唤醒")
    while(True):
        if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")) == "True":
            AT.ReportInfo(string="One.single_content is displayed")
        if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/dialog_flew_hot_layout",target="None",timeout="2000")) == "True":
            AT.ReportInfo(string="Two.Activate VA OK..")
            wakeup = True
            break
        if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")) == "False":
            AT.ReportInfo(string="Three.Reclicking the VA resident area..")
            AT.ClickElementBy_id(id="com.baidu.che.codriver:id/vpa_view",target="None",timeout="2000")
            AT.sleep(sleepTime="200")
    if(wakeup):
        pass
    else:
        AT.ReportError(string="未成功唤醒")



@apiwrapper
def wake_up_by_voice():
    """
        类型:语音唤醒
        说明:
            通过语音唤醒
        参数:
            test: 模版参数
            desc: 描述方法操作功能，更具体的展示在测试报告
        返回: False
              True
    """
    # 调用系统内置sleep方法
    # AT.sleep(sleepTime=10)
    # 返回执行结果成功
    return True
    # 返回执行结果失败
    # return False


@apiwrapper
def return_to_all_apps_page():
    """
        类型:用户自定义Demo
        说明:
            返回到主界面 all apps page
        参数:
            test: 模版参数
            desc: 描述方法操作功能，更具体的展示在测试报告
        返回: False
              True
    """
    AT.ClickElementBy_id(id="com.android.systemui:id/allapp_icon",target="None",timeout="2000")
    AT.sleep(sleepTime="200")

    return True

@apiwrapper
def open_map_input_destination_to_start_navigation():
    """
        类型:进入导航状态
        说明:
            进入导航状态
        参数:
            test: 模版参数
            desc: 描述方法操作功能，更具体的展示在测试报告
        返回: False
              True
    """

    def input_destnation():
        AT.ClickByPoint(x="400",y="70",count="1",target="None")
        AT.sleep(sleepTime="100")
        #获取焦点后可以使用Inputtext()方法输入目的地, 比如: 人民广场
        AT.Inputtext(text="人民广场",target="None")
        AT.sleep(sleepTime="100")
        #搜索
        AT.OnKeyEnter(target="None")
        AT.sleep(sleepTime="200")
        #点击   到这去   图标
        if str(AT.FindElementBy_id(id="com.baidu.naviauto:id/imageView",target="None",timeout="2000")) == 'True':
            AT.ClickElementBy_id(id="com.baidu.naviauto:id/imageView",target="None",timeout="2000")
            AT.sleep(sleepTime="2000")



    global status,once
    status = False
    once = True

    AT.open_map()


    while(True):
        if str(AT.FindElementBy_id(id="com.baidu.naviauto:id/bnav_rg_next_deriction_indicator",target="None",timeout="100")) == "True":
            status = True
            break
        if str(AT.FindElementBy_id(id="com.baidu.naviauto:id/et_ctrl_search",target="None",timeout="100")) == "True" and once:
            once = False
            input_destnation()


    if status:
        return True
    else:
        return False



@apiwrapper
def keep_map_on_path_planned_page():
    """
        类型:进入到路径规划页面
        说明:
            模版方法
        参数:
            test: 模版参数
            desc: 描述方法操作功能，更具体的展示在测试报告
        返回: False
              True
    """

    def input_destnation():
        AT.ClickByPoint(x="400",y="70",count="1",target="None")
        AT.sleep(sleepTime="100")
        #获取焦点后可以使用Inputtext()方法输入目的地, 比如: 人民广场
        AT.Inputtext(text="人民广场",target="None")
        AT.sleep(sleepTime="100")
        #搜索
        AT.OnKeyEnter(target="None")
        AT.sleep(sleepTime="200")
        #点击   到这去   图标
        if str(AT.FindElementBy_id(id="com.baidu.naviauto:id/imageView",target="None",timeout="2000")) == 'True':
            AT.ClickElementBy_id(id="com.baidu.naviauto:id/imageView",target="None",timeout="2000")
            AT.sleep(sleepTime="2000")



    global status,once
    status = False
    once = True

    AT.open_map()


    while(True):
        if str(AT.FindElementBy_id(id="com.baidu.naviauto:id/bnav_rg_next_deriction_indicator",target="None",timeout="100")) == "True":
            status = True
            break
        if str(AT.FindElementBy_id(id="com.baidu.naviauto:id/et_ctrl_search",target="None",timeout="100")) == "True" and once:
            once = False
            input_destnation()


    if status:
        return True
    else:
        return False



@apiwrapper
def close_map():
    """
        类型:关闭地图
        说明:
            close map
        参数:
            test: 模版参数
            desc: 描述方法操作功能，更具体的展示在测试报告
        返回: False
              True
    """
    r_v = AT.RunCommand(command="adb shell am force-stop com.baidu.naviauto",timeout="")
    AT.sleep(sleepTime="200")
    if len(r_v) == 7:
        return True
    else:
        return False

@apiwrapper
def open_map():
    """
        类型:打开地图
        说明:
            open map
        参数:
            test: 模版参数
            desc: 描述方法操作功能，更具体的展示在测试报告
        返回: False
              True
    """
    AT.RunCommand(command="adb shell am start -n com.baidu.naviauto/.NaviAutoActivity",timeout="")
    AT.sleep(sleepTime="12000")

    return True



