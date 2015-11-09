#!/usr/bin/python
# -*- coding: utf-8 -*-

import smbus
import time
import datetime
import argparse

__version__ = '0.1.0'

i2c = smbus.SMBus(1)

def pwr_mode():
   data = i2c.read_byte_data(0x69, 0x00)
   data = data & ~(1 << 7)
   if (data == 1):
      return 'RPi'
   elif (data == 2):
      return 'BAT'
   else:
      return 'ERR'

def bat_level():
   time.sleep(0.1)
   data = i2c.read_word_data(0x69, 0x01)
   data = format(data,'02x')
   return (float(data) / 100)

def rpi_level():
   time.sleep(0.1)
   data = i2c.read_word_data(0x69, 0x03)
   data = format(data,'02x')
   return (float(data) / 100)

def fw_version():
   time.sleep(0.1)
   data = i2c.read_byte_data(0x6b, 0x00)
   data = format(data,'02x')
   return data

def main():
   parser = argparse.ArgumentParser(description='Request status information from UPS Pico using I2C.')
   parser.add_argument('-f', '--firmware', action='store_true', help='')
   parser.add_argument('-m', '--powermode', action='store_true', help='')
   parser.add_argument('-b', '--battery', action='store_true', help='')
   parser.add_argument('-p', '--rpi', action='store_true', help='')

   args = parser.parse_args()

   print_all = False
   if not args.firmware and not args.powermode and not args.battery and not args.rpi:
      print_all = True

   if print_all:
      print('ups pico status tool v', __version__)
   if args.firmware or print_all:
      print('UPS PIco Firmware:', fw_version())
   if args.powermode or print_all:
      print('Powering Mode:    ', pwr_mode())
   if args.battery or print_all:
      print('BAT Volatge:      ', bat_level(), 'V')
   if args.rpi or print_all:
      print('RPi Voltage:      ', rpi_level(), 'V')

   return 0

if __name__ == '__main__':
   quit(main())
