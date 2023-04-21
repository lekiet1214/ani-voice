from helpers import translate_text, text_to_voice, play_audio, record_audio, audio_to_text, start_voicevox
import json, os, threading

config = json.load(open('config.json', 'r'))

audio_record = os.path.abspath(config['audio_record'])
audio_translated = os.path.abspath(config['audio_translated'])
text_translated = os.path.abspath(config['text_translated'])
text_not_translated = os.path.abspath(config['text_not_translated'])
audio_json = os.path.abspath(config['audio_json'])


def main():
    try:
        while True:
            record_audio(audio_record)
            audio_to_text(audio_record, text_not_translated)
            translate_text(text_not_translated, text_translated)
            text_to_voice(text_translated, audio_translated, audio_json)
            play_audio(audio_translated)
            print('Done\nWaiting for input...')
    except Exception as e:
        raise type(e)(str(e))


if __name__ == '__main__':
    threading.Thread(target=start_voicevox).start()
    threading.Thread(target=main).start()