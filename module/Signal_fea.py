# fight for the bright future
# contend: 
# author: xingdachen
# time: 
# email: chenxingda@iat-center.com


import os
import numpy as np
import pandas as pd
from scipy.stats import entropy

# Root Mean Squared Sum
def calculate_rms(df):
    result = np.sqrt((df ** 2).sum() / len(df))
    return result


# extract peak-to-peak features
def calculate_p2p(df):
    # return np.array(abs(df.max()) + abs(df.min()))
    return np.array(df.max() - df.min())


# extract shannon entropy (cut signals to 500 bins)
def calculate_entropy(df):
    ent = entropy(pd.cut(df, 500).value_counts())
    return np.array(ent)


# extract clearence factor
def calculate_clearence(df):
    result = ((np.sqrt(df.abs())).sum() / len(df)) ** 2
    return result


dir_fea_name = {
    "mean_abs": lambda raw_data: np.array(raw_data.abs().mean())
    , "std": lambda raw_data: np.array(raw_data.std())
    , "skew": lambda raw_data: np.array(raw_data.skew())
    , "kurtosis": lambda raw_data: np.array(raw_data.kurtosis())
    , "entropy": lambda raw_data: calculate_entropy(raw_data)
    , "rms": lambda raw_data: np.array(calculate_rms(raw_data))
    , "max_abs": lambda raw_data: np.array(raw_data.abs().max())
    , "p2p": lambda raw_data: calculate_p2p(raw_data)
    , "crest": lambda raw_data: dir_fea_name["max_abs"](raw_data) / dir_fea_name["rms"](raw_data)
    , "clearence": lambda raw_data: np.array(calculate_clearence(raw_data))
    , "shape": lambda raw_data: dir_fea_name["rms"](raw_data) / dir_fea_name["mean_abs"](raw_data)
    , "impulse": lambda raw_data: dir_fea_name["max_abs"](raw_data) / dir_fea_name["mean_abs"](raw_data)
}


class fea_creation(object):

    def __init__(self, raw_data, filename):
        raw_data = pd.Series(raw_data)
        self.raw_data = raw_data
        self.name = filename

    def add_fea(self, fea_fun):
        if fea_fun:
            for key in fea_fun:
                dir_fea_name[key] = fea_fun[key]

    def create_fea(self):
        #  单个文件fea的 value；name；filename
        fea_value = []
        for i in dir_fea_name:
            temp = dir_fea_name[i](self.raw_data)
            fea_value.append(temp)
        file_name = [self.name]
        fea_name = [tf for tf in dir_fea_name]
        data = pd.DataFrame(data=np.array(fea_value).reshape(1, -1), index=file_name, columns=fea_name)
        return data


def make_pipe_fea_create(wave_path, pre_fun, add_fea_fun=None, *args, **kwargs):
    output_fea = pd.DataFrame()  # feature
    for str_input in wave_path:
        # 先预处理(如去噪声函数， 切割函数等)
        x = pre_fun(str_input, *args, **kwargs)
        # 创建fea_creation类
        # filename = str_input.split("/")[-1]
        # fea_obj = fea_creation(x, filename)
        fea_obj = fea_creation(x, str_input)

        # 创建fea
        fea_obj.add_fea(add_fea_fun)
        temp = fea_obj.create_fea()
        output_fea = pd.concat((output_fea, temp))

    return output_fea








