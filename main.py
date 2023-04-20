import os
import pyaudio
import wave
import keyboard
import speech_recognition as sr
from mtranslate import translate
import requests
import json
import soundfile as sf
import sounddevice as sd

audio_record = 'audio_record.wav'
audio_translated = 'audio_translated.wav'
text_translated = 'text_translated.txt'
text_not_translated = 'text_not_translated.txt'
chunk = 1024


def record_audio(filename=audio_record):
    # start recording
    while True:
        if keyboard.is_pressed('ctrl+alt+shift+r'):
            print("Recording started")
            break

    # set up audio stream
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    while True:
        if keyboard.is_pressed('ctrl+alt+shift+s'):
            print("Recording stopped")
            break

        data = stream.read(CHUNK)
        frames.append(data)

    # stop audio stream and save the audio file
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # delete the output file if it exists
    if os.path.exists(filename):
        os.remove(filename)

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print('File written!!')


def audio_to_text(input_filename=audio_record, output_filename=text_not_translated):
    # set up speech recognizer
    r = sr.Recognizer()

    # open audio file
    with sr.AudioFile(input_filename) as source:
        audio_data = r.record(source)

    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio_data, language='vi-VN')
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Text: {text}")
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            f"Could not request results from Speech Recognition service; {e}")
    print(f"Text saved to {output_filename}")


def translate_text(input=text_not_translated, filename=text_translated):
    # read text
    with open(input, 'r') as f:
        text = f.read()

    # translate text to Japanese
    translation = translate(text, 'ja')

    # write translated text to file
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(translation)

    print(f"Translated text saved to {filename}")
    print(f"Translated text: {translation}")


def audio_query(text, output_file=audio_translated):
    # send a POST request to the Voicevox API endpoint with the text to convert
    response = requests.post(
        'http://localhost:50021/audio_query', params={'text': text, 'speaker': 1})

    # check if the response was successful
    if response.status_code != 200:
        print(f"Error: Voicevox Desktop app returned status code {response.status_code}",
              f"with the following message: {response.text}")
        return

    # save the data to global json variable
    global json_data
    json_data = json.loads(response.text)

    # save json to file
    with open("audio_query.json", "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def synthesis(filename=audio_translated):
    url = 'http://localhost:50021/synthesis?speaker=1'

    params = json_data

    # send a POST request to the Voicevox API endpoint with the parameters
    response = requests.post(url, json=params)

    # check if the response was successful
    if response.status_code != 200:
        print(f"Error: Voicevox Desktop app returned status code {response.status_code}",
              f"with the following message: {response.text}")
        return

    # save data to wav file
    with open(filename, "wb") as f:
        f.write(response.content)


def text_to_voice():
    # read text
    with open(text_translated, 'r', encoding='utf-8') as f:
        text = f.read()

    # send a POST request to the Voicevox API endpoint with the text to convert
    audio_query(text)

    # send a POST request to the Voicevox API endpoint with the parameters
    synthesis()

    print("Voice saved to output.wav")


def play_audio(filename=audio_translated):
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Get the ID of the virtual audio device
    device_id = 11
    # for i in range(p.get_device_count()):
    #     info = p.get_device_info_by_index(i)
    #     print(info['name'])
    #     if 'CABLE' in info['name']:
    #         device_id = info['index']
    #         break

    #     if device_id is None:
    #         print("Virtual audio device not found.")
    #         exit()

    # Open the audio file
    data, fs = sf.read(filename, dtype='float32')

    # Get device info
    device_id = None
    device_info = sd.query_devices()
    for i in range(len(device_info)):
        # print(i, device_info[i])
        if 'CABLE Input' in device_info[i]['name']:
            print('Found name')
            if device_info[i]['max_input_channels'] == 0:
                print('Found max_input_channels')
                if device_info[i]['max_output_channels'] == 2:
                    print('Found max_output_channels')
                    if device_info[i]['default_samplerate'] == 44100:
                        print('Found default_samplerate')
                        device_id = device_info[i]['index']
                        print('device_id ', device_id)
                        break

    if device_id is None:
        print("Virtual audio device not found.")
        exit()
    
    # Play the audio file
    try:
        # device_id=15
        sd.play(data, fs, device=device_id)
        status = sd.wait()
    except KeyboardInterrupt:
        sd.stop()
        raise SystemExit('Interrupted by user')
    except Exception as e:
        raise type(e)(str(e))
    
    if status:
        raise RuntimeError('Error during playback: ' + str(status))

    
    

if __name__ == '__main__':
    record_audio()
    audio_to_text()
    translate_text()
    text_to_voice()
    play_audio()
