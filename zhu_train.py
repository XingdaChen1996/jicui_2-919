# fight for the bright future
# contend: 
# author: xingdachen
# time: 
# email: chenxingda@iat-center.com


from module.ML_path_read import *
from module.Gaussian_model import *
import numpy as np
import pandas as pd
import pickle
import os
from module.Singal_preprocessing import split_pro_fun
import module.Error_analysis
import time
from module.Signal_fea import make_pipe_fea_create
from sklearn.pipeline import make_pipeline

# global val
Model_Metrix = "f1"
pro_pre_fun = split_pro_fun   # 预处理函数，定义的时候第一个参数必须是 path of a wave
pro_pre_fun_arg = {"length_quite_to_need": 2600, "show_fig_genereate_wav": False}  # 预处理函数的形参，不包括 path of a wave
add_fea_fun = [("a_mean_abs", lambda raw_data: np.array(raw_data.abs().mean()))]  # 添加的特征(非通用特征) 形式：[(), ()]
add_fea_fun = {"a_mean_abs": lambda raw_data: np.array(raw_data.abs().mean()+1),   "aa_mean_abs": lambda raw_data: np.array(raw_data.abs().mean())+2}  # 添加的特征(非通用特征) 形式：[(), ()]
Base_Dir = os.path.dirname(os.path.abspath(__file__))
saving_model_path = os.path.join(Base_Dir, "zhu_train.pkl")  # 保存的相对路径


start_time = time.time()  # 开始时间
#  读文件, 将文件path进行划分
output_path_train, output_path_val, output_path_test, label_val, label_test = split_tarin_val_test()


#  fea engineering: fea creation + fea selection,
select_fea = ["p2p", "impulse", "std"]   # 暂时人为选fea


# 输入 output_path_train, output_path_val, label_val
# 输出
# 读取训练集的wav文件路径,并且排序(origin data)
print("------------training pro------------")
# 对output_path_train文件中的.wav文件进行操作： split_pro_fun预处理 + add_fea_fun 人为增加特征(length_quite_to_need=length_quite, show_fig_genereate_wav=False 是split_pro_fun 形参)
output_fea = make_pipe_fea_create(wave_path=output_path_train, pre_fun=pro_pre_fun, add_fea_fun=add_fea_fun, **pro_pre_fun_arg)
output_fea = output_fea[select_fea]
# Gaussian_Model  training
obj_model = Gaussian_Model()
obj_model.estimateGaussian(output_fea)

# Validation
print("------------Validation pro------------")
output_fea = make_pipe_fea_create(wave_path=output_path_val, pre_fun=pro_pre_fun, add_fea_fun=add_fea_fun, **pro_pre_fun_arg)
output_fea = output_fea[select_fea]
# Gaussian_Model  Validation
Threshold, Model_Metrix = obj_model.SelectThreshold(output_fea, label_val, Model_Metrix)
outliers, confuse_m = obj_model.Gau_prediect(output_fea, label_val)

print(Threshold, Model_Metrix)
print(confuse_m.confuse_matrix)
print(confuse_m.acc_precision_recall_F1)
end_time = time.time()  # 结束时间
print(f"Running Time：{end_time - start_time}")

with open(saving_model_path, "wb") as f:
    pickle.dump(obj_model, f)

print("------------testing pro ------------")
output_fea = make_pipe_fea_create(wave_path=output_path_test, pre_fun=pro_pre_fun, add_fea_fun=add_fea_fun, **pro_pre_fun_arg)
output_fea = output_fea[select_fea]
hhh = obj_model.Gau_prediect(output_fea)
outliers, confuse_m = obj_model.Gau_prediect(output_fea, label_test)
pre, temp, pro = obj_model.Gau_prediect(output_fea, label_test, out_pro_flag=True)
print("OKOKOK, Model has been trained, you can try to predict '.wav' in the directory pre_pro")
print("model_obj.pkl have been saved")
print(f"model_obj.pkl model confuse_matrix: {confuse_m.confuse_matrix}")
print(f"model_obj.pkl model acc_precision_recall_F1: {confuse_m.acc_precision_recall_F1}")


#  Error analysis
print("------------Error analysis pro ------------")

all_path = output_path_train + output_path_val + output_path_test
label_all = [0]*len(output_path_train) + label_val + label_test
output_fea = make_pipe_fea_create(wave_path=all_path, pre_fun=pro_pre_fun, add_fea_fun=add_fea_fun, **pro_pre_fun_arg)
output_fea = output_fea[select_fea]


name = all_path
pre, temp, pro = obj_model.Gau_prediect(output_fea, label_all, out_pro_flag=True)
out_all, out_error = module.Error_analysis.generate_error(name, output_fea, pro, pre, label_all)
out_all = out_all.sort_values(by=["Model_probability"])
out_error = out_error.sort_values(by=["Model_probability"])

x = np.linspace(0, obj_model.mu*2, 1000)
y = obj_model.Gaussian_pro(x)
hh = pd.DataFrame(data=y, columns=["Model_probability"])
import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(x="Model_probability", data=out_all, hue="label", multiple="layer", stat="count")
sns.histplot(x="Model_probability", data=hh, multiple="layer", stat="count")
plt.show()

# plt.figure()
# x = np.linspace(0, obj_model.mu*2, 100)
#
# y = obj_model.Gau_prediect(x, label=None, out_pro_flag=True)
#
# plt.plot(x, y)

plt.show()
print("end")

for i in select_fea:
    module.Error_analysis.plot_fea(pd.DataFrame(output_fea[i]), label_all, i)










print("end")

# output_fea = pd.DataFrame()  # feature
# label = len(output_path_OK)*[0] + len(output_path_NG)*[1]
# output_path = output_path_OK + output_path_NG
# for str_input in output_path:
#     left_queue, right_queue = split_signal(str_input, length_quite_to_need=length_quite, show_fig_genereate_wav=False)
#     x_split = np.concatenate((left_queue, right_queue), axis=0)
#     # filename = str_input.split("/")[-1]
#     filename = str_input
#     fea_time_obj = TimeDomain_fea(x_split, filename)
#     time_fea = fea_time_obj.create_time_fea()
#     output_fea = pd.concat((output_fea, time_fea))
# output_fea = output_fea[select_fea]
# # outliers, confuse_m = obj_model.Gau_prediect(output_fea, label, obj_model.dic_par["flag_joint_pro"])
#
# name = output_path
# pre, temp, pro = obj_model.Gau_prediect(output_fea, label, out_pro_flag=True)
# out_all, out_error = module.Error_analysis.generate_error(name, output_fea, pro, pre, label)
# out_all_sort = out_all.sort_values(by=["Model_probability"])
# # module.Error_analysis.plot_fea(output_fea, label)
# for i in select_fea:
#     module.Error_analysis.plot_fea(pd.DataFrame(output_fea[i]), label, i)
#
#
# for i in out_error.index:
#     str_input_test = i
#     filename = str_input_test.split("/")[-1]
#     left_queue, right_queue = split_signal(str_input_test, length_quite_to_need=length_quite, show_fig_genereate_wav=True, show_fig_name=filename)
#     print(f"{i  :} finished")