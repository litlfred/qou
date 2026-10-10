import urllib.request
import json
import os

req = urllib.request.Request("https://api.github.com/repos/litlfred/qou/pulls?state=open")
try:
    with urllib.request.urlopen(req) as response:
        prs = json.loads(response.read())
        for pr in prs:
            print(f"#{pr['number']}: {pr['title']} (Branch: {pr['head']['ref']})")
except Exception as e:
    print("Error:", e)
