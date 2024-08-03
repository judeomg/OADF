import pandas as pd

# 读取Excel文件
input_file_path = "D:/张广倍大学/张广倍科研/爬虫新_2024.7/新数据/123.xls"
output_file_path = "D:/张广倍大学/张广倍科研/爬虫新_2024.7/新数据/456.xls"

df = pd.read_excel(input_file_path, header=None)

# 在第一列中删除指定的文本和将 "-" 替换成空格
df[0] = df[0].str.replace('https://community.openai.com/t/', '')
df[0] = df[0].str.replace('/\d+', '', regex=True)
df[0] = df[0].str.replace('-', ' ')  # 将所有的 "-" 替换成空格

# 保存到新的Excel文件
df.to_excel(output_file_path, index=False, header=False, engine='openpyxl')  # 使用openpyxl引擎
print("over!")