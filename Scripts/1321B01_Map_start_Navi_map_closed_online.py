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
  precondition: 地图处于关闭状态,后台杀死的那种
'''
class testApp(CATBaseCase):

    def info(self):
        # author :
        # priority : High
        # description :
        # device info :
        # functions :
        # model :
        # updated : 2021-07-14 12:25:58
        pass

    def setup(self):

        global user_command,TTS_feedback
        user_command = "开始导航"
        TTS_feedback = "请先打开地图"

        AT.close_map()

        AT.wake_up_by_clicking_icon()

        pass

    def main(self):
        global step1,step2
        step1 = False
        step2 = False


        AT.VRSpeak(string="",saveFile="Sources\\Medias\\Map\\Map_start_navi.wav",volume="100",ensure="False")

        #1.监听用户的输入，并以文本显示在single_content空间内,判断是否识别用户指令正确，正确即跳出while循环,不正确直接报错
        StepDesc(step_desc="1.判断识别结果",expect_value="开始导航")
        while(True):
            if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")) == "True":
                temp = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")
                if temp == user_command:
                    step1 = True
                    break


        #2.监听TTS播报的文本，判断是否相应正确，若正确即跳出while循环,不正确直接报错
        StepDesc(step_desc="2.判断TTS播报内容",expect_value="请先打开地图")
        while(True):
            if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")) == "True":
                temp = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")
                if TTS_feedback in temp and "当前网络异常" not in temp:
                    step2 = True
                    break

        AT.sleep(sleepTime="200")


        if(step1 and step2):
            StepDesc(step_desc="Final result",expect_value="pass")
            AT.sleep(sleepTime="50")
            pass
        else:
            StepDesc(step_desc="Final result",expect_value="fail")
            AT.sleep(sleepTime="50")
            AT.ReportError(string="failed finally")

        pass

    def teardown(self):
        StepDesc(step_desc="Postcondition",expect_value="Return to all apps page")
        # AT.return_to_all_apps_page()
        AT.sleep(sleepTime="200")

        pass


if __name__ == '__main__':
    testApp().run()
