# pip3 install httplib2 --upgrade
# pip install beautifulsoup4

import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd

from io import StringIO
import urllib.request
from PIL import Image


# 
# search stroke order gif
#

def get_stroke_order_gif_url(search_character):
    template_url = "https://commons.wikimedia.org/wiki/File:%s-order.gif"
    template_img_alt_tag = "File:%s-order.gif"
    url = template_url % search_character
    img_alt_tag_text = template_img_alt_tag % search_character

    # class main
    http = httplib2.Http()

    status, response = http.request(url)
    soup = BeautifulSoup(response)

    source_url = None
    images = soup.find_all("img")
    for img in images:
        alt_tag = img.get('alt')
        if alt_tag == img_alt_tag_text:
            source_url = img.get('src')
    
    # returns None if not found
    return source_url

def download_gif(gif_url, outfile):
    try:
        urllib.request.urlretrieve(gif_url, outfile)
    except IOError as e:
        return False
    print("sucsess downloading gif")
    return True

def download_character_gif(search_character):
    
    output_file_template = "stroke_order_gifs/%s_stoke_order.gif"
    output_file = output_file_template % search_character

    stroke_order_gif_url = get_stroke_order_gif_url(search_character)
    success = download_gif(stroke_order_gif_url, output_file)
    
    if success:
        print("success downloading %s stroke order gif" % search_character)
    else:
        print("failure to download %s stroke order gif" % search_character)
    return success


#
# example
#

search_character = "是"
download_character_gif(search_character)
