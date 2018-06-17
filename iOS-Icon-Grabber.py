from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from sys import argv

#Trims data from the start and end of a string
def trim(data, search, direction):
    i = 0
    while i < len(data) - len(search):
        if data[i:i+len(search)] == search:
            if direction == "forward":
                return data[i+len(search):]
            else:
                return data[:i+len(search)]
        i += 1
    return data

#Function to download an app icon
def downloadIcon(appId, nameScheme):
    try:
    #Contact apple servers and retrieve the info document for the app
        data = urlopen(("https://itunes.apple.com/lookup?id="+appId)).read().decode('utf-8')

        #Trim text from the start the image url
        image_url = trim(data,'artworkUrl512":"',"forward")
        #Trim text from the end the image url
        image_url = trim(image_url,'.jpg',"backward")

        #Open the image file
        image = urlopen(image_url)
        
    except (HTTPError,URLError) as error:
        #If urlopen cannot get data from that URL, return an error
        print(error)
        return

    #Give the file the correct name
    #Use the app id for the filename (this is default)
    if nameScheme == "@appId":
        name = appId

    #Use the app name for the filename
    elif nameScheme == "@trackName":
        #Trim text from the start the image url
        name = trim(data,'trackName":"',"forward")
        #Trim text from the end the image url
        name = trim(name,'"',"backward")[:-1]
        
    #Otherwise, use the custom name passed in   
    else: 
        name = nameScheme
        
    #Save the image file
    output = open((name+".jpg"),"wb")
    output.write(image.read())
    output.close()

    #Output a sucess message
    print("'"+name+".jpg' saved\n")

def main():
    #Check if an app id has been passed in, if not return error
    try:
        appId = argv[1]
    except IndexError:
        print("Error: Need to pass in the app id as an argument")
        return

    #Check if a nameScheme has been passed in, if not use @appId
    try:
        nameScheme = argv[2]
        downloadIcon(appId,nameScheme)
    except:
        downloadIcon(appId,"@appId")

main()   
        
