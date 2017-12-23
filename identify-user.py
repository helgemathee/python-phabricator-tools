from phabricator import Phabricator

phab = Phabricator() # this uses the ~/.arcrc file
print phab.user.whoami()