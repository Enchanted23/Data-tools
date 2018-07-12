# -*- coding:utf-8 -*-
import datetime
import time
import os
import sys
import codecs
import xlwt # 需要的模块

def txt2xls(filename, xlsname):  # 文本转换成xls的函数，filename 表示一个要被转换的txt文本，xlsname 表示转换后的文件名
    print 'converting .txt to .xls ... '
    x = 0                # 在excel开始写的位置（y）
    xls=xlwt.Workbook()
    sheet = xls.add_sheet('sheet1',cell_overwrite_ok=True) # 生成excel的方法，声明excel
    with codecs.open(filename, 'r', encoding='utf8') as fid:
        lines = fid.readlines()

        for line in lines:
        	elements = line.split('\t')
        	for i in range(len(elements)):
        		sheet.write(x, i, elements[i])
        	x += 1 #另起一行

    xls.save(xlsname)
    print 'converting finished!'

if __name__ == "__main__":
    filename = 'F:\\scene_classification\\dog_bad.txt'
    #filename_1 = 'F:\\scene_classification\\0502_tags_freq.txt'
    xlsname  = 'F:\\scene_classification\\dog_bad.xls'
    #xlsname_1  = 'F:\\scene_classification\\0502_tags_freq.xls'
    txt2xls(filename,xlsname)
    #txt2xls(filename_1,xlsname_1)