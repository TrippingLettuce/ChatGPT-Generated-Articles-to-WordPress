import requests
import AIAPI
import imgAPI


place = "Place"
prompt = f"Generate a travel guild about {place}"
title_prompt = f"Generate a travel guild title for {place}"
img_prompt = f"{place} trip"


article_block_content = AIAPI.article_block_generate(prompt)
article_title = AIAPI.article_title_generate(title_prompt)
img = imgAPI.get_img(img_prompt)


ROOT = 'https://website.com'
user = 'Username'
password = 'Password' 
#Use Application Password for Password Section User>Profile>Add New Password Name

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {
    'title' : f'{article_title}',
    'content' : f'<img src={img} width="900" height="400" />{article_block_content}',
    'status' : 'draft' #or publish 
    }
#template if theme

#/posts for post, /page for new page, /posts/id for update and del post
r = requests.post(url= ROOT + '/wp-json/wp/v2/posts', data=data, headers=headers, auth=(user, password))
print(r)
#404 means https URL cant be found
#400-401 https URL cant connect (Username/Password) Error
#201 It worked :)
#200 Connected but nothing sent


