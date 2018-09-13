import subprocess
import sys,string,os
import serial
import random
import unittest
import xmlrunner
from timeit import default_timer
from time import sleep

#automated TDE mode test version 0.1.0

tdebt="./tdebt.exe"

class TDE_Modes(unittest.TestCase):
    
    #test_SetMacaddressBT-TDETool.exe -c tvhub -s macaddress 111234567899
    def test_SetMacaddressBT(self):
        print("TEST_tdebt_SetMacaddress ")
        cmdStr=tdebt+" -c tvhub -s macaddress 111234567899"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("[OK]",r)
        return

        
    #test_GetMacaddressBT
    def test_GetMacaddressBT(self):
        print("TEST GetMacaddress")
        cmdStr=tdebt+" -c tvhub -g macaddress "
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("001122334455",r)
        return
        
if __name__ == '__main__':
    with open('results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
