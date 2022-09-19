# fight for the bright future
# contend: 
# author: xingdachen
# time: 
# email: chenxingda@iat-center.com

from module.Speech_preprocessing import *
from module.Gaussian_model import *
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np
from scipy import stats
import math
import pickle
import os

Base_Dir = os.path.dirname(os.path.abspath(__file__))
# saving_model_path = os.path.join(os.path.dirname(Base_Dir), "split_model_obj.pkl")
saving_model_path = os.path.join(Base_Dir, "split_model_obj.pkl")


with open(saving_model_path, "rb") as f:
    obj_model = pickle.load(f)


def split_signal(str_input_test, length_quite_to_need, show_fig_genereate_wav, show_fig_name="split_signal",model_mean=obj_model.mu, model_std=obj_model.sigma,
                 model_threshold=obj_model.Threshold, model_split_quite_num=100):
    # hyper parameters(Gaussian model)

    index_mean_std = [model_mean[0], model_std[0]]
    wave_mean_std = [model_mean[1], model_std[1]]


    # SubtractWave_index_mean_std = [62219.7527740790, 3801.65095979423]
    # SubtractWave_wave_mean_std = [0.00406369185161971, 0.0290240894019698]
    threshold = model_threshold
    # SubtractWave_threshold = 0.00045
    # hyper parameters(Speech model)
    split_quite_num = model_split_quite_num  # 分割的长度(参数)
    a_hyper = 0.05
    b_hyper = 0.95
    c_hyper = 0.05
    d_hyper = 0.95
    text_sum_pro_choose = 0.04
    filename_left_queue = "left_queue.wav"
    filename_right_queue = "right_queue.wav"
    speech_pre_time_obj = speech_pre_time(a_hyper, b_hyper, split_quite_num, c_hyper, d_hyper, text_sum_pro_choose)

    x, FS_samplerate = sf.read(str_input_test)
    X_quite_need_index_allx = list(range(1, len(x) + 2, split_quite_num))
    output_x_index_wave_text_x = speech_pre_time_obj.wave(X_quite_need_index_allx, x)
    output_x_index_wave_text_x = np.array(output_x_index_wave_text_x)

    text_index_probability = stats.norm(index_mean_std[0], index_mean_std[1]).pdf(output_x_index_wave_text_x[:,0])
    text_wave_probability = stats.norm(wave_mean_std[0], wave_mean_std[1]).pdf(output_x_index_wave_text_x[:,1])
    text_sum_pro = text_index_probability * text_wave_probability

    # output_list_index_SubtractWave = speech_pre_time_obj.subtract_wave(output_x_index_wave_text_x, text_sum_pro)
    # SubtractWave_text_index_probability = stats.norm(SubtractWave_index_mean_std[0],
    #                                                  SubtractWave_index_mean_std[1]).pdf(
    #     output_list_index_SubtractWave[0])
    # SubtractWave_text_wave_probability = stats.norm(SubtractWave_wave_mean_std[0], SubtractWave_wave_mean_std[1]).pdf(
    #     output_list_index_SubtractWave[1])
    # SubtractWave_text_sum_pro = SubtractWave_text_index_probability * SubtractWave_text_wave_probability

    out_index_left = -1
    out_index_right = -1

    for j in range(len(text_sum_pro)):
        if text_sum_pro[j] > threshold and text_sum_pro[j+1] > threshold and text_sum_pro[j+2] > threshold and text_sum_pro[j+50] > threshold:
            out_index_left = j + 1  # just for matlab index
            break
    for j in range(-1, -len(text_sum_pro) - 1, -1):
        if text_sum_pro[j] > threshold and text_sum_pro[j-1] > threshold and text_sum_pro[j-2] > threshold and text_sum_pro[j-50] > threshold:
            out_index_right = len(text_sum_pro) + j
            out_index_right = out_index_right + 1  # just for matlab index
            break

    if out_index_left == -1 or out_index_right == -1:
        print("something wrong with you, we can not generate split signal")

    output_test_need_index = [out_index_left * split_quite_num - 49, out_index_right * split_quite_num - 49]

    # result

    left_queue = x[0:output_test_need_index[0] - length_quite_to_need]
    right_queue = x[output_test_need_index[1] + length_quite_to_need - 1:output_test_need_index[
                                                                             1] + length_quite_to_need + len(
        left_queue) - 1]

    # 如果你想要 split图片 分割的.wav  x[output_test_need_index[0]:output_test_need_index[1]]

    if show_fig_genereate_wav:
        plt.figure()
        # plt.title(f'{show_fig_name} split_signal')
        plt.title('Split Signal')
        plt.plot(range(1, len(x) + 1, 1), x, label='origin sigal')
        plt.plot(range(1, len(left_queue) + 1, 1), left_queue, label='left queue')
        plt.plot(range(output_test_need_index[0], output_test_need_index[1], 1), x[output_test_need_index[0]:output_test_need_index[1]], label='quiet')   # 可以去除
        plt.plot(range(output_test_need_index[1] + length_quite_to_need,
                       len(left_queue) + output_test_need_index[1] + length_quite_to_need, 1)
                 , right_queue, label='right queue')

        plt.legend()
        # plt.show()
        # plt.savefig("split_signal.png")
        plt.savefig("{}-split_signal.png".format(show_fig_name))
        sf.write(filename_left_queue, left_queue, FS_samplerate)
        sf.write(filename_right_queue, right_queue, FS_samplerate)

    return left_queue, right_queue


if __name__ == '__main__':
    length_quite = 2600
    str_input_test = r"C:\Users\25760\Desktop\JiCui_demo\manually_label\zhu\NG\2300152XAA221118001198689516943224228(282).wav"
    left_queue, right_queue = split_signal(str_input_test, length_quite_to_need=length_quite, show_fig_genereate_wav=True)
    print("end")
