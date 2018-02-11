from urllib.request import urlopen

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
def downloadIcon():
    #Ask for the app id
    appId = input("Enter app id: ")
    #Contact apple servers and retrieve the info document for the app
    data = urlopen(("https://itunes.apple.com/lookup?id="+appId)).read().decode('utf-8')

    #Trim text from the start the image url
    data = trim(data,'artworkUrl512":"',"forward")
    #Trim text from the end the image url
    data = trim(data,".jpg","backward")

    #Open the image file
    image = urlopen(data)
    #Save the image file
    output = open((appId+".jpg"),"wb")
    output.write(image.read())
    output.close()

    #Output a sucess message
    print("'"+appId+".jpg' saved\n")

while True:
    downloadIcon()
