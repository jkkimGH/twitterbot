import json
from urllib.request import urlopen
import serpAPI
import wget
# import requests
# import shutil

def download_img(image_url):
    PATH = "" # <-- Downloading the image for the word to here
    image_filename = wget.download(image_url, out=PATH)

    print('Image Successfully Downloaded: ', image_filename)

    return image_filename

    # requests and shutil version

    # filename = img_url.split("/")[-1]

    # filename = filename[:-3] + filename[-3:].lower()
    # print(filename)

    # r = requests.get(img_url, stream = True)

    # if r.status_code == 200:
    #     r.raw.decode_content = True

    #     with open("twitterbot_images/" + filename,'wb') as f:
    #         shutil.copyfileobj(r.raw, f)

    #     print('Image sucessfully Downloaded: ',filename)
    #     return filename
    # else:
    #     print('Image Couldn\'t be retreived')
    #     exit()


def get_tweet_components():
    url = 'https://random-words-api.vercel.app/word'
    page = urlopen(url)
    html_bytes = page.read()
    wordAPI = html_bytes.decode("utf-8")
    data_dict = json.loads(wordAPI)

    word = data_dict[0]['word']
    text = "Today's word: " + data_dict[0]['word'] + "\nDefinition: " + data_dict[0]['definition'] + "\nPronunciation: " + data_dict[0]['pronunciation']
    
    image = serpAPI.getImage(word)[0]['original']
    img_file = download_img(image)

    returnList = [text, img_file]

    return returnList


if __name__ == "__main__":
    print(get_tweet_components())
