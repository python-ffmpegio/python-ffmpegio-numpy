"""ffmpegio plugin to use `numpy.ndarray` objects for media data I/O"""

import numpy as np
from pluggy import HookimplMarker

hookimpl = HookimplMarker("ffmpegio")

__all__ = [
    "video_info",
    "audio_info",
    "video_bytes",
    "audio_bytes",
    "bytes_to_video",
    "bytes_to_audio",
]


@hookimpl
def video_info(obj: object) -> tuple[tuple[int, int, int], str]:
    """get video frame info

    :param obj: object containing video frame data with arbitrary number of frames
    :type obj: object
    :return: shape (height,width,components) and data type in numpy dtype str expression
    :rtype: tuple[tuple[int, int, int], str]
    """
    return obj.shape[-3:], obj.dtype.str


@hookimpl
def audio_info(obj: object) -> tuple[int, str]:
    """get audio sample info

    :param obj: object containing audio data (with interleaving channels) with arbitrary number of samples
    :type obj: object
    :return: number of channels and sample data type in numpy dtype str expression
    :rtype: tuple[tuple[int], str]
    """
    return obj.shape[-1:], obj.dtype.str


@hookimpl
def video_bytes(obj: object) -> memoryview:
    """return bytes-like object of packed video pixels, associated with `video_info()`

    :param obj: object containing video frame data with arbitrary number of frames
    :type obj: object
    :return: packed bytes of video frames
    :rtype: bytes-like object
    """

    return memoryview(obj)


@hookimpl
def audio_bytes(obj: object) -> memoryview:
    """return bytes-like object of packed audio samples

    :param obj: object containing audio data (with interleaving channels) with arbitrary number of samples
    :type obj: object
    :return: packed bytes of audio samples
    :rtype: bytes-like object
    """

    return memoryview(obj)


@hookimpl
def bytes_to_video(b: bytes, dtype: str, shape: tuple[int, int, int]) -> object:
    """convert bytes to rawvideo object

    :param b: byte data of arbitrary number of video frames
    :type b: bytes
    :param dtype: data type numpy dtype string (e.g., '|u1', '<f4')
    :type dtype: str
    :param size: frame dimension in pixels and number of color components (height, width, components)
    :type size: tuple[int, int, int]
    :return: python object holding the rawvideo frames
    :rtype: object
    """

    return np.frombuffer(b, dtype).reshape(-1, *shape)


@hookimpl
def bytes_to_audio(b: bytes, dtype: str, shape: tuple[int]) -> object:
    """convert bytes to rawaudio object

    :param b: byte data of arbitrary number of video frames
    :type b: bytes
    :param dtype: numpy dtype string of the bytes (e.g., '<s2', '<f4')
    :type dtype: str
    :param shape: number of interleaved audio channels (1-element tuple)
    :type shape: tuple[int]
    :return: python object to hold the raw audio samples
    :rtype: object
    """

    return np.frombuffer(b, dtype).reshape(-1, *shape)
