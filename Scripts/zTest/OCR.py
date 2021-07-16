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
        # updated : 2021-07-16 15:23:23
        pass

    def setup(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description2",expect_value="Expect value2")
        AT.sleep(sleepTime="400")
        pass

    def main(self):
        AT.CANBusSend(id="0x42E",dlc="2",message="3100",baudrate="500",channel="1",interval="0",duration="1000")
        AT.CANBusSend(id="0x539",dlc="8",message="3131313131313131",baudrate="500",channel="1",interval="0",duration="1000")
        AT.CANBusSend(id="0x53A",dlc="8",message="3131313131313131",baudrate="500",channel="1",interval="0",duration="1000")


        pass

    def teardown(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description2",expect_value="Expect value2")
        AT.sleep(sleepTime="400")
        pass


if __name__ == '__main__':
    testApp().run()
