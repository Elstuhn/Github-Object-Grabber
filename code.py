from github import Github
import github
from github import NamedUser, PaginatedList, Organization
import os
import typing as t
import time
from collections import defaultdict
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
    print(f"Hireable: {self.user.hireable}")
    print(f"Organisations: {' | '.join([i.name for i in self.user.get_orgs()])}")
    print("\nLanguage Usages:")
    commit = 0
    languages = defaultdict(int)
    langsum = 0
    for repos in self.user.get_repos():
      for commits in repos.get_commits(author=self.user):
        commit += 1
      repolang = repos.get_languages()
      for language in repolang:
        languages[language] += repolang[language]
        langsum += repolang[language]
    for language in languages:
      print(f"{language}: {round((languages[language]/langsum)*100, 1)}%")
    print(f"{commit} commits")




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

  def getfollowers(self) -> PaginatedList:
    return self.user.get_followers()

  def getfollowing(self) -> PaginatedList:
    return self.user.get_following()

  def displayfollowers(self):
    for followers in self.user.get_followers():
      print(followers)

  def displayfollowing(self):
    for following in self.user.get_following():
      print(following)

  def getorgs(self):
    print(f"{self.user.name}'s Organizations Info")
    members = 0
    for orgs in self.user.get_orgs():
      for i in orgs.get_members():
        members += 1
      print(f"Org. Name: {orgs.name}\nID: {orgs.id}\n{orgs.description}\nCreation: {orgs.created_at}\nOwns {orgs.public_repos} public repositories\nTotal Members: {members}")
      print("\n")

  def returnorg(self) -> list:
    return [Org(org) for org in self.user.get_orgs]


class Org:
  def __init__(self, org : Organization):
    self.org = org 

  def showinfo(self):
    org = self.org
    members = projects = 0
    for i in org.get_members():
      members += 1
    for i in org.get_projects():
      projects += 1
    languages = defaultdict(int)
    langsum = 0
    for repos in self.user.get_repos():
      repolang = repos.get_languages()
      for language in repolang:
        languages[language] += repolang[language]
        langsum += repolang[language]
    print(f"Org. Name: {org.name}\nID: {org.id}\n{org.description}\nCreation: {org.created_at}\nOwns {org.public_repos} public repositories\nTotal Members: {members}\nTotal Projects: {projects}")
    print("\nLanguage Usage:")
    for language in languages:
      print(f"{language}: {round((languages[language]/langsum)*100, 1)}%")

  def listmembers(self):
    print("Name | Login")
    time.sleep(1)
    for person in self.org.get_members():
      print(f"{person.name} | {person.login}")
      time.sleep(0.3)

  def displayrepos(self):
    for repo in self.org.get_repos(type='all'):
      print(f"{repo.name}\n{repo.description}")
      time.sleep(0.5)

  def getmembers(self) -> PaginatedList:
    return self.org.get_members()


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

  def getorg(self, name):
    members = 0
    print(f"{self.user.name}'s Organizations Info")
    for orgs in self.user.get_orgs():
      for i in orgs.get_members():
        members+=1
      print(f"Org. Name: {orgs.name}\nID: {orgs.id}\n{orgs.description}\nCreation: {orgs.created_at}\nOwns {orgs.public_repos} public repositories\nTotal Members: {members}")
      print("\n")

  def convertorg(self, org : Organization) -> Org:
    return Org(org)
