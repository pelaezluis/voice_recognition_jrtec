def read_audio(audio_in):
    with open(audio_in, 'rb') as f:
        print(audio_in)
        audio = f.read()
    return audio