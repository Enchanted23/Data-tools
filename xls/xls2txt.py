# -*- coding:utf-8 -*-
import datetime
import time
import os
import sys
import codecs
import json
import xlrd # 需要的模块

def txt2xls(filename, xlsname):  # xls转换成文本的函数，xlsname 表示一个要被转换的xls，filename 表示转换后的文件名
    print 'converting .xls to .txt ... '
    x = 0                # 在excel开始写的位置（y）
    xls=xlrd.open_workbook(xlsname, encoding_override="utf_8")
    table = xls.sheets()[0] # #通过索引顺序获取

    with codecs.open(filename, 'w', encoding='utf8') as fid:
        for i in range(table.nrows):
            for j in range(3):
                fid.write(json.dumps(table.cell(i,j).value, encoding='UTF-8', ensure_ascii=False).strip('\"'))
                fid.write('\t')
            fid.write(json.dumps(table.cell(i,3).value, encoding='UTF-8', ensure_ascii=False).strip('\"'))
            fid.write('\n')

    print 'converting finished!'

if __name__ == "__main__":
    filename = 'F:\\scene_classification\\0502_tags.txt'
    xlsname  = 'F:\\scene_classification\\0502_tags.xls'
    txt2xls(filename,xlsname)