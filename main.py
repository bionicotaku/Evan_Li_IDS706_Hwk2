import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from mylib.PDFCreator import create_pdf


def calculate_stat(data):
    salaryDataDesc = data.describe()
    print(salaryDataDesc)
    return salaryDataDesc


salaryData = pd.read_csv("Dataset-salary-2024.csv")
columns_to_keep = [
    "work_year",
    "experience_level",
    "job_title",
    "salary_in_usd",
    "remote_ratio",
    "company_size",
]
filteredData = salaryData[columns_to_keep]

stats = calculate_stat(filteredData)

# create a histogram of the salary data
plt.figure(figsize=(10, 6))
filteredData["salary_in_usd"].hist(bins=50)
plt.title("Distribution of Salaries")
plt.xlabel("Salary")
plt.ylabel("Frequency")

# save the plot to a buffer
img_buffer = BytesIO()
plt.savefig(img_buffer, format="png")
img_buffer.seek(0)

# prepare the text content
text_content = f"Statistics:\n{stats.to_string()}"
# create the PDF file
create_pdf("salary_analysis.pdf", text_content, img_buffer)

print("PDF has been created: salary_analysis.pdf")
