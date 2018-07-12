# -*- coding: UTF-8 -*-
from sys import argv
import os
import sys
import codecs
import re

def check_argv():
    if len(argv) != 6:
        exit('usage: python gen_gdtruth.py <begin_date> <end_date> <project_file_path> <input_file_dir> <output_file_path>')
    begin_date, end_date, project_file, input_dir, output_file = argv[1:]
    if not os.path.exists(input_dir):
        exit('input_file_dir does not exist.')
    if not os.path.exists(project_file):
        exit('project_file_path does not exist.')
    return begin_date, end_date, project_file, input_dir, output_file

def get_date(date_str):
	date = ''
	date_list = date_str.split('-')
	for x in date_list[1:]:
		date += x
	return int(date)

def gen_dict(input_file):
	re_dict = {}
	with codecs.open(input_file, 'r','utf-8') as fid:
		for line in fid.read().strip().split('\n'):
			re_dict[line.split('\t')[0]] = line.split('\t')[1]
	return re_dict

def cat_files(begin_date, end_date, input_dir, tmp_gd_dir, tmp_gd_name):
	begin_d = get_date(begin_date)
	end_d = get_date(end_date)
	if not os.path.exists(tmp_gd_dir):
		os.system('mkdir ' + tmp_gd_dir)
	writer = codecs.open(tmp_gd_dir+tmp_gd_name, 'w', 'utf-8')
	for txt_name in os.listdir(input_dir):
    	        if txt_name.startswith('category_'):
    		        date = get_date(txt_name.split('_')[1].rstrip('.txt'))
    		        if date <= end_d and date >= begin_d:
    			        input_file = input_dir + txt_name
    			        with codecs.open(input_file, 'r','utf-8') as fid:
                                        writer.write(fid.read().strip()+'\n')
        writer.close()

def project_relations(input_file, output_file, project_file):
	project_dict = gen_dict(project_file)
	writer = codecs.open(output_file, 'w', 'utf-8')
	with codecs.open(input_file, 'r','utf-8') as fid:
		for line in fid.read().strip().split('\n'):
			if len(line.split(' ')) < 2:
				continue
			mp4_path = line.split(' ')[0]
			labels = line.split(' ')[1].split(',')
                        flag = 0
			for label in labels:
				if label in project_dict:
					writer.write(mp4_path+' '+project_dict[label]+'\n')
					flag = 1
                                        break
			if not flag:
                                        writer.write(mp4_path+' '+u'其它'+'\n')
	writer.close()

if __name__ == '__main__':
	begin_date, end_date, project_file, input_dir, output_file = check_argv()
	tmp_gd_dir = './tmp_groundtruth/'
	tmp_gd_name = begin_date+'-'+end_date+'_tmp_gdtruth.txt'
        if not os.path.exists(tmp_gd_dir+tmp_gd_name):
                cat_files(begin_date, end_date, input_dir, tmp_gd_dir, tmp_gd_name)
        project_relations(tmp_gd_dir+tmp_gd_name, output_file, project_file)

