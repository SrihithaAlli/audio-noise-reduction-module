import soundfile as sf
import noisereduce as nr
import numpy as np

# Load audio
audio, sr = sf.read("input.wav")

# Convert stereo to mono
if len(audio.shape) > 1:
    audio = np.mean(audio, axis=1)

# Reduce noise
reduced_audio = nr.reduce_noise(
    y=audio,
    sr=sr
)

# Save cleaned audio
sf.write("cleaned.wav", reduced_audio, sr)

print("Noise reduction completed successfully!")