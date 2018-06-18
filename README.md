# iOS-Icon-Grabber

A basic Python3 script to download an app icon from the Apple App Store as a 512x512 jpg image.

To get the app id for an app, visit the itunes website on a computer and find the app you want the icon for. The URL should resemble the following:
```
https://itunes.apple.com/us/app/<APPNAME>/id<APPID>?mt=8
```

Execute the script from the command line using the following arguments:
```
python iOS-Icon-Grabber.py -app_id <yourappid> [-file_name <yourfilename>]
```

There are currently 3 possible file name schemes:
1. '{app_id}' which uses the app id as the filename (this is default if you do not specify).
2. '{app_name}' which uses the app name as the filename.
2. 'your custom name here' which uses what ever you pass in as the file name (be careful because if you download multiple icons, the old one will be overwritten).

Here is an example of using the script to download the icon for Google Photos and using the apps name as the filename:
```
python iOS-Icon-Grabber.py -app_id 962194608 -file_name {app_name}
```

Enjoy!
