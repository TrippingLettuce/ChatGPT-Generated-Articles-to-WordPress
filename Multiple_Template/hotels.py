import requests
import AIAPI
import imgAPI
import os
import random
import time

def remove_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if not lines:
        return None
    selected_line = random.choice(lines)
    lines.remove(selected_line)
    with open(file_path, 'w') as file:
        file.writelines(lines)
    return str(selected_line.strip())

def hotel_run():
    counter = 0

    # Initalizing, location, title to write article about
    place = remove_random_line('/home/lettuce/WorkCode/ChatGPTWordPRess/hotel.txt')
    print(place)

    #Links
    prompt = f"Generate a blog about hotel for {place}"
    title_prompt = f"Generate a blog title about hotels for {place}"

    time.sleep(2)
    img_prompt_1 = f"{place} hotel"
    article_block_content_1 = AIAPI.article_block_generate(prompt)
    img1 = imgAPI.get_img(img_prompt_1)

    time.sleep(2)
    img_prompt_2 = f"{place} tourist attractions"
    prompt_1 = f"I have this blog about hotels can you write an adtional section for {prompt} 300 words. This is what I have so far{article_block_content_1}"
    addtion_block_prompt_2 = AIAPI.article_block_generate(prompt_1)
    img2 = imgAPI.get_img(img_prompt_2)


    time.sleep(2)
    #Par 3 (Talks about location and food)
    img_prompt_3 = f"{place} beautiful"
    prompt_2 = f"I have this travel article about hotels can you write an adtional section for {prompt} 300 words. This is what I have so far{addtion_block_prompt_2}"
    addtion_block_prompt_3 = AIAPI.article_block_generate(prompt_2)
    img3 = imgAPI.get_img(img_prompt_3)

    time.sleep(2)
    prompt_4 = f"Write a conclusion on why to go to this hotel at {place} as a travel article"
    addtion_block_prompt_4 = AIAPI.article_block_generate(prompt_4)

    end_text = f"To search for flights: <a href=\"https://aviasales.tp.st/BpZVTmNB\">https://aviasales.tp.st/BpZVTmNB</a> \n\nTo search rent a car: <a href=\"https://discovercars.tp.st/zlth7VUe\">https://discovercars.tp.st/zlth7VUe</a> \n\nTo search for hotels: <a href=\"https://hotellook.tp.st/rTRN8i1V\">https://hotellook.tp.st/rTRN8i1V</a> \n\n To search for bike rental companies: <a href=\"https://bikesbooking.tp.st/MP1Prirj\">https://bikesbooking.tp.st/MP1Prirj</a> \n\n For insurance: <a href=\"https://ektatraveling.tp.st/UsFCGShY\">https://ektatraveling.tp.st/UsFCGShY</a> \n\nAdventures in cities: <a href=\"https://www.getyourguide.com/?partner_id=1IFTBRR&utm_medium=online_publisher&placement=%22other%22\">https://www.getyourguide.com/?partner_id=1IFTBRR&utm_medium=online_publisher&placement=%22other%22</a> \n\nThere are many benefits to using these services, whether you're booking a flight, hiring a car, or exploring new destinations. Here are just a few reasons why you should choose us:ň \n\nConvenience: Our platform makes it easy to find and book the travel options you need, all in one place. No more searching multiple websites or making multiple phone calls.\n\n\nExpert support: Our team of experts is available 24/7 to help you with any questions or concerns you may have. We're here to ensure you have a smooth and stress-free experience.\n\nCompetitive prices: We work with multiple suppliers to bring you the best prices on flights, car rentals, and more. You can be confident that you're getting a good deal when you book with us.\n\nWide selection: Whether you're looking for a budget-friendly option or a luxury experience, we have a range of options to choose from. You're sure to find the perfect travel solution for your needs.\n\nPeace of mind: We know that travel can be unpredictable, which is why we offer secure payment options and flexible booking policies. You can book with confidence knowing that you're in good hands."
    #<a href="https://www.getyourguide.com/?partner_id=1IFTBRR&utm_medium=online_publisher&placement=%22other%22">https://www.getyourguide.com/?partner_id=1IFTBRR&utm_medium=online_publisher&placement=%22other%22</a>
    article_block = f'<p>{article_block_content_1}</p><figure class="wp-block-image"><img src="{img1}" alt=""/></figure><p>{addtion_block_prompt_2}</p><figure class="wp-block-image"><img src="{img2}" alt=""/></figure><p>{addtion_block_prompt_3}</p><figure class="wp-block-image"><img src="{img3}" alt=""/></figure><p>{addtion_block_prompt_4}</p><p>{end_text}</p>'
    article_title = AIAPI.article_title_generate(title_prompt)

    counter =+ 1

    #date_in = date.date_out(counter)
    #print (date_in)

    ROOT = 'https://www.bestspents.com/'
    user = 'ijcqv'
    password = 'oYQc hvBT mPKr 3OaY WYAL 539R' #


    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    #Generate a Header
    #TRy to hhave it set to publish 5 min in future

    data = {
        'title' : f'{article_title}',
        'content' : f'{article_block}',
        'status' : 'publish'
        }
    #Draft if wanted
    #template if theme
    time.sleep(2)
    r = requests.post(url= ROOT + '/wp-json/wp/v2/hotel', data=data, headers=headers, auth=(user, password))
    print(r)