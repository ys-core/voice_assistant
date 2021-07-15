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
import time

class testApp(CATBaseCase):

    def info(self):
        # author :
        # priority : High
        # description :
        # device info :
        # functions :
        # model :
        # updated : 2021-07-15 14:02:33
        # updated : 2021-07-15 15:35:37
        pass

    def setup(self):
        global startTime
        startTime = time.time()

        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description2",expect_value="Expect value2")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description3",expect_value="Expect value3")
        AT.sleep(sleepTime="400")


        pass

    def main(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description2",expect_value="Expect value2")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description3",expect_value="Expect value3")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description4",expect_value="Expect value4")
        AT.sleep(sleepTime="400")
        result = AT.get_max_time_tolerance()
        AT.ReportInfo(string=result)
        if (time.time() - startTime) > result:
            AT.MakeFail(text="produce a fail api")


        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description2",expect_value="Expect value2")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description3",expect_value="Expect value3")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description4",expect_value="Expect value4")
        AT.sleep(sleepTime="400")


        pass

    def teardown(self):
        StepDesc(step_desc="Step description1",expect_value="Expect value1")
        AT.sleep(sleepTime="400")
        StepDesc(step_desc="Step description2",expect_value="Expect value2")
        AT.sleep(sleepTime="400")
        pass


if __name__ == '__main__':
    testApp().run()
