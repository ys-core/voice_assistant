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
        # updated : 2021-07-14 13:13:40
        pass

    def setup(self):

        pass

    def main(self):
        # AT.open_map_input_destination_to_start_navigation()
        # AT.close_map()
        # AT.ClickElementBy_id(id="com.baidu.naviauto:id/second_btn",target="None",timeout="2000")
        AT.open_map()

        pass

    def teardown(self):

        pass


if __name__ == '__main__':
    testApp().run()
