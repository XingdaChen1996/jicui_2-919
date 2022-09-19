# fight for the bright future
# contend: 
# author: xingdachen
# time: 
# email: chenxingda@iat-center.com

from test_ML_path_read import *
from module.ML_path_read import ML_path_read

# 初始化的参数
Base_Dir = os.path.dirname(os.path.abspath(__file__))
dir_path_list = [
    os.path.join(Base_Dir, "test_data__init__", "data_set1")  # 文件夹路径，文件为空
    , os.path.join(Base_Dir, "test_data__init__", "data_set2")  # 文件夹路径，单层文件，全为非指定类型
    , os.path.join(Base_Dir, "test_data__init__", "data_set3")  # 文件夹路径，多层文件，全为非指定类型
    , os.path.join(Base_Dir, "test_data__init__", "data_set4")  # 文件夹路径，单层文件，部分指定，部分非指定类型
    , os.path.join(Base_Dir, "test_data__init__", "data_set5")  # 文件夹路径，多层文件，部分指定，部分非指定类型
]

# 构造函数参数一
input_dir = [
    os.path.join(Base_Dir, "qqqqqqq")  # 无效路径，路径不存在
    , os.path.join(Base_Dir, "test.py") # 非文件夹的路径，而是文件的路径
]
input_dir.extend(dir_path_list)

# 构造函数参数二
specified_type = [".wav", ".mp3"]

# 构造函数参数三
flag = [False, True]

expected_record = {

 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\qqqqqqq' : {
                                                                                                '.wav':{False: AssertionError("input_dir is not a direction")
                                                                                                        ,True: AssertionError("input_dir is not a direction")

                                                                                                },
                                                                                                '.mp3':{False: AssertionError("input_dir is not a direction")
                                                                                                        ,True: AssertionError("input_dir is not a direction")

                                                                                                }
                                                                                                 }

 ,'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test.py': {
                                                                                                '.wav':{False: AssertionError("input_dir is not a direction")
                                                                                                        ,True: AssertionError("input_dir is not a direction")

                                                                                                },
                                                                                                '.mp3':{False: AssertionError("input_dir is not a direction")
                                                                                                        ,True: AssertionError("input_dir is not a direction")

                                                                                                }
                                                                                                 }
 ,'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set1': {
                                                                                                '.wav':{False: []
                                                                                                        ,True: []

                                                                                                },
                                                                                                '.mp3':{False:[]
                                                                                                        ,True:[]

                                                                                                }
                                                                                                 }
 ,'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set2': {
                                                                                                '.wav':{False: []
                                                                                                        ,True: []

                                                                                                },
                                                                                                '.mp3':{False:[]
                                                                                                        ,True:[]

                                                                                                }
                                                                                                 }
 ,'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set3': {
                                                                                                '.wav':{False: []
                                                                                                        ,True: []

                                                                                                },
                                                                                                '.mp3':{False: []
                                                                                                        ,True: []

                                                                                                }
                                                                                                 }
 ,'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set4': {
                                                                                                '.wav':{False: ['C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set4\\(5)2300152XAA221118001198(1)(1)(1).wa.wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set4\\(6)2300152XAA221118001198689516943224228.wav']
                                                                                                        ,True: ['C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set4\\(5)2300152XAA221118001198(1)(1)(1).wa.wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set4\\(6)2300152XAA221118001198689516943224228.wav']

                                                                                                },
                                                                                                '.mp3':{False: ['C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set4\\(1)(2300152X)AA221118001198689516(2)(2)(2).mp3', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set4\\(2)(4)(4)(4)(3)2300152XAA22111800119868951694322(3)(3)(3)..mp3']
                                                                                                        ,True: ['C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set4\\(1)(2300152X)AA221118001198689516(2)(2)(2).mp3', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set4\\(2)(4)(4)(4)(3)2300152XAA22111800119868951694322(3)(3)(3)..mp3']

                                                                                                }
                                                                                                 }
 ,'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5': {
                                                                                                '.wav':{False: ['C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(1)(2300152X)AA221118001198689516(2)(2)(2).wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(2)(4)(4)(4)(3)2300152XAA22111800119868951694322(3)(3)(3).wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(3)(5)(5)(5)(4)2300152XAA221118001198689516943224(4)(4)(4).wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(4)(6)(6)(6)(5)2300152XAA22111800119868951694322422(5)(5)(5).wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(5)2300152XAA221118001198(1)(1)(1).wa.wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(5)2300152XAA221118001198(1)(1)(1).wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(6)2300152XAA221118001198689516943224228.wav']
                                                                                                        ,True: ['C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(1)(2300152X)AA221118001198689516(2)(2)(2).wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(2)(4)(4)(4)(3)2300152XAA22111800119868951694322(3)(3)(3).wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(3)(5)(5)(5)(4)2300152XAA221118001198689516943224(4)(4)(4).wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(4)(6)(6)(6)(5)2300152XAA22111800119868951694322422(5)(5)(5).wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(5)2300152XAA221118001198(1)(1)(1).wa.wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(5)2300152XAA221118001198(1)(1)(1).wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(6)2300152XAA221118001198689516943224228.wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\22\\(7)(7)(7)(7)(7)2300152XAA221118001198689516943224228107(7)(7).wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\22\\33\\(9)(10)(9)(10)(9)2300152XAA221118001198689516943224228 (217)(9)(9).wav', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\33\\(12)(12)(12)(12)(12)2300152XAA221118001198689516943224228188.wav']

                                                                                                },
                                                                                                '.mp3':{False: ['C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(1)(2300152X)AA221118001198689516(2)(2)(2).mp3', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(2)(4)(4)(4)(3)2300152XAA22111800119868951694322(3)(3)(3)..mp3']
                                                                                                        ,True: ['C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(1)(2300152X)AA221118001198689516(2)(2)(2).mp3', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\(2)(4)(4)(4)(3)2300152XAA22111800119868951694322(3)(3)(3)..mp3', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\22\\(8)(8)(8)(8)(8)2300152XAA22111800119868951694322444(8)(8).mp3', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\22\\33\\(10)(9)(10)(9)(10)2300152XAA221118001198689516943224228 (218)(10)(10).mp3', 'C:\\Users\\25760\\Desktop\\JiCui_demo\\jicui_demo\\pytest_demo\\test_ML_path_read\\test_data__init__\\data_set5\\33\\(12)(12)(12)(12)(12)2300152XAA221118001198689516943224228188.mp3']

                                                                                                }
                                                                                                 }


}



# @pytest.mark.parametrize('dir_path', dir_path)
# @pytest.mark.parametrize()
class Test_ML_path_read():

    @staticmethod
    def unzip_file(zip_scr, dst_dir):
        """
        将zip数据解压到指定的文件夹
        :param zip_scr:  源文件路径
        :param dst_dir:  目标文件夹
        :return: None
        """
        r = zipfile.is_zipfile(zip_scr)
        if r:
            fz = zipfile.ZipFile(zip_scr, 'r')
            for file in fz.namelist():
                fz.extract(file, dst_dir)
        else:
            print('This is not zip')

    @staticmethod
    def del_file(zip_dir, exclude_type):
        """
        将zip数据解压到指定的文件夹
        :param zip_dir:  源文件夹
        :param exclude_type:  不包括的文件的格式
        :return: None
        """
        for i in os.listdir(zip_dir):
            file_path = os.path.join(zip_dir, i)
            if os.path.splitext(file_path)[-1] == exclude_type:
                continue
            else:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                elif os.path.isfile(file_path):
                    os.remove(file_path)

    @classmethod
    def setup_class(cls, dir_path_list=dir_path_list, filename="test_file.zip"):
        print("\n-----setup-----------------")
        for dir_path in dir_path_list:
            zip_scr = os.path.join(dir_path, filename)
            dst_dir = dir_path
            cls.unzip_file(zip_scr, dst_dir)

    @classmethod
    def teardown_class(cls, dir_path_list=dir_path_list, type=".zip"):
        print("\n-----teardown_class-----------------")
        for dir_path in dir_path_list:
            cls.del_file(dir_path, type)


    @pytest.mark.parametrize("flag", flag)
    @pytest.mark.parametrize("specified_type", specified_type)
    @pytest.mark.parametrize('input_dir', input_dir)
    def test_constructor(self, input_dir, specified_type, flag, expected_record=expected_record):
        try:
            obj = ML_path_read(input_dir, specified_type, flag)
        except AssertionError as e:  # AssertionError异常执行
            assert str(e) == str(expected_record[input_dir][specified_type][flag])
        else:  # 无异常执行
            assert obj.path_list == expected_record[input_dir][specified_type][flag]


        # print(obj.path_list)
        # assert obj.path_list == path_list_expect




