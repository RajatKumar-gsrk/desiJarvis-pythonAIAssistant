import os
import eel

from engine.features import *
from engine.command import *

eel.init("www")

soundAssistant()
eel.start('index.html', size=[1920, 1080])
