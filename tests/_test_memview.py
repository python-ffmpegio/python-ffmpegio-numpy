import subprocess as sp
import numpy as np

fs = 48000
x = np.random.randint(-)
fs, x = audio.create("anoisesrc", d=60, c="pink", a=0.5, sample_fmt="s16")
print(fs)
print(x.shape, x.dtype.str,len(memoryview(x)))

x = np.ascontiguousarray(x)

with tempfile.TemporaryDirectory() as tmpdirname:
    wavfile = path.join(tmpdirname, "test.wav")
    audio.write(wavfile, fs, x, show_log=True)
    pprint(probe.full_details(wavfile))
    fs1, x1 = audio.read(wavfile)
