import keyboard
import wave
import pyaudio
import os

def record_audio(filename):
    # start recording
    while True:
        if keyboard.is_pressed('ctrl+alt+shift+r'):
            print("Recording started")
            break

    # set up audio stream
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
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