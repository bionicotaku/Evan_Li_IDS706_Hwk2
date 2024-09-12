import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from mylib.PDFCreator import create_pdf

# Function to calculate statistics
def calculate_stat(data):
    salaryDataDesc = data.describe()
    print(salaryDataDesc)
    return salaryDataDesc

# 读取和处理数据
salaryData = pd.read_csv("Dataset-salary-2024.csv")
columns_to_keep = ['work_year', 'experience_level', 'job_title',
                   'salary_in_usd', 'remote_ratio', 'company_size']
filteredData = salaryData[columns_to_keep]

# 计算统计信息
stats = calculate_stat(filteredData)

# 创建直方图
plt.figure(figsize=(10, 6))
filteredData['salary_in_usd'].hist(bins=50)
plt.title('Distribution of Salaries')
plt.xlabel('Salary')
plt.ylabel('Frequency')

# 保存图表到BytesIO对象
img_buffer = BytesIO()
plt.savefig(img_buffer, format='png')
img_buffer.seek(0)

# 准备文本内容
text_content = f"Filtered Data:\n{filteredData.to_string()}\n\nStatistics:\n{stats.to_string()}"

# 创建PDF
create_pdf("salary_analysis.pdf", text_content, img_buffer)

print("PDF has been created: salary_analysis.pdf")

# from ydata_profiling import ProfileReport
# import pandas as pd

# df = pd.read_csv("trending-books.csv")
# profile = ProfileReport(df, title="Trending Books")
# profile.to_notebook_iframe()
# profile.to_file("books_data.html")