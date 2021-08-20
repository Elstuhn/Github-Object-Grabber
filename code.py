from github import Github
import github
from github import NamedUser
from github import PaginatedList
import os
import typing as t
g = Github()
class User: #user has to be github object
  def __init__(self, user : NamedUser):
    self.user = user

  def getinfo(self):
    print("User Stats:")
    print(f"Name: {self.user.name}\nLocation: {self.user.location}\nAbout: {self.user.bio}")
    print(f"Following {self.user.following} users")
    print(f"Being followed by {self.user.followers} users")
    print(f"Public Repos: {self.user.public_repos}")
    print(f"Contributions: {self.user.contributions}")

  def getrepos(self) -> PaginatedList:
    repos = self.user.get_repos()
    return repos

  def listrepos(self):
    for repo in self.getrepos():
      print(repo.full_name)

  def getrepoinfo(self, reponame : str):
    repo = g.get_repo(f"{self.user.login}/{reponame}")
    print(f"Repository Owner: {repo.owner.login}")
    print(f"Repository Name: {repo.name}\n{repo.description}")
    print(f"Date of Creation: {repo.created_at}")
    print(f"{repo.stargazers_count} users starred this repository, {repo.subscribers_count} users has subscribed to this repository and {repo.watchers_count} users are watching this repository")
    print(f"Repository Language: {repo.language}")
    print(f"Size: {repo.size}KB")
    print(f"Last Update: {repo.updated_at}")
    print("\nLicense:")
    license = repo.get_license().license
    print(f"{license.name}\n{license.description}")
    print(f"Permissions: {' | '.join(license.permissions)}")
    print(f"Conditions: {' | '.join(license.conditions)}\nLimitations: {' | '.join(license.limitations)}")

    

class SGO:

  def returnuser(self, username): #username of github user
    user = g.get_user(username)
    user = User(user)
    return user
from github import Github
import github
from github import NamedUser
from github import PaginatedList
import os
import typing as t
g = Github()
class User: #user has to be github object
  def __init__(self, user : NamedUser):
    self.user = user

  def getinfo(self):
    print("User Stats:")
    print(f"Name: {self.user.name}\nUser ID: {self.user.id}\nEmail: {self.user.email}\nLocation: {self.user.location}\nAbout: {self.user.bio}\nCompany: {self.user.company}")
    print(f"Following {self.user.following} users")
    print(f"Being followed by {self.user.followers} users")
    print(f"Public Repos: {self.user.public_repos}")
    print(f"Contributions: {self.user.contributions}\nHireable: {self.user.hireable}")

  def getrepos(self) -> PaginatedList:
    repos = self.user.get_repos()
    return repos

  def listrepos(self):
    for repo in self.getrepos():
      print(repo.full_name)

  def getrepoinfo(self, reponame : str):
    repo = g.get_repo(f"{self.user.login}/{reponame}")
    print(f"Repository Owner: {repo.owner.login}")
    print(f"Repository Name: {repo.name}\n{repo.description}")
    print(f"Date of Creation: {repo.created_at}")
    print(f"{repo.stargazers_count} users starred this repository, {repo.subscribers_count} users has subscribed to this repository and {repo.watchers_count} users are watching this repository")
    print(f"Repository Language(s): {' | '.join(repo.get_languages())}")
    print(f"Size: {repo.size}KB")
    print(f"Last Update: {repo.updated_at}")
    try:
      license = repo.get_license().license
      print("\nLicense:")
      print(f"{license.name}\n{license.description}")
      print(f"Permissions: {' | '.join(license.permissions)}")
      print(f"Conditions: {' | '.join(license.conditions)}\nLimitations: {' | '.join(license.limitations)}")
    except:
      pass
    return repo

  def getfollowers(self):
    return self.user.get_followers()

  def getfollowing(self):
    return self.user.get_following()

  def displayfollowers(self):
    for followers in self.user.get_followers():
      print(followers)

  def displayfollowing(self):
    for following in self.user.get_following():
      print(following)


    

class SGO:

  def returnuser(self, username): #username of github user
    user = g.get_user(username)
    user = User(user)
    return user

  def getrepo(self, user, reponame): #user has to be login name
    repo = g.get_repo(f"{user}/{reponame}")
    print(f"Repository Owner: {repo.owner.login}")
    print(f"Repository Name: {repo.name}\n{repo.description}")
    print(f"Date of Creation: {repo.created_at}")
    print(f"{repo.stargazers_count} users starred this repository, {repo.subscribers_count} users has subscribed to this repository and {repo.watchers_count} users are watching this repository")
    print(f"Repository Language(s): {' | '.join(repo.get_languages())}")
    print(f"Size: {repo.size}KB")
    print(f"Last Update: {repo.updated_at}")
    try:
      license = repo.get_license().license
      print("\nLicense:")
      print(f"{license.name}\n{license.description}")
      print(f"Permissions: {' | '.join(license.permissions)}")
      print(f"Conditions: {' | '.join(license.conditions)}\nLimitations: {' | '.join(license.limitations)}")
    except:
      pass
