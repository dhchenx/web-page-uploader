import requests
import json
from quick_crawler.page import quick_html_page,quick_html_object
import pickle
if __name__=="__main__":
    api_url = "http://xxxxxx:8111/api/Data"
    parameters={
        "PageIndex":1,
        "PageSize":20
    }
    r = requests.get(api_url, params=parameters)
    page=json.loads(r.text)
    print("PageCount:",page["PageCount"])
    for row in page["DataTable"]:
        print(row)
        file_id=row["FileId"]
        download_fulltext_url=f"http://xxxxx:8111/WebData/{file_id}.txt"
        html_text=quick_html_page(download_fulltext_url)
        # html_text=get_html_str_with_browser(download_fulltext_url,driver_path="browsers/chromedriver.exe") # this function is slow but is more stable to fetch JavaScript-enabled pages
        # print(html_text)
        # print()
        html_obj=quick_html_object(html_text)
        ps=html_obj.findAll("p")
        for p in ps:
            p_text=p.text
            p_text=p_text.strip()
            p_text=p_text.replace("\n"," ")
            if len(p_text)>10:
                sentences=p_text.split("。")
                for sentence in sentences:
                    if '认为，' in sentence or '提出，' in sentence or '说，' in sentence :
                        print(sentence+"。")
        print()
