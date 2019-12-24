import json
import sys
from urllib.parse import urlencode

from httplib2 import Http

address = 'http://localhost:5000'

try:
    url = address + '/api/users'
    h = Http()
    data = dict(username="TinnyTim", password="Udacity")
    data = json.dumps(data)
    resp, content = h.request(url, 'POST', body=data, headers={"Content-Type": "application/json"})
    if resp['status'] != '201' and resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
    print("Test 1 FAILED: Could not make a new user")
    print(err.args)
    sys.exit()
else:
    print("Test 1 PASS: Successfully made a new user")

try:
    h = Http()
    h.add_credentials('TinnyTim', 'Udacity')
    url = address + '/bagels'
    data = dict(username="TinnyTim", password="Udacity", name="plain",
                picture="http://bonacbagel.weebly.com/uploads/4/0/5/4/40548977/s318635836612132814_p1_i1_w240.jpeg",
                description="Old-Fashioned Plain Bagel", price="$1.99")
    resp, content = h.request(url, 'POST', body=json.dumps(data), headers={"Content-Type": "application/json"})
    if resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
    print("Test 2 FAILED: Could not add new bagels")
    print(err.args)
    sys.exit()
else:
    print("Test 2 PASS: Successfully made new bagels")

try:
    h = Http()
    h.add_credentials('TinnyTim', 'Youdacity')
    url = address + '/bagels'
    data = dict(username="Tinny_Tim", password="youdacity")
    resp, content = h.request(url, 'GET', urlencode(data))
    if resp['status'] == '200':
        raise Exception("Security Flaw: able to log in with invalid credentials")
except Exception as err:
    print("Test 3 Failed")
    print(err.args)
    sys.exit()
else:
    print("Test 3 Pass: App checks against invalid credentials")

try:
    h = Http()
    h.add_credentials("TinnyTim", "Udacity")
    url = address + '/bagels'
    resp, content = h.request(url, 'GET')
    if resp['status'] != '200':
        raise Exception("Unable to access /bagels with valid credentials")
except Exception as err:
    print("Test 4 Failed")
    print(err.args)
    sys.exit()
else:
    print("Test 4 Pass: Logged in User can view /bagels")
    print("All Tests Passed!")
