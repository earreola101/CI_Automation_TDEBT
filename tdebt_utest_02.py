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
    
    #TEST_SetMacaddressBT-Tdebt.exe -c tvhub -s macaddress 111234567899
    def TEST_SetMacaddressBT(self):
        print("TEST_SetMacaddressBT ")
        cmdStr=tdebt+" -c tvhub -s macaddress 111234567899"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("[OK]",r)
        return
		
    #TEST_GetMacaddressBT-Tdebt.exe -c tvhub -g macaddress
    def TEST_GetMacaddressBT(self):
        print("TEST_GetMacaddressBT")
        cmdStr=tdebt+" -c tvhub -g macaddress "
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("111234567899",r)
        return
   
    #TEST_Settvhub_ble_peripheral_address-tdebt.exe -c tvhub -s tvhub_ble_peripheral_address 4467e23d4686
    def TEST_Settvhub_ble_peripheral_address(self):
        print("TEST_tdebt_SetMacaddress ")
        cmdStr=tdebt+" -c tvhub -s tvhub_ble_peripheral_address 4467e23d4686"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("[OK]",r)
        return
		
    #test_GetMacaddressBT-Tdebt.exe -c tvhub -g tvhub_ble_peripheral_address
    def TEST_Gettvhub_ble_peripheral_address(self):
        print("TEST_Gettvhub_ble_peripheral_address")
        cmdStr=tdebt+" -c tvhub -g tvhub_ble_peripheral_address "
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("111234567899",r)
        return
	
    #test_Settde_unique_id-Tdebt.exe -c tvhub -s tde_unique_id 1111222233334444
    def test_Settde_unique_id(self):
        print("test_Settde_unique_id ")
        cmdStr=tdebt+" -c tvhub -s tde_unique_id 1111222233334444"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("[OK]",r)
        return
		
	#test_GetTde_unique_id-Tdebt.exe -c tvhub -g tde_unique_id
    def TEST_Gettde_unique_id(self):
        print("test_GetTde_unique_id")
        cmdStr=tdebt+" -c tvhub -g tde_unique_id"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("1111222233334444",r)
        return	
   

   	#test_Gettvhub_cec_status-tdebt.exe -c tvhub -g tvhub_cec_status
    def test_Gettvhub_cec_status(self):
        print("test_Gettvhub_cec_status")
        cmdStr=tdebt+" -c tvhub -g tvhub_cec_status"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("0",r)
        return

   	#TEST_Gettvhub_chrontel_status-tdebt.exe -c tvhub -g tvhub_chrontel_status
    def TEST_Gettvhub_chrontel_status(self):
        print("TEST_Gettvhub_chrontel_status")
        cmdStr=tdebt+" -c tvhub -g tvhub_chrontel_status"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("0",r)
        return	
    
   	#TEST_Gettvhub_ble_peripheral_address-tdebt.exe -c tvhub -s tvhub_ble_peripheral_address 4467e23d4686
    def TEST_Gettvhub_ble_peripheral_address(self):
        print("test_GetTde_unique_id")
        cmdStr=tdebt+" -c tvhub -s tvhub_ble_peripheral_address 4467e23d4686"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("0",r)
        return	
    


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	#tdebt.exe -c tvhub -g tvhub_ble_peripheral_address

	#tdebt.exe -c tvhub -s tvhub_ble_central_address 4467e23d4686

	#tdebt.exe -c tvhub -g tvhub_ble_central_address

	#tdebt.exe -c tvhub -s tvhub_ble_camera_address eedd55e83755

	#tdebt.exe -c tvhub -g tvhub_ble_camera_address

    #tdebt.exe -c tvhub -s tde_test_tracking_data 11112222333344445555666677778888

    #tdebt.exe -c tvhub -g tde_test_tracking_data

	#tdebt.exe -c tvhub -s macaddress 4467e23d4686

	#tdebt.exe -c tvhub -g macaddress

	#tdebt.exe -c tvhub -s radiotxdata

	#tdebt.exe -c tvhub -s bt_uartdisable

	#tdebt.exe -c tvhub -s pskey 36

	#tdebt.exe -c tvhub -g pskey

	#tdebt.exe -c tvhub -s tvhub_led 1

	#tdebt.exe -c tvhub -s tvhub_led 0

	#tdebt.exe -c tvhub -s tvhub_spplib_bypass 1  (bypass)

	#tdebt.exe -c tvhub -s tvhub_spplib_bypass 0  (not bypass)

	#tdebt.exe -c tvhub -g btn_status		

if __name__ == '__main__':
    with open('results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
