import requests
import re

def decode_message(url):

    response = requests.get(url)
    url_from_response = response.text

    #checks for specific patterns like A23 or even #34 inside the downloded fi0le using regex
    patterns = re.findall(r"([^\s\d])(\d)(\d)",url_from_response)


    data_for_grid = []
    initial_max_for_x = 0
    initial_max_for_y = 0

    #creates a list of data for the grid and finds the maximum coordinates or values of x and y
    for pattern in patterns:
      origin = pattern[0]
      character_in_x_coordinates = pattern[1]
      character_in_y_coordinates = pattern[2]
      x_coordinates = int(character_in_x_coordinates)
      y_coordinates = int(character_in_y_coordinates)

      data_for_grid.append((origin, x_coordinates, y_coordinates))

      if x_coordinates > initial_max_for_x:
        initial_max_for_x = x_coordinates
      if y_coordinates > initial_max_for_y:
            initial_max_for_y = y_coordinates

    #creates an empty grid to place the data from the data list created above
    the_actual_grid = []
    for i in range(initial_max_for_y+1):
        row = []
        for j in range(initial_max_for_x+1):
            row.append(' ')
        the_actual_grid.append(row)

    #each character from the data list is placed in it's grid position according to their patterns
    for character in data_for_grid:
      origin = character[0]
      x_coordinates = character[1]
      y_coordinates = character[2]
      the_actual_grid[y_coordinates][x_coordinates] = origin

    #finally the rows which are the x coordinates are combined together to form lines of the decoded msg
    decode_msg = ""
    for row in the_actual_grid:
        msg = ""
        for character in row:
            msg += character
        decode_msg += msg + "\n"

    return decode_msg

#asks the user for the URL instead of hardcoding it when we want to cahnge the URL to make the program flexible and reusable in the future
url = input("Enter or copy and paste the URL: ")
print("decoded message:")
x= decode_message(url)
print(x)
def clean_message(decoded_msg):
    capital_letters = ""
    for char in decoded_msg:
        if char.isalpha():
          if char == char.upper():
            capital_letters += char +"\n"
    return capital_letters
print(clean_message(x))

