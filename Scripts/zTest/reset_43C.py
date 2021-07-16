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
        # updated : 2021-07-16 15:47:37
        pass

    def setup(self):

        pass

    def main(self):

        AT.CanBusResetMsgs(ids="0x43C",channel="1")


        pass

    def teardown(self):


        pass


if __name__ == '__main__':
    testApp().run()
