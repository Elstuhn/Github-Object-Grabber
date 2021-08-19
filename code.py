from github import Github
g = Github("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")

g = Github(base_url="https://elstuhn/api/v3", login_or_token="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")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
