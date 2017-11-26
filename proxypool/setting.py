# Redis数据库的地址和端口
from fake_useragent import UserAgent

HOST = 'localhost'
PORT = 6379

# 如果Redis有密码，则添加这句密码，否则设置为None或''
PASSWORD = ''

# 获得代理测试时间界限
get_proxy_timeout = 9

# 代理池数量界限
POOL_LOWER_THRESHOLD = 20
POOL_UPPER_THRESHOLD = 100

# 检查周期
VALID_CHECK_CYCLE = 60
POOL_LEN_CHECK_CYCLE = 20

# 测试API，用百度来测试
TEST_API='http://www.baidu.com'


# 设置Headers
ua = UserAgent()
base_headers = {
    'User-Agent': ua.random,
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}
HEADERS = dict(base_headers)