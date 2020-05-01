from src.lib.request import *
from src.search import *
import json
import sys

class Accounts(object):
    def __init__(self):
        super(Accounts, self).__init__()
        
    def account(self):
        base_url = "https://api.namefake.com/"
        contents = json.loads(request("GET", base_url).text)
        content = list(str(contents["username"] + " " + contents["email_u"]).split(" "))
        for x in range(int(len(content))):
            search(content[x])

