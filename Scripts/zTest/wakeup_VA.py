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
        # updated : 2021-07-08 17:01:52
        pass

    def setup(self):
        AT.sleep(sleepTime="100")
        AT.ClickByPoint(x="88",y="10",count="1",target="None")
        AT.sleep(sleepTime="100")
        pass

    def main(self):
        # res,iswakeup,count 三个变量分别表示已获取到的文显内容;isweakup用来标记是否成功唤醒VA;count用来统计文献内容的长度,主要是用来判断文显内容已到头
        global res,iswakeup,count
        res = ""
        iswakeup = False
        count = 0

        #1.判断是否唤醒,且唤醒成功后直到播报完再退出while循环
        res = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")
        while(len(res) >= count):
            iswakeup = True
            count = len(res)
            res = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")
            AT.sleep(sleepTime="50")

        # AT.ReportInfo(string=str(len(res)))

        #2.如果唤醒成功继续输入语音并且监听TTS反馈的内容
        if iswakeup:

            #3.播放音频,即需要执行的有效指令

            # AT.ReportError(string=str(AT.GetElementsBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000"))
            #4.监听TTS反馈的内容之前,首先需要判断id:single_content是否存在,直到该id出现了就可以继续后面的监听TTS文本的动作
            while(str(AT.GetElementsBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")) == 'False'):
                AT.sleep(sleepTime="50")

            #5.监听TTS反馈的文本内容,能执行到这个位置说明id:single_content是存在的
            count = 0
            res = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")
            while(len(res) > count):
                count = len(res)
                if res == "今天星期几":
                    count = 0
                    AT.sleep(sleepTime="200")
                else:
                    if str(AT.GetElementsBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="50")) == 'False':
                        break
                    else:    # id还未消失,继续监听,可能文显内容还未展示完整
                        res = AT.GetTextBy_id(id="com.baidu.che.codriver:id/single_content",target="None",timeout="2000")
                        count = len(res)
                        AT.sleep(sleepTime="50")

                    pass
            AT.ReportInfo(string="1111111111111111111111111111111111111111111111")
            AT.ReportInfo(string=res)

        # AT.VRSpeak(string="",saveFile="",volume="50",ensure="False")
        else:
            AT.ReportFail(string="failed")



    def teardown(self):


        pass


if __name__ == '__main__':
    testApp().run()
