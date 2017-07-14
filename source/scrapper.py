import urllib3

http = urllib3.PoolManager()
url = 'http://sacnte335/Reports/Pages/Folder.aspx?ItemPath=%2fATR_TEST&ViewMode=Detail&SortBy=Type&IsAscending=true'
headers = urllib3.util.make_headers(basic_auth='gdlebric:Qeehs46,')
r = http.request('GET', url, headers=headers)
print(r.status)
urllib3.contrib.ntlmpool.NTLMConnectionPool()