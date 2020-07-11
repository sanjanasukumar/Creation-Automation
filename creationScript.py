import sys
import os
from github import Github

foldername = str(sys.argv[1])
path = os.environ.get('mp')
token = os.environ.get('gt')
_dir = path + '/' + foldername

gh = Github(token)
user = gh.get_user()
login = user.login
repo = user.create_repo(foldername)

commands = [f'echo "# {repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

os.mkdir(_dir)
os.chdir(_dir)
for c in commands:
    os.system(c)
    print(f'{foldername} created locally')
    os.system('code .')
