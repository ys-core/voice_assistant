# [project]:
# [branch]:
# [timeout]:
# [test_case_name]:
# [test_case_id]:
# [test_case_description]:
# encoding = utf-8
from ATScripts.ATSrc.ATImpl.ATAcutor.BaseTestCase import CATBaseCase
from ATScripts import ATAPI as AT
from ATScripts.ATCommon.apiutil import StepDesc

'''
 Open Baidu Map app
'''
class testApp(CATBaseCase):

    def info(self):
        # author :
        # priority : High
        # description :
        # device info :
        # functions :
        # model :
        # updated : 2021-07-12 17:57:30
        pass

    def setup(self):                # case的前置条件写在这里

        #1. 依次点击底部的apptray_home、allapp_icon，确保进入all app界面时为第一屏
        AT.ClickElementBy_id(id="com.android.systemui:id/apptray_home",target="None",timeout="2000")
        AT.sleep(sleepTime="300")
        AT.ClickElementBy_id(id="com.android.systemui:id/allapp_icon",target="None",timeout="2000")
        AT.sleep(sleepTime="300")

        #2. 不确定 "百度地图" 是在第一屏还是第二屏，所以判断下，并切换到 "百度地图" 在可见视域内，主要是为了接下来获取到地图控件元素并可以打开
        if str(AT.FindElementBy_text(text="百度地图",target="None",timeout="200")) == 'False' and str(AT.FindElementBy_text(text="BaiduMapAuto",target="None",timeout="200")) == 'False':
            AT.Swipe(start_x="1900",start_y="350",end_x="100",end_y="350",duration="100",target="None")

        #3. 判断中英文后打开地图应用
        if str(AT.FindElementBy_text(text="百度地图",target="None",timeout="2000")) != "False":
            AT.ClickElementBy_text(text="百度地图",target="None",timeout="2000")
        else:
            AT.ClickElementBy_text(text="BaiduMapAuto",target="None",timeout="2000")
            AT.RunCommand(command="",timeout="")
        pass

    def main(self):                # case的核心内容,比如每一步的动作等都写在这个函数里面

        #等待一些时间，确保地图应用完全打开
        AT.sleep(sleepTime="800")
        #点击输入框,主要是为了获取焦点
        AT.ClickByPoint(x="400",y="70",count="1",target="None")
        AT.sleep(sleepTime="200")
        #获取焦点后可以使用Inputtext()方法输入目的地, 比如: 人民广场
        AT.Inputtext(text="人民广场",target="None")
        #输入目的地完成后，回车或者点击右侧的 搜索
        AT.sleep(sleepTime="100")
        AT.ClickElementBy_id(id="com.baidu.naviauto:id/tv_lion_search_search",target="None",timeout="200")

        pass

    def teardown(self):            # case执行完成后的收尾工作写在这里,比如退出导航状态或者是关闭地图


        pass


if __name__ == '__main__':
    testApp().run()
