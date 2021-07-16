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
        # updated : 2021-07-16 15:47:00
        pass

    def setup(self):

        pass

    def main(self):
        AT.sleep(sleepTime="400")
        AT.CanBusLoadDbcFile("D:\\core\\458.dbc")
        AT.CanBusLoadMACT(r'D:\\core\\PATAC_MACT_VCU_V23.36.0.csv')




        AT.CanBusSendMultipleMsg(ids='["0x43C"]',
                                 is_mac='{"0x43C": "False"}',
                                 signals='{"0x43C": {"ElecShftPrTrnMlfIO": "1"}}',
                                 cycle_times='{"0x43C": "1"}', channel='1')

        # signals='{"0x43C": {"ElecShftPrTrnMlfIO": "1"}}',
        pass

    def teardown(self):

        pass


if __name__ == '__main__':
    testApp().run()
