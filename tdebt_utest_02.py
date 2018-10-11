import subprocess
import sys,string,os
import serial
import random
import unittest
import xmlrunner
from timeit import default_timer
from time import sleep
# Automated TDE mode test version 0.1 .0

tdebt = "./tdebt.exe"

class TDE_Modes(unittest.TestCase):

    #1. test_SetMacaddressBT# - tdebt.exe - c tvhub - s macaddress 111234567899
    def test_SetMacaddressBT(self):
        print("test_SetMacaddressBT ")
        cmdStr = tdebt + " -c tvhub -s macaddress 111234567899"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("[OK]", r)
        return

    #2. test_GetMacaddressBT# - tdebt.exe - c tvhub - g macaddress
    def test_GetMacaddressBT(self):
        print("test_GetMacaddressBT")
        cmdStr = tdebt + " -c tvhub -g macaddress"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("111234567899", r)
        return

    #3. test_Settvhub_ble_peripheral_address# - tdebt.exe - c tvhub - s tvhub_ble_peripheral_address 4467e23 d4686
    def test_Settvhub_ble_peripheral_address(self):
        print("test_Settvhub_ble_peripheral_address")
        cmdStr = tdebt + " -c tvhub -s tvhub_ble_peripheral_address 4467e23d4686 "
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("[OK]", r)
        return

    #4. test_Gettvhub_ble_peripheral_address# - tdebt.exe - c tvhub - g tvhub_ble_peripheral_address
    def test_Gettvhub_ble_peripheral_address(self):
        print "test_Gettvhub_ble_peripheral_address"
        cmdStr = tdebt + " -c tvhub -g tvhub_ble_peripheral_address "
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("111234567899", r)
        return

    #5. test_Settde_unique_id# - tdebt.exe - c tvhub - s tde_unique_id 1111222233334444
    def test_Settde_unique_id(self):
        print "test_Settde_unique_id "
        cmdStr = tdebt + " -c tvhub -s tde_unique_id 1111222233334444 "
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("[OK]", r)
        return

    #6. test_GetTde_unique_id# - tdebt.exe - c tvhub - g tde_unique_id
    def test_Gettde_unique_id(self):
        print "test_GetTde_unique_id"
        cmdStr = tdebt + " -c tvhub -g tde_unique_id"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("1111222233334444", r)
        return

    #7. test_Gettvhub_cec_status# - tdebt.exe - c tvhub - g tvhub_cec_status
    def test_Gettvhub_cec_status(self):
        print "test_Gettvhub_cec_status"
        cmdStr = tdebt + " -c tvhub -g tvhub_cec_status"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("0", r)
        return

    #8. test_Gettvhub_chrontel_status# - tdebt.exe - c tvhub - g tvhub_chrontel_status
    def test_Gettvhub_chrontel_status(self):
        print "test_Gettvhub_chrontel_status"
        cmdStr = tdebt + " -c tvhub -g tvhub_chrontel_status"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("0", r)
        return

    #9. test_Settvhub_ble_central_address# - tdebt.exe - c tvhub - s tvhub_ble_central_address 4467e23 d4686
    def test_Settvhub_ble_central_address(self):
        print "test_Settvhub_ble_central_address"
        cmdStr = tdebt + " -c tvhub -s tvhub_ble_central_address 4467e23d4686"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("[OK]", r)
        return

        
    #10.test_Gettvhub_ble_central_address# - tdebt.exe - c tvhub - g tvhub_ble_central_address
    def test_Gettvhub_ble_central_address(self):
        print "test_Gettvhub_ble_central_address"
        cmdStr = tdebt + " -c tvhub -g tvhub_ble_central_address"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("0", r)
        return

    #11.test_Settvhub_ble_camera_address# - tdebt.exe - c tvhub - s tvhub_ble_camera_address eedd55e83755
    def test_Settvhub_ble_camera_address(self):
        print "test_Settvhub_ble_camera_address"
        cmdStr = tdebt + " -c tvhub -s tvhub_ble_camera_address eedd55e83755"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("[OK]", r)
        return

    #12.test_Gettvhub_ble_camera_address# - tdebt.exe - c tvhub - g tvhub_ble_camera_address
    def test_Gettvhub_ble_camera_address(self):
        print "test_Gettvhub_ble_camera_address"
        cmdStr = tdebt + " -c tvhub -g tvhub_ble_camera_address"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("0", r)
        return


    #13.test_Settde_test_tracking_data# - tdebt.exe - c tvhub - s tde_test_tracking_data 11112222333344445555666677778888
    def test_Settde_test_tracking_data(self):
        print "TESTSettde_test_tracking_data"
        cmdStr = tdebt + " -c tvhub -c tvhub -s tde_test_tracking_data 11112222333344445555666677778888"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("[OK]", r)
        return

#14.test_Gettvhub_tde_test_tracking_data# - tdebt.exe - c tvhub - g tde_test_tracking_data
    def TESTGettvhub_tde_test_tracking_data(self):
        print "TESTGettvhub_tde_test_tracking_data"
        cmdStr = tdebt + " -c tvhub -g tde_test_tracking_data"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("0", r)
        return

    #15.test_Setpskey# - tdebt.exe - c tvhub - s pskey 36
    def TESTSetpskey(self):
        print "TESTSetpskey"
        cmdStr = tdebt + " -c tvhub -c tvhub -s pskey 36"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("[OK]", r)
        return

    #16.test_Getpskey# - tdebt.exe - c tvhub - g pskey
    def test_Getpskey(self):
        print "TESTGetpskey"
        cmdStr = tdebt + " -c tvhub -g pskey"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("0", r)
        return

    #17.test_Settvhub_led# - tdebt.exe - c tvhub - s tvhub_led 0
    def test_Settvhub_led(self):
        print "TESTSettvhub_led"
        cmdStr = tdebt + " -c tvhub -s tvhub_led 1"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("[OK]", r)
        return

    #18.test_Settvhub_led# - tdebt.exe - c tvhub - s tvhub_led 1
    def test_Settvhub_led(self):
        print "TESTSettvhub_led"
        cmdStr = tdebt + " -c tvhub -s tvhub_led 1"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("[OK]", r)
        return

    #19.test_Getbtn_status# - tdebt.exe - c tvhub - g btn_status
    def test_Getbtn_status(self):
        print "TESTGetbtn_status"
        cmdStr = tdebt + " -c tvhub -g btn_status"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("0", r)
        return

    #20.test_Settvhub_spplib_bypass# - tdebt.exe - c tvhub - s tvhub_spplib_bypass 1(bypass)
    def test_Settvhub_led(self):
        print "TESTSettvhub_led"
        cmdStr = tdebt + " -c tvhub -s tvhub_spplib_bypass 1"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("[OK]", r)
        return

    #21.test_Settvhub_spplib_bypass# - tdebt.exe - c tvhub - s tvhub_spplib_bypass 1(bypass)
    def test_Settvhub_led(self):
        print "TESTSettvhub_led"
        cmdStr = tdebt + " -c tvhub -s tvhub_spplib_bypass 0"
        r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
        print "OUTPUT: " + r + "\r\n"
        self.assertEqual("[OK]", r)
        return        
    # DANGER Requires hard power cycle to recover.#tdebt.exe - c tvhub - s radiotxdata# tdebt.exe - c tvhub - s bt_uartdisable

if __name__ == '__main__':
    with open('results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)