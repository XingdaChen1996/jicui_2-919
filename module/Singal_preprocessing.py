# fight for the bright future
# contend: 
# author: xingdachen
# time: 
# email: chenxingda@iat-center.com

# 预处理，如去噪声函数，第一个参数必须是path of a wave，*args, **kwargs 代表了后面的参数。

from split_signal import split_signal
import soundfile as sf
import numpy as np


def split_pro_fun(*args, **kwargs):
    x, FS_samplerate = sf.read(*args, **kwargs)
    return x


def split_pro_fun(*args, **kwargs):
    left_queue, right_queue = split_signal(*args, **kwargs)
    x_split = np.concatenate((left_queue, right_queue), axis=0)
    return x_split




