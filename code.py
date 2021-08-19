from github import Github
import os
token = os.getenv('secret')
g = Github(token)

g = Github(base_url="https://elstuhn/api/v3", login_or_token=token)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
