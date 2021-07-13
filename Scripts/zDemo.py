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
        # author :
        # priority : High
        # description :
        # device info :
        # functions :
        # model :
        # updated : 2021-07-06 15:58:32
        pass

    def setup(self):
        # AT.ClickElementBy_desc(desc="语音助手",target="None",timeout="2000")

        pass

    def main(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.VRSpeak(string="小度小度",saveFile="",volume="50",ensure="False")
        pass

    def teardown(self):

        pass


if __name__ == '__main__':
    testApp().run()
