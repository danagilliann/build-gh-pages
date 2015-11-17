'''
builds your gh-pages branch from pulling master
'''
import os


# branch = str(input("Enter the branch to build from")) 
# ^ An alternative if you're building from a branch other than master
branch = "master"

os.system("git checkout gh-pages")
os.system("git pull origin " + branch) 
os.system("git push origin gh-pages")
os.system("git checkout " + branch)
