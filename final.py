# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.2)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xcc\
\x00\
\x00\x11\xeb\x78\x9c\xeb\x0c\xf0\x73\xe7\xe5\x92\xe2\x62\x60\x60\
\xe0\xf5\xf4\x70\x09\x62\x60\x60\x59\xca\xc0\xc0\x34\x85\x83\x0d\
\x28\x72\xd5\xbb\xbb\x12\x48\x71\x16\x78\x44\x16\x33\x30\x70\x0b\
\x83\x30\x23\xc3\xac\x39\x12\x40\x41\xc6\xe2\x20\x77\x27\x86\x75\
\xe7\x64\x5e\x02\x39\x2c\xe9\x8e\xbe\x8e\x0c\x0c\x1b\xfb\xb9\xff\
\x24\xb2\x32\x30\x08\x36\x78\xba\x38\x86\x54\x30\xbe\xbd\x61\xc8\
\xc8\xa0\xc0\xc0\xb2\xf0\xfa\xbf\xb9\x5b\x8f\xfa\x0a\x34\x6f\x7e\
\xcb\x0b\x54\xcd\xe0\x54\x0e\x22\x05\x26\x07\x81\xa8\x27\x4b\x44\
\x40\x94\xa5\x26\x50\x23\x83\x83\x9f\x17\x23\x90\x9a\x30\x2a\x35\
\x2a\x35\x2a\x35\x2a\x35\x2a\x35\x2a\x35\x2a\x35\x2a\x35\x2a\x35\
\x2a\x35\x2a\x35\x2a\x35\x2a\x35\x2a\x35\x2a\x35\x2a\x35\x2a\x85\
\x4f\x6a\x27\xff\x8a\x05\x6c\xea\xac\x97\xbf\x9a\x83\x78\x9e\xae\
\x7e\x2e\xeb\x9c\x12\x9a\x00\x90\x27\xea\xfe\
"

qt_resource_name = b"\
\x00\x05\
\x00\x6d\x04\x7c\
\x00\x66\
\x00\x69\x00\x6e\x00\x61\x00\x6c\
\x00\x06\
\x06\x8a\x57\x47\
\x00\x62\
\x00\x67\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x10\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x10\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x82\x91\x88\x39\x72\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
