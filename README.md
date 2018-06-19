# iOS-Icon-Grabber
A basic Python 3 script to download an app icon from the iOS App Store as a 512x512 jpeg image.

## Executing the script
Execute from command line using the following arguments:
```
python iOS-Icon-Grabber.py [options]
```

## Finding the app id
Visit the [iOS App Store](https://itunes.apple.com/gb/genre/ios/id36?mt=8) and find the app you want the icon for. The URL should resemble the following:
```
https://itunes.apple.com/gb/app/<APPNAME>/id<APPID>?mt=8
```

## Options
#### -A, --app_id [app id]
Specifies the app id for the app icon you want e.g. [962194608](https://itunes.apple.com/gb/app/google-photos/id962194608?mt=8).

#### -F, --file_name [file name]
It supports the following file names:
* **(app_id)** - which uses the app id as the file name (default).
* **(app_name)** - which uses the app name as the file name.
* Otherwise it will use whatever you pass in.

## Example usage
An example of using the script to download the icon for Google Photos and using the app name as the file name:
```
python iOS-Icon-Grabber.py -A 962194608 -F (app_name)
```

Enjoy!