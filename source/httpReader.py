import os
from os.path import join, getsize
import http.client
import requests
from requests.auth import HTTPBasicAuth
from requests_ntlm import HttpNtlmAuth
username = 'AMERICAS\\gdlebric'
password = 'Qeehs46'
url = 'http://sacnte335/Reports/Pages/Folder.aspx'

s = requests.Session()
s.auth = HttpNtlmAuth(username, password)

r1 = s.get(url)

print ('r1', r1)

r1 = requests.get(url, auth=HTTPBasicAuth(username, password))

print ('r1', r1)
print(r1.headers)


r = requests.get("http://sacnte335/Reports/Pages/Folder.aspx",auth=(username, password))
print(r.status_code)
