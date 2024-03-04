# Mute NOS Advert with Pedro Mafama Song

This script allows muting the NOS advert using Pedro Mafama's song when it's detected. It compares the audio input from the microphone with a pre-loaded annoying music sample. When similarity exceeds a defined threshold, it sends a socket request to mute the TV.

## Prerequisites
- Python 3.x
- Required libraries: `pyaudio`, `socket`, `librosa`, `numpy`, `scipy`

## Setup
1. Ensure Python and the required libraries are installed.
2. Set the `HOST`, `PORT`, `time`, and `annoying_music_sample` variables according to your setup.
3. Adjust the `threshold` parameter as needed.

## Usage
1. Run the script.
2. The script continuously captures audio from the microphone and compares it with the annoying music sample.
3. If similarity exceeds the threshold, it sends a socket request to mute the TV for the specified time.

## Configuration
- `HOST`: IP address of the device (Meo Box) to send socket requests.
- `PORT`: Port number of the Meo Box.
- `time`: Time duration to mute the TV.
- `annoying_music_sample`: Path to the annoying music sample (MP3 format).
- `debug`: Set to `True` for printing similarity values for debugging purposes.

## Script Breakdown
- `send_socket_request(key)`: Function to send socket request to mute the TV.
- `compare_audio(sample1, sample2, sr)`: Function to compare audio samples using cosine similarity.
- `capture_audio(rate, chunk_size)`: Function to capture audio from the microphone.
- Loads the annoying music sample and sets parameters.
- Starts the main loop to continuously capture audio and detect similarity.

## Disclaimer
- Ensure that you have the necessary rights to mute the TV using this script.
- Use responsibly and in compliance with applicable laws and regulations.

Feel free to modify the script and its configurations based on your requirements and setup.
