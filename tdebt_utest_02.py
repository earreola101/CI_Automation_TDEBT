import subprocess
import sys,string,os
import serial
import random
import unittest
import xmlrunner
from timeit import default_timer
from time import sleep
# Automated TDE mode test version 0.1 .0
tdebt = './tdebt.exe'

class TDE_Modes(unittest.TestCase):

  #TEST_SetMacaddressBT
  # - tdebt.exe - c tvhub - s macaddress 111234567899
def TEST_SetMacaddressBT(self):
    print 'TEST_SetMacaddressBT '
    cmdStr = tdebt + ' -c tvhub -s macaddress 111234567899'
    r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
    r = r.replace('\r\n', ' ')
    r = r.replace(' ', ' ')
    print 'OUTPUT: ' + r + '\r\n'
    self.assertEqual('[OK]', r)
    return

  # TEST_GetMacaddressBT
  # - tdebt.exe - c tvhub - g macaddress
def TEST_GetMacaddressBT(self):
    print 'TEST_GetMacaddressBT'
    cmdStr = tdebt + ' -c tvhub -g macaddress'
    r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
    print 'OUTPUT: ' + r + '\r\n'
    self.assertEqual('111234567899', r)
    return

  # TEST_Settvhub_ble_peripheral_address
  # - tdebt.exe - c tvhub - s tvhub_ble_peripheral_address 4467e23 d4686
def TEST_Settvhub_ble_peripheral_address(self):
    print 'TEST_Settvhub_ble_peripheral_address'
    cmdStr = tdebt\ + ' -c tvhub -s tvhub_ble_peripheral_address 4467e23d4686'
    r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
    r = r.replace('\r\n', ' ')
    r = r.replace(' ', ' ')
    print 'OUTPUT: ' + r + '\r\n'
    self.assertEqual('[OK]', r)
    return

  # TEST_Gettvhub_ble_peripheral_address
  # - tdebt.exe - c tvhub - g tvhub_ble_peripheral_address
def TEST_Gettvhub_ble_peripheral_address(self):
    print 'TEST_Gettvhub_ble_peripheral_address'
    cmdStr = tdebt + ' -c tvhub -g tvhub_ble_peripheral_address '
    r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
    print 'OUTPUT: ' + r + '\r\n'
    self.assertEqual('111234567899', r)
    return

  # TEST_Settde_unique_id
  # - tdebt.exe - c tvhub - s tde_unique_id 1111222233334444
def test_Settde_unique_id(self):
    print 'test_Settde_unique_id '
    cmdStr = tdebt + ' -c tvhub -s tde_unique_id 1111222233334444'
    r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
    r = r.replace('\r\n', ' ')
    r = r.replace(' ', ' ')
    print 'OUTPUT: ' + r + '\r\n'
    self.assertEqual('[OK]', r)
    return

  # TEST_GetTde_unique_id
  # - tdebt.exe - c tvhub - g tde_unique_id
def TEST_Gettde_unique_id(self):
    print 'test_GetTde_unique_id'
    cmdStr = tdebt + ' -c tvhub -g tde_unique_id'
    r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
    print 'OUTPUT: ' + r + '\r\n'
    self.assertEqual('1111222233334444', r)
    return

  # TEST_Gettvhub_cec_status
  # - tdebt.exe - c tvhub - g tvhub_cec_status
def test_Gettvhub_cec_status(self):
    print 'test_Gettvhub_cec_status'
    cmdStr = tdebt + ' -c tvhub -g tvhub_cec_status'
    r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
    print 'OUTPUT: ' + r + '\r\n'
    self.assertEqual('0', r)
    return

  # TEST_Gettvhub_chrontel_status
  # - tdebt.exe - c tvhub - g tvhub_chrontel_status
def TEST_Gettvhub_chrontel_status(self):
	print 'TEST_Gettvhub_chrontel_status'
	cmdStr = tdebt + ' -c tvhub -g tvhub_chrontel_status'
	r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
	print 'OUTPUT: ' + r + '\r\n'
	self.assertEqual('0', r)
	return

  # TEST_Settvhub_ble_central_address
  # - tdebt.exe - c tvhub - s tvhub_ble_central_address 4467e23 d4686
def TEST_Settvhub_ble_central_address(self):
    print 'TEST_Settvhub_ble_central_address'
    cmdStr = tdebt\ + ' -c tvhub -s tvhub_ble_central_address 4467e23d4686'
    r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
    print 'OUTPUT: ' + r + '\r\n'
    self.assertEqual('[OK]', r)
    return

  # TEST_Gettvhub_ble_central_address
  # - tdebt.exe - c tvhub - g tvhub_ble_central_address
def TEST_Gettvhub_ble_central_address(self):
	print 'TEST_Gettvhub_ble_central_address'
	cmdStr = tdebt + ' -c tvhub -g tvhub_ble_central_address'
	r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
	print 'OUTPUT: ' + r + '\r\n'
	self.assertEqual('0', r)
	return

  # TEST_Settvhub_ble_camera_address
  # - tdebt.exe - c tvhub - s tvhub_ble_camera_address eedd55e83755
def TEST_Settvhub_ble_camera_address(self):
	print 'TEST_Settvhub_ble_camera_address'
	cmdStr = tdebt\ + ' -c tvhub -s tvhub_ble_camera_address eedd55e83755'
	r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
	print 'OUTPUT: ' + r + '\r\n'
	self.assertEqual('[OK]', r)
	return

  # TEST_Gettvhub_ble_camera_address
  # - tdebt.exe - c tvhub - g tvhub_ble_camera_address
def TESTGettvhub_ble_camera_address(self):
	print 'TESTGettvhub_ble_camera_address'
	cmdStr = tdebt + ' -c tvhub -g tvhub_ble_camera_address'
	r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
	print 'OUTPUT: ' + r + '\r\n'
	self.assertEqual('0', r)
	return

  # TEST_Settde_test_tracking_data
  # - tdebt.exe - c tvhub - s tde_test_tracking_data 11112222333344445555666677778888
def TESTSettde_test_tracking_data(self):
	print 'TESTSettde_test_tracking_data'
	cmdStr = tdebt\ + ' -c tvhub -c tvhub -s tde_test_tracking_data 11112222333344445555666677778888'
	r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
	print 'OUTPUT: ' + r + '\r\n'
	self.assertEqual('[OK]', r)
	return

  # TEST_Gettvhub_tde_test_tracking_data
  # - tdebt.exe - c tvhub - g tde_test_tracking_data
def TESTGettvhub_tde_test_tracking_data(self):
	print 'TESTGettvhub_tde_test_tracking_data'
	cmdStr = tdebt + ' -c tvhub -g tde_test_tracking_data'
	r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
	print 'OUTPUT: ' + r + '\r\n'
	self.assertEqual('0', r)
	return

  # TEST_Setpskey
  # - tdebt.exe - c tvhub - s pskey 36
def TESTSetpskey(self):
	print 'TESTSetpskey'
	cmdStr = tdebt + ' -c tvhub -c tvhub -s pskey 36'
	r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
	print 'OUTPUT: ' + r + '\r\n'
	self.assertEqual('[OK]', r)
	return

  # TEST_Getpskey
  # - tdebt.exe - c tvhub - g pskey
def TESTGetpskey(self):
	print 'TESTGetpskey'
	cmdStr = tdebt + ' -c tvhub -g pskey'
	r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
	print 'OUTPUT: ' + r + '\r\n'
	self.assertEqual('0', r)
	return

  # TEST_Settvhub_led
  # - tdebt.exe - c tvhub - s tvhub_led 0
def TESTSettvhub_led(self):
	print 'TESTSettvhub_led'
	cmdStr = tdebt + ' -c tvhub -s tvhub_led 1'
	r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
	print 'OUTPUT: ' + r + '\r\n'
	self.assertEqual('[OK]', r)
	return

  # TEST_Settvhub_led
  # - tdebt.exe - c tvhub - s tvhub_led 1
def TESTSettvhub_led(self):
	print 'TESTSettvhub_led'
	cmdStr = tdebt + ' -c tvhub -s tvhub_led 1'
	r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
	print 'OUTPUT: ' + r + '\r\n'
	self.assertEqual('[OK]', r)
	return

  # TEST_Getbtn_status
  # - tdebt.exe - c tvhub - g btn_status
def TESTGetbtn_status(self):
	print 'TESTGetbtn_status'
	cmdStr = tdebt + ' -c tvhub -g btn_status'
	r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
	print 'OUTPUT: ' + r + '\r\n'
	self.assertEqual('0', r)
	return

  # TEST_Settvhub_spplib_bypass
  # - tdebt.exe - c tvhub - s tvhub_spplib_bypass 1(bypass)
def TESTSettvhub_led(self):
	print 'TESTSettvhub_led'
	cmdStr = tdebt + ' -c tvhub -s tvhub_spplib_bypass 1'
	r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
	print 'OUTPUT: ' + r + '\r\n'
	self.assertEqual('[OK]', r)
	return

  # TEST_Settvhub_spplib_bypass
  # - tdebt.exe - c tvhub - s tvhub_spplib_bypass 1(bypass)
def TESTSettvhub_led(self):
	print 'TESTSettvhub_led'
	cmdStr = tdebt + ' -c tvhub -s tvhub_spplib_bypass 0'
	r = subprocess.check_output(cmdStr, stderr = subprocess.STDOUT)
	print 'OUTPUT: ' + r + '\r\n'
	self.assertEqual('[OK]', r)
	return

  # DANGER Requires hard power cycle to recover.
  #tdebt.exe - c tvhub - s radiotxdata
  #tdebt.exe - c tvhub - s bt_uartdisable

if __name__ == '__main__':
  with open('results.xml', 'wb') as output:
  unittest.main(testRunner = xmlrunner.XMLTestRunner(output = output),
    failfast = False, buffer = False, catchbreak = False)