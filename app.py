import requests

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


api_key = ''
url = input('URL: ')
url_length = len(url)
video_id = url[17:28]

if url_length == 28:
    video = requests.get(
        f'https://www.googleapis.com/youtube/v3/videos?key={api_key}&fields=items(snippet(title,description,tags))&part=snippet&id={video_id}')
    allVideos = video.json()
    allVideosArray = allVideos["items"]
    title = allVideosArray[0]['snippet']['title']
    print(color.BOLD + color.BLUE + 'Title' + color.END)
    print(title)
    print('')
    print(color.BOLD + color.BLUE + 'Description' + color.END)
    description = allVideosArray[0]['snippet']['description']
    print(description)
    print('')
    print(color.BOLD + color.BLUE + 'Tags' + color.END)
    tags = allVideosArray[0]['snippet']['tags']
    print(tags)
else:
    print('Video not found')
