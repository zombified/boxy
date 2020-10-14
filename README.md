# BOXY

A very simple MacOS app that puts an icon in the menu bar and lets you start
a timer for 60, 25, or 5 minutes.

At the end of the time, an alert box is shown.


# Building the App

```
$ python3.8 -m venv ./env
$ ./env/bin/pip install rumps py2app
$ ./env/bin/python setup.py py2app
$ open -a dist/Boxy.app
```
