#-*- coding:utf-8 -*-
import os
import sys
import codecs
import re

def gen_list(t_file):
	with codecs.open(t_file, 'r','utf-8') as fid:
		t_list = fid.read().strip().split('\n')
	return t_list

def project_relations_single(input_file, output_file, project_file):
	project_list = gen_list(project_file)
	writer = codecs.open(output_file, 'w', 'utf-8')
	with codecs.open(input_file, 'r','utf-8') as fid:
		for line in fid.read().strip().split('\n'):
			if len(line.split(' ')) < 2:
				continue
			mp4_path = line.split(' ')[0]
			labels = line.split(' ')[1].split(',')
			tmp_str = ''
			for label in labels:
				for x in project_list:
					if label in x:
						tmp_str += x + ','
						break

			writer.write(mp4_path+' '+tmp_str.rstrip(',')+'\n')
	writer.close()

def gen_dict(input_file):
	re_dict = {}
	with codecs.open(input_file, 'r','utf-8') as fid:
		for line in fid.read().strip().split('\n'):
			re_dict[line.split('\t')[0]] = line.split('\t')[1]
	return re_dict

def project_relations(input_file, output_file, project_file):
	project_dict = gen_dict(project_file)
	writer = codecs.open(output_file, 'w', 'utf-8')
	with codecs.open(input_file, 'r','utf-8') as fid:
		for line in fid.read().strip().split('\n'):
			if len(line.split(' ')) < 2:
				continue
			mp4_path = line.split(' ')[0]
			labels = line.split(' ')[1].split(',')
			tmp_str = ''
			for label in labels:
				if label in project_dict:
					tmp_str += project_dict[label] + ','
					break
			writer.write(mp4_path+' '+tmp_str.rstrip(',')+'\n')
	writer.close()

if __name__ == '__main__':
	input_file = '/cephfs/share/data/zhancheng/zhou/58_obj_check_erhu.txt'
	output_file = '/cephfs/share/data/zhancheng/zhou/new_58_obj_check_erhu.txt'
	project_file = '/cephfs/share/data/zhancheng/zhou/0711_project.txt'
        project_relations_single(input_file, output_file, project_file)
