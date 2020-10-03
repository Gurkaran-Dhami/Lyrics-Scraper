import random
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def return_song_list() -> list:
    """
    Returns all the lyrics of a song as a list, where each item is 
    a line from the song as displayed on the lyrics.com website
    """
    my_url = 'https://www.lyrics.com/lyric/36366328/Jaden/Summertime+in+Paris'
    #open the connection and grab the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    #html parsing
    page_soup = soup(page_html, 'html.parser')

    #lyrics are contained in the pre tag, this grabs all the text
    raw_lyrics = page_soup.body.pre.text
    obj1 = raw_lyrics.split('\n')     #problem with \r showing up
    cleaned_lyrics = []
    for vals in obj1: 
        if vals != '':
            cleaned_lyrics.append(vals)
    return cleaned_lyrics 

def choose_random_line() -> str:
    """
    from the output of def return_song_list() it chooses a random line that
    client can decide to be the caption of the post or not
    """
    lst = return_song_list()
    random_num = random.randint(0, len(lst))
    return lst[random_num]

