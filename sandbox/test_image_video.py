import ffmpegio
from matplotlib import pyplot as plt

# vf = ffmpegio.FilterGraph(
#     [
#         [
#             (
#                 "drawtext",
#                 {
#                     "fontfile": "C:\\WINDOWS\\FONTS\\BKANT.TTF",
#                     "text": "Test Text",
#                     "x": "(w-text_w)/2",
#                     "y": "(h-text_h)/2",
#                     "fontsize": 24,
#                     "fontcolor": "black@0.8",
#                     "box": 1,
#                     "boxcolor": "white@0.5",
#                     "boxborderw": 6,
#                 },
#             )
#         ]
#     ]
# )

# I = ffmpegio.image.create("smptebars", d=1, vf=vf)

# plt.imshow(I)
# plt.show()

# T = 10
# ffmpegio.video.write(
#     r"sandbox\test.mp4", 1 / T, I, r=25, t=10, show_log=True, overwrite=True
# )

i = 0

url = r'sandbox\test.mp4'

info = ffmpegio.probe.video_streams_basic(url)[0]
w = info['width']
h = info['height']

with ffmpegio.open(url, f_in='lavfi',pix_fmt='rgb24', 
                   hwaccel_in='auto',bufsize=w*h*3*2) as f:
    for image in f:
        i += 1
        print(image.shape,image.dtype)

        # throw away the data in the pipe's buffer.
        f.read(2) # flush the buffer (of size 2)

        if i>2:
            break
