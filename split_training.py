# fight for the bright future
# contend:
# author: xingdachen
# time:
# email: chenxingda@iat-center.com

from module.Speech_preprocessing import *
from module.ML_path_read import *
from module.Gaussian_model import *
import numpy as np
import pickle
import math


# split_quite_num = 100  # 分割的长度(参数)
# threshold = 0.001
# SubtractWave_threshold = 0.00045
# length_quite_to_need = 2200

dic_par = {}
flag_joint_pro = 1  # hyper1 是否使用联合概率分布,只有完整看时间序列才是0，一般都是1
Model_Metrix = "f1"
dic_par["flag_joint_pro"] = flag_joint_pro

# 读取训练集的wav文件路径,并且排序(origin data)
print("------------training pro------------")
ml_read_obj = ML_read()

Base_Dir = os.path.dirname(os.path.abspath(__file__))
saving_model_path = os.path.join(Base_Dir, "split_model_obj.pkl")
Base_Dir = os.path.join(os.path.dirname(Base_Dir), "manually_label", "split", "input")

file_dir_training = os.path.join(Base_Dir, "training_data_set")
file_dir_val = os.path.join(Base_Dir, "validation_data_set")
file_dir_test = os.path.join(Base_Dir, "testing_data_set")
col_str = ["T2", "T3"]

# saving_model_path = os.path.join(os.path.abspath(__file__.split("JiCui_demo")[0]), "JiCui_demo",
# "split_model_obj.pkl")


file_dir = os.path.join(file_dir_training, "01NG")
output_path = ml_read_obj.read_specified_file(input_dir=file_dir, specified_type=".wav", flag=0)

# 读取训练集的excel(label file)
file_path = os.path.join(file_dir_training, "01NG.xlsx")
index = ml_read_obj.read_excel_file(file_path, col_str)
# print(index)

# 语音预处理
speech_pre_time_obj = speech_pre_time()

output_x_wave_index_all = []  # feature
for i in range(len(output_path)):
    x, FS_samplerate = sf.read(output_path[i])
    X_quite_need_index = list(range(index[i][0], index[i][1]+1, speech_pre_time_obj.split_quite_num))
    output_x_index_wave = speech_pre_time_obj.wave(X_quite_need_index, x)
    output_x_wave_index_all.extend(output_x_index_wave)
    # X_quite_need_index = np.array(X_quite_need_index)
    # output_x_index_wave = np.array(output_x_index_wave)


output_x_wave_index_all = np.array(output_x_wave_index_all)


# Gaussian model
# training process
speech_split_obj = Gaussian_Model()
speech_split_obj.estimateGaussian(output_x_wave_index_all)
# p = speech_split_obj.Gaussian_pro(output_x_wave_index_all)

# Validation file

# 读取验证集的wav文件(origin data)
print("------------Validation pro------------")
ml_read_obj = ML_read()
file_dir = os.path.join(file_dir_val, "02NG")

output_path = ml_read_obj.read_specified_file(input_dir=file_dir, specified_type=".wav", flag=0)

# 读取验证集的excel(label file)
file_path = os.path.join(file_dir_val, "02NG.xlsx")
index = ml_read_obj.read_excel_file(file_path, col_str)

output_x_wave_index_all_val = []  # feature
label_all = []  # label
for i in range(len(output_path)):
    label = []
    x, FS_samplerate = sf.read(output_path[i])
    X_quite_need_index_allx = list(range(1, len(x) + 2, speech_pre_time_obj.split_quite_num))
    output_x_index_wave_allx = speech_pre_time_obj.wave(X_quite_need_index_allx, x)

    label.extend([1] * math.floor(index[i][0] / speech_pre_time_obj.split_quite_num))
    label.extend([0] * (math.floor(index[i][1] / speech_pre_time_obj.split_quite_num) - math.floor(index[i][0] / speech_pre_time_obj.split_quite_num)))
    label.extend([1] * (len(output_x_index_wave_allx) - math.floor((index[i][1]) / speech_pre_time_obj.split_quite_num)))

    output_x_wave_index_all_val.extend(output_x_index_wave_allx)
    label_all.extend(label)

# Validation process and saving model to "input\saving_model"
Threshold, Model_Metrix_val = speech_split_obj.SelectThreshold(output_x_wave_index_all_val, label_all, Model_Metrix, dic_par["flag_joint_pro"])

speech_split_obj.dic_par = dic_par
with open(saving_model_path, "wb") as f:
    pickle.dump(speech_split_obj, f)


if __name__ == '__main__':
    print("------------text example ------------")
    # 加载模型
    # saving_model_path,  col_str = ["T2", "T3"]
    speech_pre_time_obj = speech_pre_time()
    with open(saving_model_path, "rb") as f:
        obj_model = pickle.load(f)

    # 读取测试集的wav文件(origin data)
    ml_read_obj = ML_read()
    file_dir = os.path.join(file_dir_test, "01OK")
    output_path = ml_read_obj.read_specified_file(input_dir=file_dir, specified_type=".wav", flag=0)

    # 读取测试集的excel(label file)
    file_path = os.path.join(file_dir_test, "01OK.xlsx")
    index = ml_read_obj.read_excel_file(file_path, col_str)

    # 语音预处理,提取特征
    output_x_wave_index_all_val = []  # feature
    label_all = []  # label
    for i in range(len(output_path)):
        label = []
        x, FS_samplerate = sf.read(output_path[i])
        X_quite_need_index_allx = list(range(1, len(x) + 2, speech_pre_time_obj.split_quite_num))
        output_x_index_wave_allx = speech_pre_time_obj.wave(X_quite_need_index_allx, x)

        label.extend([1] * math.floor(index[i][0] / speech_pre_time_obj.split_quite_num))
        label.extend([0] * (math.floor(index[i][1] / speech_pre_time_obj.split_quite_num) - math.floor(index[i][0] / speech_pre_time_obj.split_quite_num)))
        label.extend([1] * (len(output_x_index_wave_allx) - math.floor((index[i][1]) / speech_pre_time_obj.split_quite_num)))

        output_x_wave_index_all_val.extend(output_x_index_wave_allx)
        label_all.extend(label)

    outliers, precision_recall_F1 = obj_model.Gau_prediect(output_x_wave_index_all_val, label_all, obj_model.dic_par["flag_joint_pro"])
    print("split_training end")






