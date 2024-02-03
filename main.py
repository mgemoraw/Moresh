#!/usr/bin/python3
#What is main is main
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')
from kivy.app import App


from app import Moresh


Moresh().run()
