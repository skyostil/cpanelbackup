#!/usr/bin/python
import urllib2
import base64
import sys

if not len(sys.argv) > 3:
    print "Usage: %s domain authfile dbname filename" % sys.argv[0]
    sys.exit(1)

domain = sys.argv[1]
#auth = base64.encodestring("username:password")
auth = open(sys.argv[2]).read()
dbname = sys.argv[3]
url = "https://%s:2083/getsqlbackup/%s.sql.gz" % (domain, dbname)

headers = {
    "Authorization": "Basic " + auth,
    "Connection": "Close"
}

req = urllib2.Request(url, headers = headers)
out = open(sys.argv[4], "wb")

# Should not really read the whole DB into memory here but oh well
out.write(urllib2.urlopen(req).read())
out.close()
