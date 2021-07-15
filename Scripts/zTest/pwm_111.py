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
        AT.CanBusSendMultipleMsg(ids="",datas="None",signals="None",is_mac="None",cycle_times="None",durations="None",channel="1")
        # description :
        # device info :
        # functions :
        # model :
        # updated : 2021-07-09 09:32:37
        pass

    def setup(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description2",expect_value="Expect value2")
        AT.sleep(sleepTime="400")
        pass

    def main(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.CanBusLoadDbcFile("D:\\core\\458.dbc")
        AT.CanBusLoadMACT(r'D:\\core\\PATAC_MACT_VCU_V23.36.0.csv')
        AT.CanBusSendMultipleMsg(ids='["0x111"]',
                                 is_mac='{"0x111": "True"}',
                                 signals='{"0x111": {"IPPEIPltGenStMAC": "88524310","IPPEIPltGenStAntiRplyCnt": "6","ISysPwrMdARC": ["0", "1", "2", "3"],"IRmVehStrRqARC": "0","ISysPwrMd": "2","IPrkBrkSwAtv": "1"}}',
                                 cycle_times='{"0x111": "100"}', channel='1')
        AT.sleep(7200000 * 7)


        pass

    def teardown(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description2",expect_value="Expect value2")
        AT.sleep(sleepTime="400")
        pass


if __name__ == '__main__':
    testApp().run()
