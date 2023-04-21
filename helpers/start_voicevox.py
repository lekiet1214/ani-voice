import subprocess
import json
import sys

config = json.load(open('config.json', 'r'))


def start_voicevox():
    try:
        print('Starting Voicevox engine')
        # Run the exe file and store the output in a variable
        result = subprocess.run(
            f'{config["voice_vox_path"]}/run.exe', capture_output=True)

        # Print the output of the exe file
        print(result.stdout.decode('utf-8'))
        print('Voicevox engine started')
    except Exception as e:
        raise type(e)(str(e))

sys.modules[__name__] = start_voicevox