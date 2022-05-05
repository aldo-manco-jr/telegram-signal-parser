# import json
#
# with open('result.json') as fp:
#     data = json.loads(fp)
#
# for user in data:
#     print(user["text"])

import json

file = open("messages.txt", "r")
content = file.read().split("\n")

for line in content:
    if (line.lower().find("sl") != -1 or line.lower().find("tp") != -1 or line.lower().find("buy") != -1 or line.lower().find("sell") != -1) and line.lower().find("target") == -1 and line.lower().find("breakeven") == -1 and line.lower().find("running") == -1 and line.lower().find("[") == -1 and line.lower().find("]") == -1 and line.lower().find("hit")==-1 and line.lower().find("pip") == -1 and line.lower().find("put") == -1 and line.lower().find("pattern") == -1 and line.lower().find("signal") == -1 and line.lower().find("h4") == -1 and line.lower().find("wait") == -1 and line.lower().find("remove") == -1 and line.lower().find("touch") == -1 and line.lower().find("drop") == -1 and line.lower().find("again") == -1 and line.lower().find("read") == -1 and line.lower().find("time") == -1 and line.lower().find("mean") == -1 and line.lower().find("big") == -1 and line.lower().find("modif") == -1 and line.lower().find("too") == -1 and line.lower().find("will") == -1 and line.lower().find("tell") == -1 and line.lower().find("when") == -1 and line.lower().find("we") == -1 and line.lower().find("if") == -1 and line.lower().find("same") == -1 and line.lower().find("keep") == -1 and line.lower().find("long") == -1 and line.lower().find("term") == -1 and line.lower().find("move") == -1 and line.lower().find("market") == -1 and line.lower().find("execution") == -1 and line.lower().find("update") == -1 and line.lower().find("lot") == -1 and line.lower().find("size") == -1 and line.lower().find("every") == -1 and line.lower().find("leave") == -1 and line.lower().find("news") == -1 and line.lower().find("minute") == -1:
        print(line)
