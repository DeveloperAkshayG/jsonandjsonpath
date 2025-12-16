import json

import jsonpath

mydict='{"name":"testingworld","age":"24","phonenumber":"8765432109","cities":["delhi","mumbai","pune"]}'

json_result=json.loads(mydict)
print(json_result)

# to extract age
x=jsonpath.jsonpath(json_result,"age")
print(x)

# to extract phone number
y=jsonpath.jsonpath(json_result,"phonenumber")
print(y)

# to extract cities
z=jsonpath.jsonpath(json_result,"cities")
print(z)

# to extract mumbai from cities
m=jsonpath.jsonpath(json_result,"cities[1]")
print(m)