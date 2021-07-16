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
        # updated : 2021-07-16 16:33:06
        pass

    def setup(self):

        pass

    def main(self):
        StepDesc(step_desc="",expect_value="")
        AT.CanBusLoadDbcFile("D:\\core\\458.dbc")
        AT.CanBusLoadMACT(r'D:\\core\\PATAC_MACT_VCU_V23.36.0.csv')
        AT.CanBusSendMultipleMsg(ids='["0x420"]',
                                 is_mac='{"0x420": "False""}',
                                 signals='{"0x420": {"SnrfConfig":"1"}}',
                                 cycle_times='{"0x420": "1"}', channel='1')



        # AT.sleep(7200000 * 7)
        pass

    def teardown(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        # AT.sleep(sleepTime="400")
        # AT.CanBusStopSendMsg(id="0x111", ch=1)
        # AT.CanBusStopSendMsg(id="0x638", ch=1)
        # AT.CanBusStopSendMsg(id="0x376", ch=1)
        pass


if __name__ == '__main__':
    testApp().run()
