import logging

logging.basicConfig(level=logging.DEBUG)

from fractions import Fraction
import ffmpegio
from tempfile import TemporaryDirectory
from os import path
import numpy as np


def test_gray12le():

    # codec = "h264"
    # size = [256, 256]
    # pix_fmt = "gray"
    # vmax = 2**8
    # dtype = "u1"
    # framerate = Fraction(30, 1)

    codec = "ffv1"
    size = [254, 177]
    pix_fmt = "gray12le"
    vmax = 2**12
    dtype = "<u2"
    framerate = Fraction(32, 1)

    show_log = True

    with TemporaryDirectory() as dir:
        filepath = path.join(dir, "temp.mkv")
        with ffmpegio.open(
            filepath,
            "vw",
            framerate,
            # s_in=size,
            pix_fmt_in=pix_fmt,
            # pix_fmt=pix_fmt,
            show_log=show_log,
            vcodec=codec,
        ) as f:
            for n in range(30):
                I = np.random.randint(0, vmax, [*size[::-1]], dtype)
                f.write(I)

        with ffmpegio.open(filepath, "rv", show_log=show_log) as f:
            for Iout in f:
                pass

        assert np.array_equal(I, Iout[-1, :, :, 0])

        # print(ffmpegio.probe.video_streams_basic(filepath))
        r_out, Iout = ffmpegio.video.read(
            filepath,
            # show_log=show_log,
            # pix_fmt="gray12le",
        )

        assert np.array_equal(I, Iout[-1, :, :, 0])

        filepath1 = path.join(dir, "temp1.mkv")
        ffmpegio.video.write(
            filepath1,
            r_out,
            Iout,
            show_log=show_log,
            pix_fmt_in="gray12le",
            vcodec=codec,
        )
        r_out, Iout1 = ffmpegio.video.read(
            filepath1,
            # show_log=show_log,
            # pix_fmt="gray12le",
        )
        assert np.array_equal(Iout1, Iout)

        # print(ffmpegio.probe.video_streams_basic(filepath))
        I0 = ffmpegio.image.read(
            filepath,
            # show_log=show_log
            # pix_fmt="gray12le",
        )

        assert np.array_equal(I0, Iout[0, :, :, 0])

    # print(sorted(ffmpegio.caps.pix_fmts().keys()))

if __name__=='__main__':
    test_gray12le()


    # -nostdin -hide_banner -pix_fmt gray12le -r 32 -f rawvideo -s 254x177 -i - 
    #   -vcodec ffv1 -r 32 'C:\Users\tikum\AppData\Local\Temp\tmp_xgk_lki\temp.mkv'
    # -nostdin -hide_banner -f rawvideo -c:v rawvideo -s 254x177 -r 32 -pix_fmt gray12le -i - 
    #   -vcodec ffv1 'C:\Users\tikum\AppData\Local\Temp\tmp39wbec7m\temp1.mkv'