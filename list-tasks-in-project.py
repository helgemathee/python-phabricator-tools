from phabricator import Phabricator

phab = Phabricator() # this uses the ~/.arcrc file

projects = phab.project.query()['data']
projectMap = {}
for phid in projects:
    projectMap[projects[phid]['name']] = phid

projectName = 'Infrastruktur'
projectPHID = projectMap[projectName]

tasks = phab.maniphest.query(projectPHIDs = [projectPHID])

print "====================================================================="
print "All tasks in project %s (%s)" % (projectName, projectPHID)
print "====================================================================="

for phid in tasks:
    task = tasks[phid]
    print "%s - %s" % (task['statusName'], task['title'])
