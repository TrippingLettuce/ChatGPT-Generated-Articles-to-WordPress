import requests
import AIAPI

place = "Tokyo"
prompt = f"Generate a travel article about {place}"
#Generate from block to get title
title_prompt = f"Generate a travel article title for {place}"

article_block_content = AIAPI.article_block_generate(prompt)
article_title = AIAPI.article_title_generate(title_prompt)

ROOT = 'https://lettuce.website'
user = 'StrongG'
password = 'M8du o5mb 7EiZ Rg0K y7Fu fRl3'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

#Generate a Header
data = {
    'title' : f'{article_title}',
    'content' : f'{article_block_content}',
    'status' : 'draft'
}

#Draft if wanted
#template if theme

r = requests.post(url= ROOT + '/wp-json/wp/v2/posts', data=data, headers=headers, auth=(user, password))
print(r)

