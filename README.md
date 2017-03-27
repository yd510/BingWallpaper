# BingWallpaper

Collecting the background image of cn.bing.com and set it as desktop wallpaper.

The code is compatible to ~~`3.6.1`~~ `3.5.3`.


## Requirements

* **PIL** The orignal [PIL](http://www.pythonware.com/products/pil/) doesn't suport python `3.x`. Use [Pillow](https://pypi.python.org/pypi/Pillow) instead.
* [**pywin32**](https://sourceforge.net/projects/pywin32/) provides `win32gui` and `win32con`.


## Others

1. [**pyinstaller**](http://www.pyinstaller.org/), [**py2exe**](http://www.py2exe.org/) and [**cx_Freeze**](https://anthony-tuininga.github.io/cx_Freeze/) could be used to create executable file from `.py`
2. p2exe only supports python `2.x`
3. cx_Freeze could support to python `3.6` but only could create runtime environments (or pack them into a `.msi`) instead of a single executuable file.
4. pyinstaller is a good thing. However, it only supports python `2.7` and `3.3`-`3.5`.

## Ref
* http://blog.csdn.net/u011584748/article/details/51377915
