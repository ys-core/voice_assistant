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

class testApp(CATBaseCase):

    def info(self):
        # updated : 2021-07-09 13:06:37
        pass

    def setup(self):

        global user_command
        user_command = "今天星期几"

        AT.ClickElementBy_id(id="com.android.systemui:id/apptray_home",target="None",timeout="2000")
        AT.sleep(sleepTime="100")
        AT.ClickElementBy_id(id="com.android.systemui:id/allapp_icon",target="None",timeout="2000")
        AT.sleep(sleepTime="100")

        #2. 不确定 "语音助手" 是在第一屏还是第二屏，所以判断下，并切换到 "百度地图" 在可见视域内，主要是为了接下来获取到地图控件元素并可以打开
        if str(AT.FindElementBy_text(text="语音助手",target="None",timeout="200")) == 'False' and str(AT.FindElementBy_text(text="Voice Assistant",target="None",timeout="200")) == 'False':
            AT.Swipe(start_x="1900",start_y="350",end_x="100",end_y="350",duration="100",target="None")

        #3. 判断中英文后打开语音助手
        if str(AT.FindElementBy_text(text="语音助手",target="None",timeout="2000")) != "False":
            AT.ClickElementBy_text(text="语音助手",target="None",timeout="2000")
        else:
            AT.ClickElementBy_text(text="Voice Assistant",target="None",timeout="2000")
            AT.RunCommand(command="",timeout="")



        pass

    def main(self):
        # res,iswakeup,count 三个变量分别表示已获取到的文显内容;isweakup用来标记是否成功唤醒VA;count用来统计文献内容的长度,主要是用来判断文显内容已到头
        global res,iswakeup,count,step1,step2,step3
        res = ""
        iswakeup = False
        count = 0
        step1 = False
        step2 = False
        step3 = False


        #1.判断是否唤醒,且唤醒成功后直到播报完并且dialog_flew_hot_layout出现再退出while循环
        # res = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")
        while(True):
            if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")) == "True":
                AT.ReportError(string="1111111111111111")
            if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/dialog_flew_hot_layout",target="None",timeout="2000")) == "True":
                AT.ReportError(string="222222222222222")
                step1 = True
                break

        #2.监听用户的输入，并以文本显示在single_content空间内,判断是否识别用户指令正确，正确即跳出while循环,不正确直接报错
        while(True):
            if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")) == "True":
                temp = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")
                if temp == user_command:
                    AT.ReportError(string="3333333333333333")
                    step2 = True
                    break


        #3.监听TTS播报的文本，判断是否相应正确，若正确即跳出while循环,不正确直接报错
        while(True):
            if str(AT.FindElementBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")) == "True":
                temp = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")
                AT.ReportInfo(string=str(len(temp)))
                if ("今天是" in temp and "年" in temp and "月" in temp and "日" in temp and "，" in temp and "星期" in temp):
                    temp = temp.replace("今天是星期","").replace(",","").replace("年","").replace("月","").replace("日","").replace("号","")
                    if temp in ['一','二','三','四','五','六','日']:
                        AT.ReportError(string="44444444444444444444")
                        step3 = True
                        break

        if(step1 and step2 and step3):
            pass
        else:
            AT.ReportError(string="failed finally")

    def teardown(self):


        pass


if __name__ == '__main__':
    testApp().run()
