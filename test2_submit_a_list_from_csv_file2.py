from carbon2.api.submit_list import *
# 根据给出的csv文件，批量提交数据，这里这里需要考虑哪些字段也要上传
if __name__=="__main__":
    server_url = "http://xxxx:8111"
    # server_url = "http://localhost:8889"
    user_id="test"
    csv_file="data/baidu_carbon_neutrality_20220114.txt"
    save_folder="html_data"
    submit_page_list(server_url, user_id, csv_file, save_folder, use_md5url_as_id=True,
                         driver_path="browsers/chromedriver.exe") # chromedriver.exe需要和用户电脑的chrome浏览器版本号一致，具体请查询百度 chromedriver的使用
