'''
builds your gh-pages branch from pulling master
'''
import os


remote = str(raw_input("Enter the remote to build from "))
branch = str(raw_input("Enter the branch to build from "))
# ^ An alternative if you're building from a branch other than master
# branch = "master"

os.system("git checkout gh-pages")
os.system("git pull " + remote + " " + branch)
os.system("git push " + remote + " gh-pages")
os.system("git checkout " + branch)
