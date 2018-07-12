# -*- coding: UTF-8 -*-
import os
import sys
import codecs

def add_prefix(input_file, output_file):
	writer = codecs.open(output_file, 'w', 'utf-8')
	with codecs.open(input_file, 'r', 'utf-8') as fid:
		lines = fid.read().strip().split('\n')
		for line in lines:
			if len(line.split(' ')) < 2:
				continue
			mp4_path = 'http://100.115.5.36/' + line.split(' ')[0].split('/')[-1].split('.')[0] + '.f0.mp4'
			writer.write(mp4_path+'\n')
	writer.close()

if __name__ == '__main__':
	input_file = '/cephfs/person/brycezhou/VTalentDetect/model/bad_case_caiyi_new.txt'
	output_file = '/cephfs/person/brycezhou/VTalentDetect/model/bad_case_caiyi_chanpin.txt'
	add_prefix(input_file, output_file)
