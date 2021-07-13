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
        # updated : 2021-07-12 19:38:58
        pass



    def setup(self):                # precondtion

        global user_command,TTS_feedback
        user_command = "打开地图"
        TTS_feedback = "请先同意免责声明"
        AT.wake_up_by_clicking_icon()
        # AT.wake_up_by_voice()

        pass



    def main(self):                # core steps


        global step1,step2,step3,step4
        step1 = False
        step2 = False
        step3 = False
        step4 = False

        #1.监听用户的输入，并以文本显示在single_content空间内,判断是否识别用户指令正确，正确即跳出while循环,不正确直接报错
        StepDesc(step_desc="1.判断识别结果",expect_value="打开地图")
        while(True):
            if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")) == "True":
                temp = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")
                if temp == user_command:
                    step1 = True
                    break


        #2.监听TTS播报的文本，判断是否相应正确，若正确即跳出while循环,不正确直接报错
        StepDesc(step_desc="2.判断TTS播报内容",expect_value="请先同意免责申明")
        while(True):
            if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")) == "True":
                temp = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")
                if TTS_feedback in temp and "当前网络异常" not in temp:
                    step2 = True
                    break

        AT.sleep(sleepTime="200")
        #3.手动选择同意，以及 下次不再弹出的提醒框
        StepDesc(step_desc="3.判断灰色背景的 免责声明 弹窗显示状态",expect_value="正常显示")
        while(True):
            if str(AT.FindElementBy_id(id="com.baidu.naviauto:id/permit_accept",target="None",timeout="2000")) == "True" and str(AT.FindElementBy_id(id="com.baidu.naviauto:id/first_btn",target="None",timeout="2000")) == "True":
                # title = AT.GetTextBy_id(id="com.baidu.navigation:id/dialog_title",target="None",timeout="2000")
                # content = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")
                step3 = True
                break




        if(step1 and step2 and step3):
            StepDesc(step_desc="Final result",expect_value="pass")
            AT.sleep(sleepTime="50")
            pass
        else:
            StepDesc(step_desc="Final result",expect_value="fail")
            AT.sleep(sleepTime="50")
            AT.ReportError(string="failed finally")








    def teardown(self):            # postcondition


        pass


if __name__ == '__main__':
    testApp().run()
