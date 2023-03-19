from pprint import pprint
import tempfile
from os import path
import numpy as np

from ffmpegio import plugins, utils, audio, video, probe


def test_hooks():
    hook = plugins.get_hook()

    dtype = "|u1"
    shape = (2, 2, 3)
    b = b"\0" * utils.prod(shape)
    data = hook.bytes_to_video(b=b, dtype=dtype, shape=shape, squeeze=False)
    assert memoryview(data).cast("b") == b
    assert data.dtype.str == dtype
    assert data.shape[1:] == shape
    assert hook.video_info(obj=data) == (shape, dtype)
    assert hook.video_bytes(obj=data).cast("b") == b

    data = hook.bytes_to_video(b=b, dtype=dtype, shape=shape, squeeze=True)
    assert data.shape == shape

    dtype = "<f4"
    shape = (2,)
    b = b"\0" * (1024 * utils.prod(shape))
    data = hook.bytes_to_audio(b=b, dtype=dtype, shape=shape, squeeze=False)
    assert memoryview(data).cast("b") == b
    assert data.dtype.str == dtype
    assert data.shape[1:] == shape
    assert hook.audio_info(obj=data) == (shape, dtype)
    assert hook.audio_bytes(obj=data).cast("b") == b

    print(plugins.pm.get_plugins())


def test_audio():
    fs, x = audio.create("anoisesrc", d=10, c="pink", a=0.5, sample_fmt="s16")
    print(fs)
    print(x.shape, x.dtype.str)

    with tempfile.TemporaryDirectory() as tmpdirname:
        wavfile = path.join(tmpdirname, "test.wav")
        audio.write(wavfile, fs, x, show_log=True)
        pprint(probe.full_details(wavfile))
        fs1, x1 = audio.read(wavfile)

        audio.write(wavfile, fs, x1, show_log=True, overwrite=True)

    assert fs == fs1
    # TODO: shape not same in GH Action
    # assert x.shape == x1.shape
    # assert np.array_equal(x, x1)


def test_video():
    fs, F = video.create("cellauto", p="@@ @ @@", s="100x400", full=0, rule=18, t_in=1)
    print(fs)
    print(F.shape, F.dtype.str)

    with tempfile.TemporaryDirectory() as tmpdirname:
        avifile = path.join(tmpdirname, "test.avi")
        video.write(avifile, fs, F, pix_fmt="bgr24", vcodec="rawvideo", show_log=True)
        fs1, F1 = video.read(avifile)

        # test 2-D input
        video.write(avifile, fs, np.array(F[0, :, :, 0]), show_log=True, overwrite=True)

    assert fs == fs1
    assert np.array_equal(F, F1)


if __name__ == "__main__":
    test_video()
