# fight for the bright future
# contend: 
# author: xingdachen
# time: 
# email: chenxingda@iat-center.com


import os
import re


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
        try:
            assert os.path.isdir(input_dir) == True
        except AssertionError:
            raise AssertionError("input_dir is not a direction")

        path_list = []
        for curDir, dirs, files in os.walk(input_dir):
            for file in files:
                if os.path.splitext(file)[-1] == specified_type:  # 判断文件后缀名是否一致
                    temp = os.path.join(curDir, file)  # 后缀一致就添加到output_path中
                    path_list.append(temp)
            if not flag:
                break
        self.__path_list = path_list

    def add_filename_parentheses_rank(self):
        """
        如果一个文件下的文件名不是以(int)排好的，则添加(int)为开头
        output_path:  所有的文件path的list
        @param output_path:
        @return: None
        """
        # first step：判断所有的文件是否以(int)开头，只要 path_list 有一个不是 (int)开头，那么全部重改，add_filename_flag 设置为 True
        add_filename_flag = False
        for i in range(0, len(self.__path_list), 1):
            filename = os.path.basename(self.__path_list[i])
            if not re.match(pattern=r"\(\d+\)", string=filename):
                add_filename_flag = True
                break

        if add_filename_flag:  # 如果所有的文件有一个不是以(int)开头，则rename filename + 重新排序
            for i in range(0, len(self.__path_list), 1):
                old_path = self.__path_list[i]  # old path
                old_filename = os.path.basename(self.__path_list[i])  # filename of an old path
                old_dir = os.path.dirname(self.__path_list[i])  # old path excluding filename

                new_filename = str(f"({i + 1})") + old_filename
                new_dir = old_dir
                new_path = os.path.join(new_dir, new_filename)

                self.__path_list[i] = new_path
                os.rename(old_path, new_path)  # 重命名

        print("--------Your filename has been changed--------")

    def get_path_list(self):
        return self.__path_list

    path_list = property(get_path_list)


if __name__ == '__main__':
    Base_Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # file_dir_OK = os.path.join(Base_Dir, "module", "test_file_data") + "1"
    file_dir_OK = os.path.join(Base_Dir, "module", "test_file_datas")
    specified_type = ".wav"
    flag = True
    obj = ML_path_read(input_dir=file_dir_OK, specified_type=specified_type, flag=flag)
    obj.add_filename_parentheses_rank()
    ff = obj.path_list
    print("end")
