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
        # updated : 2021-07-09 15:00:14
        pass

    def setup(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description2",expect_value="Expect value2")
        AT.sleep(sleepTime="400")
        pass

    def main(self):
        AT.CanBusLoadDbcFile("D:\\core\\458.dbc")
        AT.CanBusLoadMACT(r'D:\\core\\PATAC_MACT_VCU_V23.36.0.csv')

        AT.CanBusStopSendMsg(id="0x111", ch=1)
        AT.CanBusStopSendMsg(id="0x638", ch=1)
        AT.CanBusStopSendMsg(id="0x42E", ch=1)
        AT.CanBusStopSendMsg(id="0x539", ch=1)
        AT.CanBusStopSendMsg(id="0x53A", ch=1)

        # AT.CanBusStopSendMsg(id="0x376", ch=1)
        pass

    def teardown(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description2",expect_value="Expect value2")
        AT.sleep(sleepTime="400")
        pass


if __name__ == '__main__':
    testApp().run()
