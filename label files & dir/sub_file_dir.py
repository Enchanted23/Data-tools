# -*- coding: UTF-8 -*-
import os
import sys
import codecs

def gen_sublist_by_file(sub_file):
	sub_list = []
	with codecs.open(input_file, 'r', 'utf-8') as fid:
		lines = fid.read().strip().split('\n')
		for line in lines:
			mp4_path = line.split(' ')[0].split('.')[0].split('/')[-1]
			sub_list.append(mp4_path)
	return sub_list

def gen_sublist_by_dir(sub_dir):
	sub_list = set()
	for img in os.listdir(sub_dir):
		mp4_path = img.split('.')[0]
		sub_list.add(mp4_path)
	return sub_list

def exec_sub(input_file, sub_dir, output_file):
	sub_list = gen_sublist_by_dir(sub_dir)
	writer = codecs.open(output_file, 'w', 'utf-8')
	with codecs.open(input_file, 'r', 'utf-8') as fid:
		lines = fid.read().strip().split('\n')
		for line in lines:
			mp4_path = line.split(' ')[0]
			mp4 = mp4_path.split('/')[-1].split('.')[0]
			if mp4 in sub_list:
				continue
			writer.write(line+'\n')
	writer.close()

if __name__ == '__main__':
	input_file = '/cephfs/darnellzhou/game_0709/moba.txt'
	#sub_file = ''
	sub_dir = '/cephfs/darnellzhou/game_0709/moba/'
	output_file = '/cephfs/darnellzhou/game_0709/moba_1.txt'
	exec_sub(input_file, sub_dir, output_file)
