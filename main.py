import os
import eel
import asyncio

from engine.features import *
from engine.command import *

async def main():
    eel.init("www")

    soundAssistant()
    await eel.start('index.html', size=[1920, 1080])

if __name__ == '__main__':
    asyncio.run(main())
