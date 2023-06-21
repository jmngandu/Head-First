import requests,  json,turtle
#This first line just gets a reference to the turtle’s screen object.
screen = turtle.screen()
#We’re going to increase the size of the window to 1000 by 500 pixels, which matches the size of the image we’re about to add.
screen.setup(1000,500)
#This sets the entire window’s background to an image.
screen.bgpic('earth.gif')
#This resets the coordinate system of the turtle window; we talk about this on the next page
url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)
if (response.status_code == 200):
    response_dictionary = json.loads(response.text)
    position = response_dictionary['iss_position']
    print('International Space Station at ' +
        position['latitude'] + ', ' + position['longitude'])
else:
    print("Houston, we have a problem:", response.status_code)
turtle.mainloop()
