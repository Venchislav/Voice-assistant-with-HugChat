import os

programs = {'chrome': 'C:\Program Files\Google\Chrome\Application\chrome.exe',
            'пайчарм': 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2023.1.2.lnk',
            'telegram': r'C:\Users\rayga\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\telegram.lnk',
            'steam': r'C:\Users\rayga\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Steam.lnk',
            'проводник': ''}


def open_(program):
    os.startfile(programs[program])
