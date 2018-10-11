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
        self.assertEqual("111234567899",r)
        return
   

    #tdebt.exe -c tvhub -g fwversion
    def test_Getfwversion(self):
        print("test_Getfwversion")
        cmdStr=tdebt+" -c tvhub -g fwversion "
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("111234567899",r)
        return
		

    #tdebt.exe -c tvhub -s tde_unique_id 1111222233334444
    def test_SetTde_unique_id(self):
        print("test_SetTde_unique_id ")
        cmdStr=tdebt+" -c tvhub -s tde_unique_id 1111222233334444"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("[OK]",r)
        return		
		
    #tdebt.exe -c tvhub -s serialnumber 111111111222222222
    def test_Setserialnumber(self):
        print("test_Setserialnumber ")
        cmdStr=tdebt+" -c tvhub -s serialnumber 111111111222222222"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("[OK]",r)
        return	
		
		
		
    #tdebt.exe -c tvhub -g tvhub_valens_status
    def test_Gettvhub_valens_status(self):
        print("test_tvhub_valens_status")
        cmdStr=tdebt+" -c tvhub -g tvhub_valens_status"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("111234567899",r)
        return		

    #tdebt.exe -c tvhub -g tvhub_ble_status
    def test_GetTvhub_ble_status(self):
        print("test_GetTvhub_ble_status")
        cmdStr=tdebt+" -c tvhub -g tvhub_ble_status"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("111234567899",r)
        return

if __name__ == '__main__':
    with open('results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
