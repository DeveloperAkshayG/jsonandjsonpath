import json

import jsonpath

dict='{"name":"joe","nationality":"british","mobileno":"6789543267","cities":["london","birmingham","old tafford"],"address":{"street":"abcd","house":"24d","job":{"company":"mercedes","position":"infotainment","location":"germany"}}}'

res=json.loads(dict)

print(res)

x=jsonpath.jsonpath(res,"cities")
print(x)

a=jsonpath.jsonpath(res,"cities[2]")
print(a)

b=jsonpath.jsonpath(res,"address.job.company")
print(b)