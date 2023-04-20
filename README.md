# ani-voice

## About

ani-voice is a software to turn your ugly voice into a cute anime girl voice.
And also translate your voice into Japanese.

## Installing and Running

### Requirements

- Windows 11 or later

- Python 11.0 or later. Get it from [here](https://www.python.org/downloads/)

- VB-CABLE Virtual Audio Device. Get it from [here](https://vb-audio.com/Cable/)

- VOICEVOX engine. Get it from [here](https://github.com/VOICEVOX/voicevox_engine/releases/tag/0.14.4)

Note that this software is not tested on other platforms.

### Installing

1. Clone this repository

2. Install dependencies

```bash
pip install -r requirements.txt
```

### Usage

By default, this software will use the first audio device as input and the VB-CABLE device as output.

First, run the VOICEVOX engine.

Then, run the software.

```bash
python main.py
```

### Configuration

You can change the speaker by changing the configuration file.
Refer to the [speaker file](speakers.json) for more information.

```json
{
    "speaker": "speaker_id"
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



