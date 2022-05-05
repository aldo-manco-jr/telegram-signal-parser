# import json
#
# with open('result.json') as fp:
#     data = json.loads(fp)
#
# for user in data:
#     print(user["text"])

import json

# some JSON:
with open('result.json', 'r') as file:
    data = file.read()

# parse x:
y = json.loads(data)

# the result is a Python dictionary:
for message in y["messages"]:
    print(message["text"])

