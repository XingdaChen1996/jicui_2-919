# fight for the bright future
# contend: 
# author: xingdachen
# time: 
# email: chenxingda@iat-center.com

import module.Speech_preprocessing as SP
from module.ML_path_read import *
from module.Gaussian_model import *
import numpy as np
import argparse
import pickle
import os
from split_signal import *
from module.Signal_fea import TimeDomain_fea
import time

select_fea = ["p2p", "impulse", "std"]
length_quite = 2600






def Anomaly_det(wave_path):
    Base_Dir = os.path.dirname(os.path.abspath(__file__))
    # saving_model_path = os.path.join(os.path.dirname(Base_Dir), "zhu_train.pkl")
    saving_model_path = os.path.join(Base_Dir, "zhu_train.pkl")

    with open(saving_model_path, "rb") as f:
        obj_model = pickle.load(f)

    str_input = wave_path
    left_queue, right_queue = split_signal(str_input, length_quite_to_need=length_quite, show_fig_genereate_wav=False)
    x_split = np.concatenate((left_queue, right_queue), axis=0)
    filename = str_input
    fea_time_obj = TimeDomain_fea(x_split, filename)
    time_fea = fea_time_obj.create_time_fea()
    output_fea = time_fea
    output_fea = output_fea[select_fea]
    # output_fea = np.array(output_fea)
    outliers = obj_model.Gau_prediect(output_fea, label=None)

    return outliers


if __name__ == '__main__':

    start_time = time.time()  # 开始时间

    parser = argparse.ArgumentParser(description="Anomaly detection")
    parser.add_argument('-p', '--wave_path', type=str, metavar="", required=True,
                        help='path of a wave')

    # 你设置 required=False， 若在 python命令行 不写参数的话，参数没有赋值则为 default 后的参数
    # 你设置 required=True，  若在 python命令行 不写参数的话，直接报错
    # 注意啊： parser.add_argument("-h")会出错， 不允许出现 -h；应为这个库自带-h代表为help命令
    # -p C:\Users\25760\Desktop\JiCui_demo\manually_label\zhu\OK\2300152XAA221118001198689516943224228(1).wav  OK
    # -p C:/Users/25760/Desktop/JiCui_demo/manually_label/zhu/OK/2300152XAA221118001198689516943224228(150).wav  NG
    # -p C:\Users\25760\Desktop\JiCui_demo\manually_label\zhu\NG\2300152XAA221118001198689516943224228(64).wav   NG

    args = parser.parse_args()
    outliers = Anomaly_det(args.wave_path)
    if outliers[0] == 0:
        result = "OK"
    else:
        result = "NG"
    print(f"this wave label: {outliers}  {result}")

    end_time = time.time()  # 结束时间
    print(f"Running Time：{end_time - start_time}")









