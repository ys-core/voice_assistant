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
import time

'''
  it's the first time to open the Map, the "免责声明" toast should be pop-uped before accessing the map homepage
'''
class testApp(CATBaseCase):

    def info(self):
        # author :
        # priority : High
        # description :
        # device info :
        # functions :
        # model :
        # updated : 2021-07-15 15:46:57
        pass



    def setup(self):                # precondtion

        global user_command,TTS_feedback,startTime
        startTime = time.time()
        user_command = "打开地图"
        TTS_feedback = "请先同意免责声明"
        AT.wake_up_by_clicking_icon()
        # AT.wake_up_by_voice()

        pass



    def main(self):                # core steps


        global step1,step2,step3
        step1 = False
        step2 = False
        step3 = False

        AT.VRSpeak(string="",saveFile="Sources\\Medias\\Map\\Map_open_map.wav",volume="100",ensure="False")

        #1.监听用户的输入，并以文本显示在single_content空间内,判断是否识别用户指令正确，正确即跳出while循环,不正确直接报错
        StepDesc(step_desc="1.判断识别结果",expect_value="打开地图")
        while(True):
            if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")) == "True":
                temp = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")
                if temp == user_command:
                    step1 = True
                    break
            if (time.time() - startTime) > AT.get_max_time_tolerance():
                step1 = False
                break


        #2.监听TTS播报的文本，判断是否相应正确，若正确即跳出while循环,不正确直接报错
        StepDesc(step_desc="2.判断TTS播报内容",expect_value="请先同意免责申明")
        while(True):
            if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")) == "True":
                temp = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")
                if TTS_feedback in temp and "当前网络异常" not in temp:
                    step2 = True
                    break
            if (time.time() - startTime) > AT.get_max_time_tolerance():
                step2 = False
                break

        #3.判断 黑色背景的 免责声明 弹窗是否打开
        StepDesc(step_desc="3.判断灰色背景的 免责声明 弹窗显示状态",expect_value="正常显示")
        while(True):
            if str(AT.FindElementBy_id(id="com.baidu.naviauto:id/dialog_title",target="None",timeout="2000")) == "True" and str(AT.FindElementBy_id(id="com.baidu.naviauto:id/dialog_content",target="None",timeout="2000")) == "True" and str(AT.FindElementBy_id(id="com.baidu.naviauto:id/bottom_bar",target="None",timeout="2000")) == "True":
                # title = AT.GetTextBy_id(id="com.baidu.navigation:id/dialog_title",target="None",timeout="2000")
                # content = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")
                step3 = True
                break
            if (time.time() - startTime) > AT.get_max_time_tolerance():
                step3 = False
                break

        if(step1 and step2 and step3):
            StepDesc(step_desc="Final result",expect_value="pass")
            AT.sleep(sleepTime="50")
            pass
        else:
            StepDesc(step_desc="Final result",expect_value="fail")
            AT.sleep(sleepTime="50")
            # AT.ReportError(string="failed finally")
            AT.MakeFail(text="This case failed")




    def teardown(self):            # postcondition
        StepDesc(step_desc="Postcondition",expect_value="Return to all apps page")
        AT.sleep(sleepTime="400")
        AT.return_to_all_apps_page()
        pass


if __name__ == '__main__':
    testApp().run()
