# Requirements
## Python 3.6
This application was developed in Python 3.6.
An easy way to install Python is to with Homebrew. Go to https://brew.sh/ to install it.

Once it's installed, (and assuming you installed XCode), run this command to get python 3:

brew install python

You can look at this website to install it.
http://docs.python-guide.org/en/latest/starting/install3/osx/

## Virtual Environment
You should use a virtual environment so developing this project doesn't affect your other projects.

Open a terminal, go to the base directory and run venv. Pass in the new directory that will have all of the environment information:

python3 -m venv environment_directory

Now activate the environment by running bin/activate:
cd environment_directory
. bin/activate
cd ..

The terminal should have a "(environment_directory)" prefix to indicate you activated it.

### Do not use virtualenv
pygame and virtualenv do not get along, especially when you use the keyboard. If you can't type into your apps while running virtualenv, this is the most likely culprit.

More information and a workaround can be found here:
https://www.pygame.org/wiki/GettingStarted#virtualenv%20issue

## pip
pip is a Python package installer that is installed when you set up your virtual environment.

I've included a requirements.txt file that pip can use to download most of the requirements.

pip install -r requirements-mac.txt

## kivy
Kivy is a UI wrapper that can be used to build and edit your in-game GUI.

https://kivy.org/docs/guide/basic.html

On the Mac, there are 2 ways to install kivy.
### Use the Kivy App
https://kivy.org/docs/installation/installation-osx.html#installation-osx

You can download the package to create a launcher. All of the required files are in this package.

### Pure command line
If you don't want to use an app and want to keep everything on the terminal, you can use Homebrew and pip to install the prerequires.

I followed the instructions in this gist
https://gist.github.com/garyjohnson/53c1eef4adaf57c247a4

#!/bin/bash
brew install sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer
pip3 install --upgrade Cython==0.25.2
# USE_OSX_FRAMEWORKS=0 pip3 install kivy # currently doesn't work due to incompatibility with SDL_mixer: https://github.com/kivy/kivy/pull/5459
USE_OSX_FRAMEWORKS=0 pip3 install http://github.com/kivy/kivy/archive/master.zip

## pygame
Pygame is a Python binding for SDL that handles most of the in game functions you would ever want to help produce games.

It should have been installed with kivy or with the pip update, but just in case:

pip install pygame
