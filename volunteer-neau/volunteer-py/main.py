from openpyxl import load_workbook
from openpyxl import Workbook
import os
import pymongo

client = pymongo.MongoClient(host='localhost')
db = client['trial-class']
collection = db['volunteer']


def read_volunteer(root_dir, first_level_dir, file):
    workbook = load_workbook('%s/%s/%s' % (root_dir, first_level_dir, file))
    sheet = workbook[workbook.sheetnames[0]]
    cells = list(sheet[sheet.dimensions])

    keys = list(map(lambda cell: cell.value, cells[:1][0]))
    volunteers = []

    for row in cells[1:]:
        if row[0].value:
            values = list(map(lambda cell: cell.value, row))
            volunteer_info = dict(zip(keys, values))
        else:
            volunteer_info = volunteers[len(volunteers) - 1]
            volunteer_info['服务项目名称'] = row[7].value
            volunteer_info['单项时长'] = row[8].value
        volunteers.append(volunteer_info)
    print(volunteers)
    return volunteers


def save_volunteer(volunteer_info):
    if isinstance(volunteer_info, list):
        print('volunteer 是 list')
        collection.insert_many(volunteer_info)
    else:
        collection.insert_one(volunteer_info)


def main():
    root_dir = 'volunteer-neau/volunteer-py/volunteer-info'
    first_level_dir = '青站'
    file = '电信青站第十周时间记录表.xlsx'
    volunteers = read_volunteer(root_dir, first_level_dir, file)
    save_volunteer(volunteers)
    print(volunteers)


if __name__ == "__main__":
    main()