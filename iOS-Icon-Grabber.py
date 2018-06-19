import urllib.request
import urllib.error
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
def downloadIcon(app_id, file_name):
    if app_id == "":
        print("You have not entered an app id?")
        return
    try:

        #Connect to itunes and retrieve the info document for the app
        data = urllib.request.urlopen(("https://itunes.apple.com/lookup?id="+app_id)).read().decode('utf-8')

        #Trim text from the start the image url
        image_url = trim(data,'artworkUrl512":"',"forward")
        #Trim text from the end the image url
        image_url = trim(image_url,'.jpg',"backward")
        
        #Open the image file
        image = urllib.request.urlopen(image_url)

    #If urlopen cannot get data from that URL, return an error
    except (urllib.error.HTTPError,urllib.error.URLError) as error:
        print("Invalid app id?")
        return

    #Give the output file a name
    #Use the app id for the file name (this is default)
    if file_name == "(app_id)" or file_name == "":
        file_name = app_id

    #Use the app name for the filename
    elif file_name == "(app_name)":
        #Trim text from the start the image url
        file_name = trim(data,'trackName":"',"forward")
        #Trim text from the end the image url
        file_name = trim(file_name,'"',"backward")[:-1]
        
    #Otherwise, use the custom name passed in

    #Save the image file
    output = open((file_name+".jpg"),"wb")
    output.write(image.read())
    output.close()

    #Output a sucess message
    print("'"+file_name+".jpg' saved")

def main():
    app_id = ""
    file_name = ""

    #Loop through all command line arguments apart from the file name
    pos = 1
    while pos < len(argv):
        if argv[pos] == "--app_id" or argv[pos] == "-A":
            if not pos == len(argv) - 1:
                app_id = argv[pos+1]
                pos += 1
                
        elif argv[pos] == "--file_name" or argv[pos] == "-F":
            if not pos == len(argv) - 1:
                file_name = argv[pos+1]
                pos += 1
            else:
                print("You haven't specified the file name")
        
        #Handles unknown arguments
        else:
            print("Unrecognised argument: " + argv[pos])
            
        pos += 1
    
    downloadIcon(app_id,file_name)

main()   
        
