import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time

start_time=time.time()

def remove_code_tags(soup):
    for pre_code_tag in soup.select('pre code'):
        if pre_code_tag.text.strip():  # Check if <code> tag has content
            pre_code_tag.decompose()  # Remove the <pre><code> block

def remove_media_tags(soup):
    media_tags = soup.select('img, video, audio')
    for media_tag in media_tags:
        media_tag.decompose()

def extract_content(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"网络请求错误: {e}")
        return None, None

    page_content = resp.text
    soup = BeautifulSoup(page_content, 'html.parser')

    # Remove <pre><code> tags with content
    remove_code_tags(soup)

    # Remove media tags (img, video, audio)
    remove_media_tags(soup)

    # 提取问题描述：
    post_content = soup.find('div', class_='post', itemprop='articleBody')
    post_text = post_content.text.strip() if post_content else "未知"

    # 提取时间：
    published_time_match = re.search(r'<meta property="article:published_time" content="(\d{4}-\d{2}-\d{2})', page_content)
    published_time = published_time_match.group(1) if published_time_match else "未知"

    return post_text, published_time

# 读取原始的 xls 文件
input_file_path = "D:/张广倍大学/张广倍科研/爬虫新_2024.7/新数据/全部网址.xls"
df = pd.read_excel(input_file_path, header=None, names=['网址'])

# 初始化新的 DataFrame 用于保存提取的内容
result_df = pd.DataFrame(columns=['问题描述', '发布时间'])

# 对每个网址进行提取
for url in df['网址']:
    post_text, published_time = extract_content(url)
    result_df = pd.concat([result_df, pd.DataFrame({'问题描述': [post_text], '发布时间': [published_time]})], ignore_index=True)

# 合并原始 DataFrame 和新的 DataFrame，并保存到新的 xlsx 文件
result_df = pd.concat([df, result_df], axis=1)
result_file_path = "D:/张广倍大学/张广倍科研/爬虫新_2024.7/新数据/全部.xlsx"
result_df.to_excel(result_file_path, index=False)

end_time=time.time()
print("over!"+str(end_time-start_time))
