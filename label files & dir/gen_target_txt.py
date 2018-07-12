# -*- coding: UTF-8 -*-
import os
import sys
import codecs

def get_date(date_str):
        date = ''
        date_list = date_str.split('-')
        for x in date_list[1:]:
                date += x
        return int(date)


def cat_files(begin_date, end_date, input_dir):
        begin_d = get_date(begin_date)
        end_d = get_date(end_date)
        for txt_name in os.listdir(input_dir):
                if txt_name.startswith('category_'):
                        date = get_date(txt_name.split('_')[1].rstrip('.txt'))
                        if date <= end_d and date >= begin_d:
                                input_file = input_dir + txt_name
                                with codecs.open(input_file, 'r','utf-8') as fid:
                                        lines = fid.read().strip().split('\n')
                                        for line in lines:
                                                all_list.append(line)   
        return all_list


def cat_files_simple(input_dir):
        all_list = []
        for txt_name in os.listdir(input_dir):
                if txt_name.startswith('category_'):
                        input_file = input_dir + txt_name
                        with codecs.open(input_file, 'r','utf-8') as fid:
                                lines = fid.read().strip().split('\n')
                                for line in lines:
                                        all_list.append(line)
        
        return all_list


def gen_dict(input_file):
	re_dict = []
	with open(input_file, 'r') as fid:
		for line in fid.readlines():
			re_dict.append([line.strip().split(' ')[0], line.strip().split(' ')[1]])
	return re_dict


def find_target(input_dir, output_dir, config_file, begin_date, end_date):
        if begin_date == None or end_date == None:
                all_lines = cat_files_simple(input_dir)
        else:
                all_lines = cat_files(begin_date, begin_date, input_dir)
        target_dict = gen_dict(config_file)
        for t in target_dict:
                writer = codecs.open(output_dir + t[0] +'.txt', 'w', 'utf-8')
                for i, line in enumerate(all_lines):
                        if len(line.split(' ')) < 2:
                                continue
                        mp4_path = line.split(' ')[0]
                        labels = line.split(' ')[1]
                        for x in t[1].split(','):
                                if x.decode('utf-8') in labels:
                                        writer.write(line+'\n')
                                        all_lines[i] = ''
                                        break
                writer.close()

if __name__ == '__main__':
        input_dir = '/cephfs/weishi/cate_tags_file_0607/'
        output_dir = '/cephfs/darnellzhou/tools/find_target_test/'
        config_file = '/cephfs/darnellzhou/tools/find_target_test/game_config.txt'
        begin_date = None # should be s string
        end_date = None
        find_target(input_dir, output_dir, config_file, begin_date, end_date)

