import record_audio
import audio_to_text
import translate_text
import text_to_voice
import play_audio
import json
import subprocess

audio_record = 'audio_record.wav'
audio_translated = 'audio_translated.wav'
text_translated = 'text_translated.txt'
text_not_translated = 'text_not_translated.txt'
audio_json = 'audio_query.json'
chunk = 1024

if __name__ == '__main__':

    # Start the voicevox engine
    with open('config.json', 'r') as f:
        config = json.load(f)
    try:
        # Run the exe file and store the output in a variable
        result = subprocess.run(f'{config["voice_vox_path"]}/run.exe', capture_output=True)

        # Print the output of the exe file
        print(result.stdout.decode('utf-8'))
        print('Voicevox engine started')
    except Exception as e:
        raise type(e)(str(e))

    record_audio.record_audio(audio_record)
    audio_to_text.audio_to_text(audio_record, text_not_translated)
    translate_text.translate_text(text_not_translated, text_translated)
    text_to_voice.text_to_voice(text_translated, audio_translated, audio_json)
    play_audio.play_audio(audio_translated)