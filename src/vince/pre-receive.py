import requests
import json
import os
import subprocess
import sys


r = requests.get('https://testgit1.atlassian.net/rest/api/2/search?jql=project=TES', auth=('admin', 'Ld26091989'))
data = json.loads(r.text)

key_issue = []
for i in range(len(data['issues'])):
    key_issue.append(data['issues'][i]['key'])

print key_issue

lastest_commit = subprocess.check_output(['git','log','--pretty=oneline','origin/master..master'])
# git log --pretty=oneline origin/master..master

print lastest_commit
