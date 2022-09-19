import re
import os
import math

# source = """苹果.是绿色的
# 橙子.是橙色的.
# 香蕉.是黄色的"""
#
#
# p = re.compile(r".*?\.")
# gg = p.findall(source)
# print(p.findall(source))
#
#
# so = "<1><1><1><1><1>45<541651>"
#
# p = re.compile(r"666")
# ggd = p.findall(so)
#
#
# pattern = r"\(\d+\)"
# string = "(555555)kopjkghp(454)ok"
#
# re.match(pattern, string, flags=0)

# input_dir = r"C:\Users\25760\Desktop\JiCui_demo\jicui_demo\pytest_demo\ML_path_read\test_data_set\(1)(2300152X)AA221118001198689516(2)(2)(2).wav"
#
# try:
#     assert os.path.isdir(input_dir) == True
# except AssertionError:
#      print("input_dir is not a direction")
#
#
#
# def sqrt(x):
#     try:
#         assert x >= 0
#         num = math.sqrt(x)
#         print("num is: ", num)
#     except:
#         print("if you want to solve sqrt num, x must be bigger or equal zero!")
#
# sqrt(4)
# sqrt(-4)


aaa = ["2123", "564"]
bbb = ["rr", "dg"]
aaa.extend(bbb)



try:
    a = input("shuru:")
    a = int(a)
    b=0
    a/b
except:
    print("11")
    raise RuntimeError

print("222")