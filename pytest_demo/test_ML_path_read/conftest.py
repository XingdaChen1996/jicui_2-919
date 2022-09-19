# fight for the bright future
# contend: 
# author: xingdachen
# time: 
# email: chenxingda@iat-center.com


from test_ML_path_read import *


@pytest.fixture(scope="module",
                params=[("https://baidu.com", "百度")
                         ,("https://aliyun.com", "阿里")
                         ,("https://qq.com", "腾讯")]
                )
def _test_data(request):
    return request.param






@pytest.fixture(scope="class",
                params=[[1]
                         ,[2]
                         ,[3]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                         ,[]
                        ]
                )
def path_list_expect(request):
    return request.param