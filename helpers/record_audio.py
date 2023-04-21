import keyboard
import wave
import pyaudio
import os
import json
import sys

config  = json.load(open('config.json', 'r'))
start_key = config['start_key']
stop_key = config['stop_key']

def record_audio(filename):
    
    try:
        print(f"Press the start key to start recording. {start_key}")
        # start recording
        while True:
            if keyboard.is_pressed(start_key):
                print("Recording started")
                print(f"Press the stop key to stop recording. {stop_key}")
                break

        # set up audio stream
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100

        audio = pyaudio.PyAudio()

        # channels config seems to be undertermined, try all channels until one is accepted
        for i in range(1, 4): # channels would ussually be 1 or 2
            try:
                stream = audio.open(format=FORMAT, channels=i,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
                # if no error, set channels to i and break
                CHANNELS = i
                break
            except OSError:
                pass
        
        frames = []
        while True:
            if keyboard.is_pressed(stop_key):
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
    except Exception as e:
        raise type(e)(str(e))
    
sys.modules[__name__] = record_audio    