from PIL import Image

# RGB values for recoloring.
fuschia = (255,0,255)
green = (101,245,120)
orange = (243,141,64)
seafoam = (64,243,195)
pink = (250,152,221)
lightblue = (160,226,246)
red = (252,127,102)
darkblue = (143,147,243)
yellow = (240,243,143)
purple = (149,111,168)
rose = (210,106,179)




# Import image.
my_image = Image.open("pic4.jpeg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

print (image_list)
recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.

for pixel in image_list:
    intensity = pixel[0] + pixel[1] + pixel[2]
    if intensity <75:
        recolored.append(seafoam)
    elif intensity <150:
        recolored.append(orange)
    elif intensity <225:
        recolored.append(pink)
    elif intensity <300:
        recolored.append(fuschia)
    elif intensity <375:
        recolored.append(red)
    elif intensity <450:
        recolored.append(lightblue)
    elif intensity <525:
        recolored.append(yellow)
    elif intensity <600:
        recolored.append(rose)
    elif intensity <675:
        recolored.append(darkblue)
    elif intensity <750:
        recolored.append(green)
    elif intensity <765:
        recolored.append(purple)
print(recolored)


# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"

