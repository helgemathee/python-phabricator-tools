from phabricator import Phabricator

phab = Phabricator() # this uses the ~/.arcrc file

tasks = phab.maniphest.query(status = "status-open")

for phid in tasks:
    task = tasks[phid]
    print task['title']
