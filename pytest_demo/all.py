# fight for the bright future
# contend: 
# author: xingdachen
# time: 
# email: chenxingda@iat-center.com

from test_ML_path_read import *

if __name__ == "__main__":
    # pytest_demo.main(["-vs", "test_package2/test_2.py::test_fun4"])
    pytest.main()
    os.system("allure generate ./test_ML_path_read/allure_dir -o ./test_ML_path_read/report__init__ --clean")
