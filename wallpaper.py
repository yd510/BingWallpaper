
import re
import urllib.request
import os
import time
from PIL import Image
import win32gui
import win32con


def get_jpg_url():
    print('Parsing html...')
    html = urllib.request.urlopen('http://cn.bing.com/').read().decode('utf-8')
    jpg_url = re.findall(r'([\w\/_-]+?.jpg)',html)[0]
    print(jpg_url)
    jpg_name = re.search(r'[\w_-]+?.jpg',jpg_url).group(0)
    print(jpg_name)
    return (jpg_url,jpg_name)


def get_jpg_file(jpg_url):
    jpg_url = 'http://cn.bing.com' + jpg_url
    print('Downloading %s' % jpg_url)
    urllib.request.urlretrieve(jpg_url,jpg_name)
    print('Done!')


def set_wallpaper(jpg_name):
    bmp_name = jpg_name[0:len(jpg_name)-3]+"bmp"
    print('Converting %s to %s' % (jpg_name,bmp_name))
    img = Image.open(jpg_name)
    img.save(bmp_name)
    print('Done!')
    print('Setting wallpaper...')
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,bmp_name,0)
    print('Done!')


if __name__ == '__main__':
    while(True):
        print('In while loop...')
        jpg_url,jpg_name=get_jpg_url()
        if os.path.exists(jpg_name):
            print('Sleep for 12 hours!')
            time.sleep(60*60*12)
            continue
        get_jpg_file(jpg_url)
        set_wallpaper(jpg_name)
