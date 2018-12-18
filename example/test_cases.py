import unittest
from ExtentHTMLTestRunner import HTMLTestRunner
# python 3.6

class case_01_test(unittest.TestCase):
    """testcase 01"""
    def setUp(self):
        print("--->")

    def test_case_01(self):
        print("test_01")
        print("--->>>")

    def tearDown(self):
        pass

class case_02_test(unittest.TestCase):
    """testcase 02"""
    def setUp(self):
        print("--->")

    def test_case_02(self):
        print("test_02")
        # Name and print in this format "screenshot_*.png" if you want to show screenshot in report.
        # print("screenshot_122323.png")
        assert 1 == 2
        print("--->>>")


    def tearDown(self):
        pass

if __name__ == "__main__":
    # unittest
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(case_01_test))
    suite.addTest(unittest.makeSuite(case_02_test))
    fp = open("report.html", 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='test report',
                            description='test report detail:')
    runResult = runner.run(suite)
    fp.close()