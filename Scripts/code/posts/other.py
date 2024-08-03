import requests
from bs4 import BeautifulSoup
import csv
import time

# 基础网址
base_url = "https://community.openai.com/top?page={}&per_page=50&period=all"

all_data = []

start_time=time.time()

# 遍历不同的页码
for page_number in range(0,475):
    url = base_url.format(page_number)
    
    # 发送请求
    resp = requests.get(url)
    resp.raise_for_status()
    page_content = resp.text

    # 使用Beautiful Soup解析网页内容
    soup = BeautifulSoup(page_content, "html.parser")

    # 查找所有包含信息的tr块
    topic_items = soup.find_all("tr", class_="topic-list-item")

    for item in topic_items:
        # 提取发布日期
        date = item.find_all("td")[-1].text.strip()

        # 提取浏览数
        views = item.find("td", class_="views").text.strip()

        # 提取回答数
        replies = item.find("td", class_="replies").text.strip()

        # 提取类别名称
        category_name = item.find("span", class_="category-name").text.strip()

        # 提取标签
        tag_links = item.find_all("a", class_="discourse-tag")
        tags = [link.text for link in tag_links]

        # 提取帖子链接
        post_link = item.find("a", class_='title')['href']

        data_dict = {
            "Date": date,
            "Views": views,
            "Replies": replies,
            "Category": category_name,
            "Tags": ", ".join(tags),
            "Post_Link": post_link  
        }

        all_data.append(data_dict)

# 指定保存CSV文件的路径:
csv_file_path = "D:/张广倍大学/张广倍科研/爬虫新_2024.7/新数据/3.csv"

with open(csv_file_path, mode="w", newline='', encoding="utf-8") as f:
    csvwriter = csv.writer(f)

    # 写入表头
    csvwriter.writerow(["Date", "Views", "Replies", "Category", "Tags", "Post_Link"])

    # 写入数据
    for data_dict in all_data:
        csvwriter.writerow(data_dict.values())

over_time=time.time()

print("over!"+str(over_time-start_time))
