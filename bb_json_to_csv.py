import pandas as pd
import requests
from requests.auth import HTTPBasicAuth

##Login
username = 'username'
password = 'password'
team = 'myteam'

full_repo_list = []

# Request 100 repositories per page (and only their slugs), and the next page URL
next_page_url = 'https://api.bitbucket.org/2.0/repositories/jwalton/git-scripts' % team

# Keep fetching pages while there's a page to fetch
while next_page_url is not None:
  response = requests.get(next_page_url, auth=HTTPBasicAuth(username, password))
  page_json = response.json()

  # Parse repositories from the JSON
  for repo in page_json['values']:
    reponame=repo['slug']
    repohttp=repo['links']['clone'][0]['href'].replace('SaravThangaraj@','')
    repogit=repo['links']['clone'][1]['href']

    print  (reponame+","+repohttp+","+repogit)
    full_repo_list.append(repo['slug'])
    

  # Get the next page URL, if present
  # It will include same query parameters, so no need to append them again
  next_page_url = page_json.get('next', None)

# Result length will be equal to `size` returned on any page

print ("Result:", len(full_repo_list))

df = pd.read_json (r'a.json')
df.to_csv (r'a.csv', index = None)
