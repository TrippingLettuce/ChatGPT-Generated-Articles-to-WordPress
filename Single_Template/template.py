import requests
import AIAPI
import imgAPI
import promtGen

# Initalizing, location, title to write article about
place = promtGen.pop() #Gets first location from top 1000 locations and deletes it
prompt = f"Generate a travel guild about {place}"
title_prompt = f"Generate a travel guild title for {place}"

#Each paragraph has one img 
#Par 1 (Talks about the actual travel guild)
img_prompt_1 = f"{place} trip"
article_block_content_1 = AIAPI.article_block_generate(prompt)
img1 = imgAPI.get_img(img_prompt_1)

#Par 2 (Talks about festivals and events)
img_prompt_2 = f"{place}"
prompt_1 = f"I have this travel article can you write an adtional section for the events/festivals at {prompt} 300 words. This is what I have so far{article_block_content_1}"
addtion_block_prompt_2 = AIAPI.article_block_generate(prompt_1)
img2 = imgAPI.get_img(img_prompt_2)

#Par 3 (Talks about location and food)
img_prompt_3 = f"{place} food"
prompt_2 = f"I have this travel article can you write an adtional section for the location and food at {prompt} 300 words. This is what I have so far{article_block_content_1}"
addtion_block_prompt_3 = AIAPI.article_block_generate(prompt_2)
img3 = imgAPI.get_img(img_prompt_3)

prompt_4 = f"Write a conclusion on why to travel to {place} as a travel article"
addtion_block_prompt_4 = AIAPI.article_block_generate(prompt_4)

#
article_block = f'<img src={img1} width="900" height="400" />{article_block_content_1}<img src={img2} width="900" height="400" />{addtion_block_prompt_2}<img src={img3} width="900" height="400" />{addtion_block_prompt_3}'
article_title = AIAPI.article_title_generate(title_prompt)



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
#'date'   : '2023-02-02T12:00:00' (Future Date)
#


#/posts for post, /page for new page, /posts/id for update and del post
r = requests.post(url= ROOT + '/wp-json/wp/v2/posts', data=data, headers=headers, auth=(user, password))
print(r)
#404 means https URL cant be found
#400-401 https URL cant connect (Username/Password) Error
#201 It worked :)
#200 Connected but nothing sent


