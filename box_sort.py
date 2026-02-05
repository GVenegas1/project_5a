#Author: Gabriel Venegas
#GitHub username: Gvenegas1
#Date: February 4, 2026
#Description: This code makes a Box class and a function to sort a list of
#boxes from the biggest to the smallest.

class Box:
    """A class that represents a box with dimensions."""

    def __init__(self, length, width, height):
        """Sets the starting dimensions using private variables."""

        self._length =length
        self._width = width
        self._height = height

    def volume(self):
        """Calculate the volume by multiplying L,W,and H."""

        #Using a variable here to make it easier to read
        box_volume = self._length * self._width * self._height
        return box_volume

    def get_length(self):
        """Returns the length of the box."""

        return self._length

    def get_width(self):
        """Returns the width of the box."""

        return self._width

    def get_height(self):
        """Returns the height of the box."""

        #Fixed this! It actually returns height now
        return self._height


def box_sort(box_list):
    """Sorts a list of boxes from greatest volume to least volume.
    It changes the list directly without making a new one."""

    #Start at the second box because the first one is "sorted"
    for current_index in range(1, len(box_list)):

        #this is the box trying to place
        box_to_sort = box_list[current_index]

        #Look at the box to the left
        previous_index = current_index - 1

        #current box is bigger than the one on its left
        while previous_index >= 0 and box_to_sort.volume() > box_list[previous_index].volume():

            #Shift the smaller box one spot to the right
            box_list[previous_index + 1] = box_list[previous_index]

            #Move the pointer left to check the next box
            previous_index = previous_index - 1

        #Put box into the empty hole created
        box_list[previous_index + 1] =box_to_sort
