# libraries needed
from libs_pack import *

# create Bard lib object
bard = Bard(token=TOKEN)

# init microphone and recognizer
r = sr.Recognizer()
m = sr.Microphone()


if __name__ == '__main__':
    say('Привет, я Юджин. Голосовой помощник с Искусственным Интелектом. Чем могу помочь?')

    while True:
        # our voice input
        input_ = recognize_user()
        # Here I mean if input is bye program breaks
        if input_ == 'пока':
            say(random.choice(['Пока', 'До скорых встреч', 'Удачи', 'Обращайтесь ещё!']))
            break
        if (input_ == ' ') or (input_ == ''):
            print('Не молчите! \n{"-"*60}')
            say('Не молчите! ')

        if ('найди в браузере' in input_) or ('найди в интернете' in input_):
            wb.open(f'https://www.google.com/search?q={input_.replace("найди в браузере", "").replace("найди в интернете", "")}')

        if input_.startswith('открой'):
            print(input_ + f'\n{"-"*60}')
            open_(' '.join(input_.split()[1:]))
        else:
            print(colored(f'User (you) - {input_}', "red"))
            print(f'{"-"*60}\n connecting Bard: \n {"-"*60}')
            # say bard's response
            response = bard.get_answer(input_)['content']
            print(colored(f'BardAi (assistant) - {response}\n{"-"*60}', 'green'))
            say(response.replace('*', '').replace('>', '').replace('°C', 'Градусов цельсия').replace('-', ' '))
