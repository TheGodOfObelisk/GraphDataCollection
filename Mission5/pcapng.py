#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from scapy.all import *
package = rdpcap('DESKTOP-AK8ARRP_20190603_144850.pcapng')
print package[7]
