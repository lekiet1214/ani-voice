import speech_recognition as sr
import sys

def audio_to_text(input_filename, output_filename):

    try:
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
            raise sr.UnknownValueError
        except sr.RequestError as e:
            print(
                f"Could not request results from Speech Recognition service; {e}")
        print(f"Text saved to {output_filename}")
    except Exception as e:
        raise type(e)(str(e))
    
sys.modules[__name__] = audio_to_text    