# fight for the bright future
# contend: 
# author: xingdachen
# time: 
# email: chenxingda@iat-center.com


# fight for the bright future
# contend:
# author: xingdachen
# time:
# email: chenxingda@iat-center.com


import os
import re
# import shutil
# import soundfile as sf
# import pandas as pd
# from sklearn.model_selection import train_test_split



# def split_tarin_val_test(specified_type=".wav", flag=0, shuffle=False, random_state=21):
#     ml_read_obj = ML_read()
#     output_path_OK = ml_read_obj.read_specified_file(input_dir=file_dir_OK, specified_type=specified_type, flag=flag)
#     output_path_NG = ml_read_obj.read_specified_file(input_dir=file_dir_NG, specified_type=specified_type, flag=flag)
#
#     output_path_train_OK, output_path_val_test_OK = train_test_split(output_path_OK, test_size=0.4, shuffle=shuffle,
#                                                                      random_state=random_state)
#     output_path_val_OK, output_path_test_OK = train_test_split(output_path_val_test_OK, test_size=0.5, shuffle=False)
#     ooutput_path_val_NG, output_path_test_NG = train_test_split(output_path_NG, test_size=0.5, shuffle=shuffle,
#                                                                 random_state=random_state)
#
#     output_path_train = output_path_train_OK
#     output_path_val = output_path_val_OK + ooutput_path_val_NG
#     output_path_test = output_path_test_OK + output_path_test_NG
#
#     label_val = len(output_path_val_OK) * [0] + len(ooutput_path_val_NG) * [1]
#     label_test = len(output_path_test_OK) * [0] + len(output_path_test_NG) * [1]
#
#     return output_path_train, output_path_val, output_path_test, label_val, label_test


# New version

class ML_path_read(object):

    def __init__(self, input_dir, specified_type=".wav", flag=False):
        """
        读取一个文件夹下面的的指定文件，返回一个list
        :param input_dir: str
        :param specified_type: str
        :param flag: bool True or False
        False: 读取改文件夹下面第一层的所有 specified_type 文件
        True： 读取改文件夹下面所有层的所有 specified_type 文件
        :return: list
        所有指定文件的目录组成的list
        """

        path_list = []
        for curDir, dirs, files in os.walk(input_dir):
            for file in files:
                if os.path.splitext(file)[-1] == specified_type:  # 判断文件后缀名是否一致
                    temp = os.path.join(curDir, file)  # 后缀一致就添加到output_path中
                    path_list.append(temp)
            if not flag:
                break
        self.path_list = path_list

    def add_filename_parentheses_rank(self):
        """
        如果一个文件下的文件名不是以(int)排好的，则添加(int)为开头
        output_path:  所有的文件path的list
        @param output_path:
        @return: None
        """

        # os.path.splitext(item)[-1]  # 获取path后缀，  #  没找到返回-1，找到的话返回最右边的index
        # file = os.path.basename(output_path[0])  # filename of a path
        # path = os.path.dirname(output_path[0])   # path excluding filename
        # s.startswith("(")
        # string[0].isdigit()

        # first step：判断所有的文件是否以(int)开头，只要 path_list 有一个不是 (int)开头，那么全部重改，add_filename_flag 设置为 True
        add_filename_flag = False
        for i in range(0, len(self.path_list), 1):
            filename = os.path.basename(self.path_list[i])
            if not re.match(pattern=r"\(\d+\)", string=filename):
                add_filename_flag = True
                break
            # index_left_parentheses = filename.find("(")
            # index_right_parentheses = filename.find(")")
            # if index_left_parentheses != 0 or index_right_parentheses == -1 \
            #         or not self.path_list[i][index_left_parentheses + 1: index_right_parentheses].isdigit():
            #     add_filename_flag = True
            #     break

        if add_filename_flag:  # 如果所有的文件有一个不是以(int)开头，则rename filename + 重新排序
            for i in range(0, len(self.path_list), 1):
                old_path = self.path_list[i]  # old path
                old_filename = os.path.basename(self.path_list[i])  # filename of an old path
                old_dir = os.path.dirname(self.path_list[i])   # old path excluding filename

                new_filename = str(f"({i+1})") + old_filename
                new_dir = old_dir
                new_path = os.path.join(new_dir, new_filename)

                self.path_list[i] = new_path
                os.rename(old_path, new_path)  # 重命名

        print("--------Your filename has been changed--------")


if __name__ == '__main__':
    Base_Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_dir_OK = os.path.join(Base_Dir, "module", "test_file_data")
    specified_type = ".wav"
    flag = True

    # obj = ML_read()
    # output_path = obj.read_file_sorted(input_dir=file_dir_OK, specified_type=specified_type, flag=flag)

    obj = ML_path_read(input_dir=file_dir_OK, specified_type=specified_type, flag=flag)
    obj.add_filename_parentheses_rank()
    ff = obj.path_list


