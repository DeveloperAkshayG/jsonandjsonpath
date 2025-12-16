import json

import jsonpath

mydict='{"name":"testingworld","age":"24","phonenumber":"8765432109","cities":["delhi","mumbai","pune"],"address":{"house":"23d","street":"westavenue","city":"oro"}}'

jsonresponse=json.loads(mydict)

print(jsonresponse)

x=jsonpath.jsonpath(jsonresponse,"cities")
print(x)

y=jsonpath.jsonpath(jsonresponse,"cities[2]")
print(y)

z=jsonpath.jsonpath(jsonresponse,"address")
print(z)

a=jsonpath.jsonpath(jsonresponse,"address.street")
print(a)