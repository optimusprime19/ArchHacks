from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from pprint import pprint
import requests

#SCOPES = 'https://www.googleapis.com/auth/drive.readonly'

#url = 'https://www.googleapis.com/fitness/v1/users/me/dataSources'
SCOPES = ['https://www.googleapis.com/auth/fitness.activity.read', 
		 'https://www.googleapis.com/auth/fitness.activity.write', 
		 'https://www.googleapis.com/auth/fitness.location.write',
		 'https://www.googleapis.com/auth/fitness.body.write']

resource = {
  "dataStreamName": "MyDataSource",
  "type": "derived",
  "application": {
    "detailsUrl": "http://example.com",
    "name": "Foo Example App",
    "version": "1"
  },
  "dataType": {
    "field": [
      {
        "name": "heartbeat",
        "format": "integer"
      }
    ],
    "name": "com.google.heartbeat.delta"
  },
  "device": {
    "manufacturer": "UF Health",
    "model": "ExampleTablet",
    "type": "tablet",
    "uid": "88888",
    "version": "1"
  }
}

		 
CLIENT_SECRET = 'client_secret.json'

store = file.Storage('storage.json')
credz = store.get()


if not credz or credz.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES, redirect_uri= "https://developers.google.com/oauthplayground")
    credz = tools.run_flow(flow, store)



SERVICE = build('fitness', 'v1', http = credz.authorize(Http()))

pprint(SERVICE.users().dataSources().list(userId='me').execute())




post_response = requests.post("https://www.googleapis.com/fitness/v1/users/me/dataSources", resource)

print (post_response)