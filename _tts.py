import torch
import sounddevice as sd
import time
from num2words import num2words

language = 'ru'
model_id = 'v4_ru'
sample_rate = 48000  # 48000
speaker = 'eugene'  # aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu')  # cpu или gpu

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)


def say(text: str):
    for i in text.split():
        if i.isdigit():
            text = text.replace(i, num2words(i, lang='ru'))


    try:
        audio = model.apply_tts(text=text,
                                speaker=speaker,
                                sample_rate=sample_rate,
                                put_accent=put_accent,
                                put_yo=put_yo,
                                )

        sd.play(audio, sample_rate * 1.05)
        time.sleep((len(audio) / sample_rate) + 0.5)
        sd.stop()
    except Exception:
        audio = model.apply_tts(text='Ошибка озвучки, читайте текст сами(',
                                speaker=speaker,
                                sample_rate=sample_rate,
                                put_accent=put_accent,
                                put_yo=put_yo,
                                )

        sd.play(audio, sample_rate * 1.05)
        time.sleep((len(audio) / sample_rate) + 0.5)
        sd.stop()

