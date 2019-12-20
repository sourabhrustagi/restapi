import httplib2
import sys

print("Running Endpoint Tester....\n")

address = 'http://localhost:5000'

print("Making a GET Request for /puppies...")

try:
    url = address + "/puppies"
    h = httplib2.Http()
    resp, result = h.request(url, 'GET')
    if resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
    print("Test 1 FAILED: Could not make GET Request to web server")
    print(err.args)
else:
    print("Test 1 PASS: Successfully Made GET Request to /puppies")

print("Making a POST request to /puppies...")
try:
    url = address + "/puppies"
    h = httplib2.Http()
    resp, result = h.request(url, 'POST')
    if resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
    print("Test 2 FAILED: Could not make POST Request to web server")
    print(err.args)
else:
    print("Test 2 PASS: Successfully Made POST Request to /puppies")

print("Making GET requests to /puppies/id")

try:
    id = 1
    while id <= 10:
        url = address + "/puppies/%s" % id
        h = httplib2.Http()
        resp, result = h.request(url, 'GET')
        if resp['status'] != '200':
            raise Exception('Received an unsuccessful status code of %s' % resp['status'])
        id = id + 1

except Exception as err:
    print("Test 3 FAILED: Could not make GET requests to web server")
    print(err.args)
else:
    print("Test 3 PASS: Successfully Made GET request to /puppies/id")

print("Making PUT requests to /puppies/id")

try:
    id = 1
    while id <= 10:
        url = address + "/puppies/%s" % id
        h = httplib2.Http()
        resp, result = h.request(url, 'PUT')
        if resp['status'] != '200':
            raise Exception('Received an unsuccessful status code of %s' % resp['status'])
        id = id + 1

except Exception as err:
    print("Test 4 FAILED: Could not make PUT requests to web server")
    print(err.args)
else:
    print("Test 4 PASS: Successfully Made PUT request to /puppies/id")

print("Making PUT requests to /puppies/id")

try:
    id = 1
    while id <= 10:
        url = address + "/puppies/%s" % id
        h = httplib2.Http()
        resp, result = h.request(url, 'DELETE')
        if resp['status'] != '200':
            raise Exception('Received an unsuccessful status code of %s' % resp['status'])
        id = id + 1

except Exception as err:
    print("Test 5 FAILED: Could not make DELETE requests to web server")
    print(err.args)
else:
    print("Test 5 PASS: Successfully Made DELETE request to /puppies/id")

print("Making a get request to /readHello...")
try:
    url = address + "/readHello"
    h = httplib2.Http()
    resp, result = h.request(url, 'GET')
    if resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
    print("Test 6 FAILED: Could not make GET Request to web server")
    print(err.args)
else:
    print("Test 6 PASS: Successfully Made GET Request to /readHello")

print("Making a get request to /createHello...")
try:
    url = address + "/createHello"
    h = httplib2.Http()
    resp, result = h.request(url, 'POST')
    if resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
    print("Test 7 FAILED: Could not make POST Request to web server")
    print(err.args)
else:
    print("Test 7 PASS: Successfully Made POST Request to /createHello")

print("Making a get request to /updateHello...")
try:
    url = address + "/updateHello"
    h = httplib2.Http()
    resp, result = h.request(url, 'PUT')
    if resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
    print("Test 8 FAILED: Could not make PUT Request to web server")
    print(err.args)
else:
    print("Test 8 PASS: Successfully Made PUT Request to /updateHello")

print("Making a get request to /deleteHello...")
try:
    url = address + "/deleteHello"
    h = httplib2.Http()
    resp, result = h.request(url, 'DELETE')
    if resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
    print("Test 9 FAILED: Could not make DELETE Request to web server")
    print(err.args)
else:
    print("Test 9 PASS: Successfully Made DELETE Request to /deleteHello")

print("Making a get request to /testJson...")
try:
    url = address + "/testJson"
    h = httplib2.Http()
    resp, result = h.request(url, 'DELETE')
    if resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
    print("Test 10 FAILED: Could not make DELETE Request to web server")
    print(err.args)
else:
    print("Test 10 PASS: Successfully Made DELETE Request to /testJson")

print("Making a get request to /testJson...")
try:
    url = address
    h = httplib2.Http()
    resp, result = h.request(url, 'GET')
    if resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
    print("Test 11 FAILED: Could not make GET Request to web server")
    print(err.args)
else:
    print("Test 11 PASS: Successfully Made GET Request to /testJson")
