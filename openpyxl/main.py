from openpyxl import load_workbook
from openpyxl import Workbook
# 1、读取数据
workbook = load_workbook("openpyxl/作业-原始成绩.xlsx")
# workbook.sheetnames
print(workbook.sheetnames)
sheet = workbook["Sheet1"]
# sheet.dimensions查看表格的维度
print(sheet.dimensions)
# cell = sheet["A2:G27"]
cell = sheet[sheet.dimensions]
# print(cell)
# 2、提取表格中的数据
y = []
for i in cell:
    x = []
    for j in i:
        x.append(j.value)
        xx = x[:1]+x[4:]
    y.append(xx)

# 新建一个空白的excel表格
workbook = Workbook()
sheet1 = workbook.active
sheet1.title = "表格1"
sheet1.append(["学号", "姓名", "检测", "讨论", "成绩"])
# 数据清洗
for xx in y:
    print(xx)
    try:
        # 提取学号
        xuehao = xx[0][5:13]
        # 提取姓名
        name = xx[0][13:]
        # 提取检测
        test = float(xx[1])
        # 提取套论
        taolun = xx[2]
        if taolun == "-":
            taolun = 0
        else:
            taolun = float(xx[2])
        # 提取成绩
        score = float(xx[3])
        final = [xuehao, name, test, taolun, score]
        # 将最终的数据一行行的写入到excel中
        sheet1.append(final)
    except:
        continue
# 将数据写入到excel后，必须保存，否则前面的操作前功尽弃
workbook.save(filename="openpyxl/作业.xlsx")
