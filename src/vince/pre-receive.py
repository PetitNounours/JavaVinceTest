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

# print key_issue

lastest_commit = subprocess.check_output(['git', 'log', '--pretty=oneline', 'origin/master..master'])
# git log --pretty=oneline origin/master..master

test = lastest_commit.split('\n', 1)
# print test

OK = []
KO = []
for commit in test:
    for key in key_issue:
        line = commit.split(" ", 1)
        print key
        if line[1] == key:
            print 'OK'
            OK.append(key)
        elif line[1] == "":
            print 'Message manquant'
            KO.append(key)
        else:
            print "le commit ", line[0], " ne contient pas de code d'erreur"
            KO.append(key)

if KO == []:
    sys.exit(0)
else:
    sys.exit(1)
