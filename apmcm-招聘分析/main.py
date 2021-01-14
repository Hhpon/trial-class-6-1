from openpyxl import load_workbook
from openpyxl import Workbook


def read_demand(dir, first_level_dir, file):
    workbook = load_workbook('%s%s/%s' % (dir, first_level_dir, file))
    sheet = workbook[workbook.sheetnames[0]]
    cells = sheet[sheet.dimensions]
    demand_lists = []
    print(cells.len())
    cells.pop()
    # for row in cells:
    #     for cell in row:
            # print(cell.value)
            
    print(sheet.dimensions)


def main():
    dir = 'apmcm-招聘分析/market-demand/'
    first_level_dir = '2015'
    file = '09.xlsx'
    read_demand(dir, first_level_dir, file)


if __name__ == "__main__":
    main()
