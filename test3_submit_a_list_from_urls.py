from carbon2.api.submit_list import *
# 根据给出的url列表，批量提交数据，这里这里需要考虑哪些字段也要上传
if __name__=="__main__":
    # server_url = "http://xxxxx:8111"
    server_url = "http://localhost:8889"
    user_id="test"
    # 有多少网页可以上传， 这里设置
    list_url=[
        "http://www.news.cn/politics/leaders/2022-01/11/c_1128253361.htm",
        "http://sports.news.cn/index.htm"
    ]
    submit_url_list(server_url, user_id, list_url, use_md5url_as_id=True,
                         driver_path="browsers/chromedriver.exe")
