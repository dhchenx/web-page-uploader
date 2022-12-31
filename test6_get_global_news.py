from quick_crawler.multilang import get_sites_with_multi_lang_keywords
import os
# https://www.w3newspapers.com/
# https://www.w3newspapers.com/russia/
keywords="carbon neutrality"

init_urls=[
    ["en-cnn","https://edition.cnn.com/"],
    ['jp-asahi', 'https://www.asahi.com/'],
    ['ru-mk', 'https://www.mk.ru/'],
    ['zh-xinhuanet', 'http://xinhuanet.com/'],
]

current_path = os.path.dirname(os.path.realpath(__file__))

list_item=get_sites_with_multi_lang_keywords(
    current_path=current_path,
    init_urls=init_urls,
    src_term=keywords,
    src_language="en",
    target_langs=["ja","zh","es","ru"],
    save_data_folder="webdata",
    summarize_after_finished=True,
    summary_file_path=f"{current_path}/summarized_data.csv",
    max_num_urls=2000,
    )
