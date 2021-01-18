#!/usr/bin/python

import sys
sys.path.append("/home/pims/.local/lib/python3.9/site-packages")

import requests
import json
from zerotier import *

#dit is de key van een test netwerk
zeroTierKey = 'K0MgKsZFeGub9m8coz1go06siz3U6KO0'

zt = ZT(zeroTierKey)
test = zt.status

#print(json.dumps(test, indent=2, sort_keys=True))

print (zt.status)
for net in zt.list_networks():
    #print (json.dumps(net._json, indent=2, sort_keys=True))
    print "Network name: " + net.name + " and ID: " + net.id 
    for member in net.members:
        print "Member name: " + member.name + " tags: " + member.tags

