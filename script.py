# Parameters
HOST = "192.168.1.4"  # Meo Box IP
PORT = 8082  # Meo Box Port
time = 30  # Time to mute
annoying_music_sample = "annoying_music_sample.mp3"  # Your ad sample
debug = False  # Debug mode (prints similarity)
threshold = 0.3  # Adjust as needed

# Imports
import pyaudio, socket, librosa, time, numpy
from scipy.spatial.distance import cosine

# Function to send socket request
def send_socket_request(key):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(f"key={key}\n".encode())
    s.close()


# Function to compare two audio samples
def compare_audio(sample1, sample2, sr):
    # Convert mic to mel spectrogram and flatten
    flat1 = librosa.feature.melspectrogram(y=sample1, sr=sr).flatten()
    # Compute cosine similarity
    similarity = 1 - cosine(flat1, flat2)
    return similarity


# Function to capture audio from the microphone
def capture_audio(rate, chunk_size):
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=rate,
        input=True,
        frames_per_buffer=chunk_size,
    )
    while True:
        data = stream.read(chunk_size)
        yield numpy.frombuffer(data, dtype=numpy.float32)
    stream.stop_stream()
    stream.close()
    audio.terminate()


# Load the annoying music sample
annoying_music, sr = librosa.load(annoying_music_sample, sr=None)
chunk_size = len(annoying_music)
flat2 = librosa.feature.melspectrogram(y=annoying_music, sr=sr).flatten()
# Inform the script started
print("A DETETAR")
# Main loop
for mic_input in capture_audio(sr, chunk_size):
    # Calculate similarity between mic input and annoying music sample
    similarity = compare_audio(mic_input, flat2, sr)
    if debug:
        print(similarity)
    # If similarity exceeds threshold, mute the TV
    if similarity > threshold:
        print("DETETADO")
        send_socket_request(173)
        time.sleep(time)
        send_socket_request(173)
