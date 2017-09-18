# Created by: Julie Nguyen
# Created on: Sept 2017
# Created for: ICS3U
# Daily Assignment - Unit0-05
# This program calculates the area and perimter of a rectangle with a length of 5 cm and a width of 3 cm

import ui

def answer_touch_up_inside(sender):
    # displays the answer for area and perimeter
    view['area_answer_label'].text = 'Area = ' + str(3*5) + ' cm^2'
    view['perimeter_answer_label'].text = 'Perimeter = ' + str(2*(5+3)) + ' cm'

view = ui.load_view()
view.present('full_screen')
