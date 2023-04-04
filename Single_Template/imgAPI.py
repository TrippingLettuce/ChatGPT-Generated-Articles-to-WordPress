from bing_image_urls import bing_image_urls


def get_img(prompt:str)->str:
    url = bing_image_urls(f"{prompt}", limit=1)[0]
    print(url)
    return url
