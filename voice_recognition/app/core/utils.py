import os

def read_audio(audio_in: str):
    with open(audio_in, 'rb') as f:
        print(audio_in)
        audio = f.read()
    return audio

def delete_audio(audio_in: str):
    os.remove(audio_in)


def validate_format(ext: str):
    formats = ['wav', 'opus', 'webm']
    if ext in formats:
        return True
    else:
        return False