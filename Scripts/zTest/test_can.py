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
        # updated : 2021-07-09 11:26:29
        pass

    def setup(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description2",expect_value="Expect value2")
        AT.sleep(sleepTime="400")
        pass

    def main(self):
        StepDesc(step_desc="",expect_value="")
        AT.sleep(sleepTime="400")
        AT.CanBusLoadDbcFile("D:\\core\\458.dbc")
        AT.CanBusLoadMACT(r'D:\\core\\PATAC_MACT_VCU_V23.36.0.csv')
        AT.CanBusSendMultipleMsg(ids='["0x638", "0x111","0x42E","0x539","0x53A"]',
                                 is_mac='{"0x638": "False","0x42E": "False", "0x539": "False", "0x53A": "False",  "0x111": "True"}',
                                 signals='{"0x111": {"IPPEIPltGenStMAC": "88524310","IPPEIPltGenStAntiRplyCnt": "6","ISysPwrMdARC": ["0", "1", "2", "3"],"IRmVehStrRqARC": "0","ISysPwrMd": "2","IPrkBrkSwAtv": "1"}}',
                                 datas='{"0x638": "4840400000000000",0x42E": "3100",0x539": "3131313131313131",0x53A": "3131313131313131",}',
                                 cycle_times='{"0x638": "1"}', channel='1')



        AT.sleep(7200000 * 7)
        pass

    def teardown(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.sleep(sleepTime="400")
        # AT.CanBusStopSendMsg(id="0x111", ch=1)
        # AT.CanBusStopSendMsg(id="0x638", ch=1)
        # AT.CanBusStopSendMsg(id="0x376", ch=1)
        pass


if __name__ == '__main__':
    testApp().run()
