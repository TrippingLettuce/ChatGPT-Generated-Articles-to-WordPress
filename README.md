# ChatGPT_Generated_Articles_to_WordPress
Currently set to generate articles with 3 images from prompt and 3 text blocks (200-500) words long.
Can be easly configured in template.py  
Taking prompts (Locations) in from loc.txt
Using OpenAI and Bing API.


## Example Website that uses this repo
![Example1111](https://user-images.githubusercontent.com/82426784/229942039-84726e31-52e0-49eb-b007-ccde7c607070.png)



## Installs
- python 
- `pip install openai`
- `pip install bing_image_urls`

## Set Up (Single Template)
For posting to a blog with no subcategories 

In template.py add wordpress API
```python
ROOT = 'https://website.com' #Your Website
user = 'Username' #Your Username
password = 'Password' #Application Password
#Password Section User>Profile>Add New Password Name
```

In AIAPI.py add OpenAI API
```python
openai.api_key = "sk-KEY" #OpenAI key
model_engine = "text-davinci-003" #model
```

## Set Up (Multiple Template) 
Blog with subcategories (Example Picture Above)


## Featured IMG
Word press REST API for python doesnt have the ability to post the IMG as a featured IMG.
All featured IMG plugins either have a pay wall or outdated the best way to fix this is FTP
Using the php script below and following the steps from gavickPro you can insert this fucntion in a wordPress theme.
https://www.gavick.com/blog/wordpress-automatically-set-post-featured-image
*It can possibly break your website use test site or child site to test*

```php
function wpsites_auto_set_featured_image() {
    global $post;
    if (!has_post_thumbnail($post->ID)) {
        $attached_image = get_children(array(
            'post_parent' => $post->ID,
            'post_type' => 'attachment',
            'post_mime_type' => 'image',
            'numberposts' => 1
        ));
        if ($attached_image) {
            foreach ($attached_image as $attachment_id => $attachment) {
                set_post_thumbnail($post->ID, $attachment_id);
                break;
            }
        }
    }
}
add_action('save_post', 'wpsites_auto_set_featured_image');
```

### Other Option 
This plug in works but needs to be updated to set featured img
https://wordpress.org/plugins/auto-featured-image-from-title/

## Block Error
Block Error Try this
```python
article_block = f'<p>{article_block_content_1}</p><figure class="wp-block-image"><img src="{img1}" alt=""/></figure><p>{addtion_block_prompt_2}</p><figure class="wp-block-image"><img src="{img2}" alt=""/></figure><p>{addtion_block_prompt_3}</p><figure class="wp-block-image"><img src="{img3}" alt=""/></figure><p>{addtion_block_prompt_4}</p>'
```
Source: https://wordpress.com/support/wordpress-editor/block-error-unexpected-or-invalid-content/

## Featrued IMG Still not working 

Add in functions.php
```php
add_theme_support( 'post-thumbnails');
```
Source: https://kinsta.com/blog/wordpress-featured-image-not-showing/#fixing-a-featured-image-problem-because-of-lazy-loading
