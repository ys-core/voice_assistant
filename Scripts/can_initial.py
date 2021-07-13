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
        # updated : 2021-07-09 10:34:03
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


        AT.CanBusSendMultipleMsg(ids='["0x638","0x111"]',
                                 is_mac='{"0x111": "True"}',
                                 signals='{"0x111": {"IPPEIPltGenStMAC": "88524310","IPPEIPltGenStAntiRplyCnt": "6","ISysPwrMdARC": ["0", "1", "2", "3"],"IRmVehStrRqARC": "0","ISysPwrMd": "2","IPrkBrkSwAtv": "1"}}',
                                 channel='1')
        # AT.CanBusSendMsg(msg="4840400000000000",ch="1",interval="1000",duration="100000")
        # AT.CANBusSend(id="0x638",dlc="8",message="4840400000000000",baudrate="500",channel="1",interval="5",duration="10")
        AT.sleep(7200000 * 7)
        pass

    def teardown(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.sleep(sleepTime="400")
        AT.CanBusStopSendMsg(id="0x111", ch=1)
        # AT.CanBusStopSendMsg(id="0x638", ch=1)
        # AT.CanBusStopSendMsg(id="0x376", ch=1)
        pass


if __name__ == '__main__':
    testApp().run()
