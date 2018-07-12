#-*- coding:utf-8 -*-
import os
import sys
import codecs
import re

def neaten_files(input_dir, output_dir):
	for i, img in enumerate(os.listdir(input_dir)):
		t_dir = str(i//8000)
		if not os.path.exists(output_dir+t_dir):
			os.system('mkdir '+output_dir+t_dir)
		os.system('cp ' + input_dir + img + ' ' + output_dir + t_dir + '/' + img)

if __name__ == '__main__':
	input_dir = '/cephfs/darnellzhou/game_0709/moba/'
	output_dir = '/cephfs/darnellzhou/game_0709/moba_splited/'
        neaten_files(input_dir, output_dir)
