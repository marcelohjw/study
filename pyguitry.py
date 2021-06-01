# this Script will create a Progress Bar
# The Progress will be Manually Updated using the format listed below
# progress_bar.UpdateBar(Value of Bar, Maximum Bar Value)
# the Window uses a .Finalize Function to make the window Persistent

# Import the PySimpleGUI Library
import PySimpleGUI as sg
# Import the Time Library for use in this script
import time

# this is for the Layout Design of the Window
layout = [[sg.Text('PROGRESS BAR')],
          [sg.ProgressBar(1, orientation='h', size=(100, 100), key='progress')],
          ]
# This Creates the Physical Window
window = sg.Window('BAR STUDY', layout).Finalize()
progress_bar = window.FindElement('progress')

# This Updates the Window
# progress_bar.UpdateBar(Current Value to show, Maximum Value to show)
progress_bar.UpdateBar(0, 10)
# adding time.sleep(length in Seconds) has been used to Simulate adding your script in between Bar Updates
time.sleep(.50)

progress_bar.UpdateBar(1, 10)
time.sleep(.50)

progress_bar.UpdateBar(2, 10)
time.sleep(.50)

progress_bar.UpdateBar(3, 10)
time.sleep(.50)

progress_bar.UpdateBar(4, 10)
time.sleep(.50)

progress_bar.UpdateBar(5, 10)
time.sleep(.50)

progress_bar.UpdateBar(6, 10)
time.sleep(.50)

progress_bar.UpdateBar(7, 10)
time.sleep(.50)

progress_bar.UpdateBar(8, 10)
time.sleep(.50)

progress_bar.UpdateBar(9, 10)
time.sleep(.50)

progress_bar.UpdateBar(10, 10)
time.sleep(.50)