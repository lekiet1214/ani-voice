import requests
import json
import sys

def synthesis(filename, data):
    try:   
        # load config file
        with open('config.json', 'r') as f:
            config = json.load(f)

        url = f'http://localhost:50021/synthesis?speaker={config["speaker"]}'

        # load json data
        with open(data, "r", encoding="utf-8") as f:
            json_data = json.load(f)

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
    except Exception as e:
        raise type(e)(str(e))
    
sys.modules[__name__] = synthesis