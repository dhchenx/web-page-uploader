from quick_crawler.page import *
from carbon2.api.submit import *

if __name__=="__main__":
    # 设置后台服务器的域名和端口
    server_url = "http://xxxx:8111"

    # 这里设置你想抓取的网页地址
    target_url="http://www.news.cn/politics/leaders/2022-01/11/c_1128253361.htm"

    # 1. 产生一个随机、唯一的ID，用来标识每一次上传
    unique_id = uuid.uuid4()
    page_id=str(unique_id)
    print(page_id)

    # 2. 利用爬虫工具获取该网页的HTML文本信息，以{unique_id}.txt命名保存在你的本地电脑，这里{unique_id}是前面生成的ID
    html_str=quick_html_page(target_url)
    f_out=open(f"html_data/{page_id}.txt","w",encoding="utf-8")
    f_out.write(html_str)
    f_out.close()

    # 3. 开始提交该网页的元数据，包括地址、标题等预处理的信息，具体字段及时如下
    root_url=f"{server_url}/api"
    c2api=Carbon2Api(root_url)
    r=c2api.submit_metadata(url=target_url,               # 网页地址
                            title="新华社网站",             # 网页的标题，一般从HTML中提取
                            publisher="新华社",            # 网页的来源，可自定义
                            publishtime="2020-01-02",       # 从网页中提取的文章时间，格式为yyyy-mm-dd HH:mm:ss
                            keywords="关键词1;关键词2",       # 从网页的meta标签提取的关键词或者你自定义的关键词，用分号隔开
                            description="这是一个测试页面",    # 从网页的meta标签提取的描述或者你自定义的描述
                            html="",                        # 默认空，这个默认为空即可，暂时用不到，本意是存储HTML文本，但目前以文件的形式存储，所以这个字段默认为空
                            language="zh",                  # 两位语言代码，地区中使用的两个字符的语言代码是ISO-639代码。
                            uploader="chendonghua",         # 用户的ID，注意：这里需要修改为用户的自己的ID，以便与其他人的数据区分开来
                            baidu_url="",                   # 如果使用百度搜索结果获取的URL，请填充你所使用的百度搜索结果URL
                            search_keywords="",             #如果使用百度搜索结果获取的URL，请填充你所使用的百度关键词
                            tag="测试标签",                   # 个人标签，用于区分某一用户下不同类别的数据，自定义自己的标签，帮助分类
                            file_id=page_id)                # 文件的ID，这个ID必须与以下上传HTML文件代码的ID保持一致
    if r==1: # 如果r=1，则保存元数据成功，继续保存文件；否则，请检查哪些地方出问题，无法继续上传文件
        # 4. 提交该网页的文件，注意：文件命名为{page_id}.txt
        r=c2api.submit_file(f"html_data/{page_id}.txt")

        # 5. 如果上传生成，在域名下的WebData文件夹+{page_id}.txt能找到对应的文件
        download_url=f"{server_url}/WebData/{page_id}.txt"
        if check_url_ok(download_url):
            print("upload successfully")
    else:
        print("无法上传，因为上传网页元数据失败！")

