# ChatGPT_Generated_Articles_to_WordPress
Using OpenAI and Bing API.
Currently set to generate 1000 travel articles that include, 3 images and 3 text blocks.
Can be forked or configured to do more or less.


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
