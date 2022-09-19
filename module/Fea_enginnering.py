# fight for the bright future
# contend: 
# author: xingdachen
# time: 
# email: chenxingda@iat-center.com

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score
import pandas as pd
import os
from module.ML_path_read import ML_read
#  fea creation：
#  step1: 读取所有的文件path，生成.wav文件; step2: 检查fea是否有格式错误数据(字符串类型， np.nan or None类型， 有就报错)，
#  metrix: roc_auc_score
#  1D Gaussian Model, multi D Gaussian Model


Base_Dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
file_dir_all = os.path.join(Base_Dir, "manually_label", "zhu")

def split_tarin_val_test(shuffle=False, random_state=21):
    ml_read_obj = ML_read()
    output_path_OK = ml_read_obj.read_specified_file(input_dir=file_dir_all, specified_type=".wav", flag=1)

class fea_engineering(object):

    def __init__(self, output_path_train, output_path_val, label_val):
        pass










def result_df(model, X_train, y_train, X_test, y_test, metrics=
              [accuracy_score, recall_score, precision_score, f1_score, roc_auc_score]):
    res_train = []
    res_test = []
    col_name = []
    for fun in metrics:
        res_train.append(fun(model.predict(X_train), y_train))
        res_test.append(fun(model.predict(X_test), y_test))
        col_name.append(fun.__name__)
    idx_name = ['train_eval', 'test_eval']
    res = pd.DataFrame([res_train, res_test], columns=col_name, index=idx_name)
    return res