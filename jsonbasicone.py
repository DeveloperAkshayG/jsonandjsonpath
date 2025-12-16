import json

import jsonpath

mydic='{"name":"joe","mobileno":"9810931432","city":"london"}'

json_result=json.loads(mydic)

print(json_result)
print(type(json_result))

x=jsonpath.jsonpath(json_result,"mobileno")
print(x)