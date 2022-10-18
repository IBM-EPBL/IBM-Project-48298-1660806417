Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
sql = " your select query here "
service = "/sql_jobs"
r = requests.post(host+service,headers=auth_header,json=sql_command)
jobid = r.json()['id']
r = requests.get(host+service+"/"+jobid,headers=auth_header)
results = r.json()['results']
rows = results[0]['rows']


sql = " your insert/update/delete query here "
sql_command = {"commands":sql,"limit":1000,"separator":";","stop_on_error":"yes"}
service = "/sql_jobs"
r = requests.post(host+service,headers=auth_header,json=sql_command)
sql_command = {"commands":"COMMIT","limit":1000,"separator":";","stop_on_error":"yes"}
service = "/sql_jobs"
r = requests.post(host+service,headers