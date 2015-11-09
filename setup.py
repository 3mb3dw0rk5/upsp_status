#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from upsp_status.version import __version__

setup(name='upsp_status',
      version=__version__,
      description='Tool to get status of UPS Pico via I2C.',
      author='Erik Wofl',
      author_email='3mb3dw0rk5@users.noreply.github.com',
      url='https://github.com/3mb3dw0rk5/upsp_status',
      packages=['upsp_status'],
      scripts=['upsp_status/upsp_status.py']
     )
