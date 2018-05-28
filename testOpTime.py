'''
Test module for OpTime
'''
import os
import sys
import nose2

from optoolbox import OpTime
from optoolbox import optest


class OpTimeTestCase(optest.TestCase):

    def testGetTime(self):
        """
        This test checks that GetTime returns a floating point number.
        """
        value = OpTime.GetTime()
        self.failUnless(isinstance(value,float))
        
    def testTimeNumberAsString(self):
        """
        This test checks that GetTimeNumberAsString returns a string, and when converting this string to a number,
        the number is an int.
        """
        timeString = OpTime.GetTimeNumberAsString(OpTime.GetTime())
        self.failUnless(isinstance(timeString, basestring))
        timeInt = int(timeString)
        timeFloat = float(timeString)
        self.failUnless(timeInt == timeFloat)
        
    def testTimeString(self):
        print OpTime.GetTimeString()
        
    def testDiffTimeString(self):
        msg = "The tested method does not return proper strings."
        elapsed = OpTime.GetDiffTimeString(5)
        self.failUnless(elapsed.find('seconds')>-1, msg)
        elapsed = OpTime.GetDiffTimeString(65)
        self.failUnless(elapsed.find('minutes')>-1, msg)
        elapsed = OpTime.GetDiffTimeString(3605)
        self.failUnless(elapsed.find('hours')>-1, msg)

        
        
if __name__ == '__main__':
    #optest.main()
    cfg_path=os.path.normpath(os.path.join(os.environ['OPTOOLBOX'], '..', 'tests', 'unittest.cfg'))
    argv =[sys.argv[0], '--config', cfg_path]
    nose2.main(module='testOpTime', argv=argv)