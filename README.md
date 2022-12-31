## 网页数据抓取及上传接口使用案例

1. 首先需要安装以下Python包，这个案例代码我推荐使用Pycharm和Python 3.6+开发

```
pip install quick-crawler carbon2
```

2. 示例代码介绍：

### test_submit_a_web_page.py
从本地电脑抓取一个网页，然后上传到我们的服务器

### test2_submit_a_list_from_csv_file.py
从本地电脑的csv文件中获取一系列URL，并上传到服务器

### test3_submit_a_list_from_urls.py
给定一组URL，爬取后上传到服务器

### test4_fetch_downloaded_pages.py
获取某一页的系统网页数据，并下载下来作基本的处理

### test5_download_all_data.py
分页下载系统中所有的网页原始文件数据，并将元数据保存为csv文件

### test6_get_global_news.py
根据指定的网站和语种，按照关键词搜索相关网页

3. 注意事项

- 提交网页数据时传入的用户ID需要是本人的用户ID，方便后面的数据管理，比如可以批量下载/删除某些特定用户的数据；
- 提交每一份相关的数据（比如，单个网站的数据），需要设置一个唯一的标签Tag，这样可以区分不同用户下的不同类别数据；
- 这里面上传的URL必须是唯一的，也就是说，如果系统已经存在URL了，则其他用户无法上传同一个网址的数据。