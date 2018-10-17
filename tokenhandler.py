import requests
import json

def create(username, password, cid, csecret):
	payload = {
				"client_secret" : csecret,
				"scopes": ["admin:org", "admin:org_hook", "admin:public_key", "admin:repo_hook", "repo", "user"],
				"note": "codex-github"
				}
	AUTH_URL = f'https://api.github.com/authorizations/clients/{cid}'
	response = requests.put(AUTH_URL, data=json.dumps(payload), auth=(username, password))
	if response.status_code == 200:
		print("Using existing token")
	if response.status_code == 201:
		print("Created new token")
	if response.status_code == 401:
		print("Bad credentials")
		return None
	
	return response.json()

def delete(username, password, url):
	response = requests.delete(url, auth=(username, password))
	return (response.status_code == 204)
