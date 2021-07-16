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
        # updated : 2021-07-16 16:07:10
        pass

    def setup(self):

        pass

    def main(self):
        StepDesc(step_desc="wakeup...",expect_value="")
        AT.sleep(sleepTime="400")
        AT.CanBusLoadDbcFile("D:\\core\\458.dbc")
        AT.CanBusLoadMACT(r'D:\\core\\PATAC_MACT_VCU_V23.36.0.csv')
        AT.CanBusSendMultipleMsg(ids='["0x638", "0x111"]',
                                 is_mac='{"0x638": "False", "0x111": "True"}',
                                 signals='{"0x111": {"IPPEIPltGenStMAC": "88524310","IPPEIPltGenStAntiRplyCnt": "6","ISysPwrMdARC": ["0", "1", "2", "3"],"IRmVehStrRqARC": "0","ISysPwrMd": "2","IPrkBrkSwAtv": "1"}}',
                                 datas='{"0x638": "4840400000000000"}',
                                 cycle_times='{"0x638": "1"}', channel='1')


        AT.CANBusSend(id="0x42E",dlc="2",message="3100",baudrate="500",channel="1",interval="0",duration="1000")
        AT.CANBusSend(id="0x539",dlc="8",message="3131313131313131",baudrate="500",channel="1",interval="0",duration="1000")
        AT.CANBusSend(id="0x53A",dlc="8",message="3131313131313131",baudrate="500",channel="1",interval="0",duration="1000")

        pass

    def teardown(self):

        pass


if __name__ == '__main__':
    testApp().run()
