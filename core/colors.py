import sys

colors = True # Output should be colored
machine = sys.platform # Detecting the os of current system
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False # Colors shouldn't be displayed in mac & windows
if not colors:
    end = red = white = green = yellow 
else:
    white = '\033[1;31;97m'
    green = '\033[1;31;92m'
    red = '\033[1;31;91m'
    yellow = '\033[1;31;93m'
    end = '\033[0m'
