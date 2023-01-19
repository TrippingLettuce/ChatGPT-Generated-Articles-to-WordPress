import requests
import base64
import json

username = "klingercaleb11"
password = "sfLj5j9ry67sYLd"

creds = username + ':' + password
cred_token = base64.b64encode(creds.encode())

header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}

url = "https://testing9035.wordpress.com/wp/v2"

postID = "2"
post = {
 'title' : 'WordPress Python Integration: Updating Content',
 'content' : 'Hello, this content updated.'
}

blog = requests.post(url + '/' + postID , headers=header, json=post)
print(blog)