import requests
import json
from quick_crawler.page import quick_html_page,quick_html_object,quick_download_file,quick_save_csv
from quick_crawler.browser import get_html_str_with_browser
import os
from tqdm import tqdm

if __name__=="__main__":
    api_url = "http://xxxxx:8111/api/Data"
    list_model = []
    fields = []
    for page_index in tqdm(range(1,12+1)):# 这里请设置总页数，比如共有12页，这里再+1
        parameters = {
            "PageIndex": page_index,
            "PageSize": 100 # 每页包含多少条记录
        }
        r = requests.get(api_url, params=parameters)
        page = json.loads(r.text)
        # print(page)
        print("page index = ",page_index)
        # print("PageCount:", page["PageCount"])

        for row in tqdm(page["DataTable"]):
            # print(row)
            if len(fields) == 0:
                fields = row.keys()
                print(fields)
            file_id = row["FileId"]
            download_fulltext_url = f"http://xxxxxx:8111/WebData/{file_id}.txt"
            save_path = f"downloaded_data/{file_id}.txt"
            if not os.path.exists(save_path):
                try:
                    quick_download_file(download_fulltext_url, save_file_path=save_path)
                except:
                    print("error in downloading file", download_fulltext_url)
            list_model.append(row)
    # 设置保存的文件夹和csv文件名
    quick_save_csv("downloaded_news_list.csv", field_names=fields, list_rows=list_model)
