# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.2.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xb5\
i\
mport QtQuick\x0d\x0a\x0d\
\x0aRectangle {\x0d\x0a  \
  id: main\x0d\x0a    \
width: 400\x0d\x0a    \
height: 300\x0d\x0a   \
 color: \x22green\x22\x0d\
\x0a\x0d\x0a    Text {\x0d\x0a \
       text: \x22He\
llo World\x22\x0d\x0a    \
    anchors.cent\
erIn: main\x0d\x0a    \
}\x0d\x0a}\
"

qt_resource_name = b"\
\x00\x03\
\x00\x00x\xc3\
\x00r\
\x00e\x00s\
\x00\x08\
\x0f\xca[\xbc\
\x00v\
\x00i\x00e\x00w\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01|\xcf\xff\xd7[\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
