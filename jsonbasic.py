import json
import jsonpath

odics='{"k1":"v1","k2":"v2","k3":"v3"}'

json_result = json.loads(odics)

print(json_result)

x=jsonpath.jsonpath(json_result,"k2")
print(x)