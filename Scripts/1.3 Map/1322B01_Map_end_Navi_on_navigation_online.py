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
  precondition: 正在导航中...
'''
class testApp(CATBaseCase):

    def info(self):
        # author :
        # priority : High
        # description :
        # device info :
        # functions :
        # model :
        # updated : 2021-07-15 17:26:28
        pass



    def setup(self):                # precondtion

        global user_command,TTS_feedback,startTime
        startTime = time.time()
        user_command = "结束导航"
        TTS_feedback = "导航结束"

        StepDesc(step_desc="确认当前为导航过程中",expect_value="处于导航中")
        if AT.open_map_input_destination_to_start_navigation():
            AT.wake_up_by_clicking_icon()
        else:
            AT.open_map_input_destination_to_start_navigation()

        pass



    def main(self):                # core steps


        global step1,step2,step3
        step1 = False
        step2 = False
        step3 = False

        AT.VRSpeak(string="",saveFile="Sources\\Medias\\Map\\Map_end_navi.wav",volume="100",ensure="False")

        #1.监听用户的输入，并以文本显示在single_content空间内,判断是否识别用户指令正确，正确即跳出while循环,不正确直接报错
        StepDesc(step_desc="1.判断识别结果",expect_value="结束导航")
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
        StepDesc(step_desc="2.判断TTS播报内容",expect_value="导航结束")
        while(True):
            if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")) == "True":
                temp = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="1")
                if TTS_feedback in temp and "当前网络异常" not in temp:
                    step2 = True
                    break
            if (time.time() - startTime) > AT.get_max_time_tolerance():
                step2 = False
                break

        AT.sleep(sleepTime="200")

        StepDesc(step_desc="3.判断是否成功结束导航",expect_value="能正常退出导航")
        while(True):
            if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/et_ctrl_search",target="None",timeout="1")) == "True":
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
            AT.MakeFail(text="This case failed")




    def teardown(self):            # postcondition
        StepDesc(step_desc="Postcondition",expect_value="Return to all apps page")
        # AT.return_to_all_apps_page()
        AT.sleep(sleepTime="200")

        pass


if __name__ == '__main__':
    testApp().run()