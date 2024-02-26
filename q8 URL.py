from urllib.request import urlopen, URLError
url= input('Enter your URL: ')
def validation_url(url):
    try:
        urlopen(url)
        return True
    except URLError:
        return False