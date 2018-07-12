#-*- coding:utf-8 -*-
from sys import argv
import os
import sys
import codecs
import re


def check_argv():
        if len(argv) != 5:
                exit('usage: python caculate_data_multimodel.py <groundtruth_path> <prediction_path> <output_path1> <output_path2>')
        groundtruth_path, prediction_path, output_path1, output_path2 = argv[1:]
        if not os.path.exists(groundtruth_path):
                exit('groundtruth_path does not exist.')
        if not os.path.exists(prediction_path):
                exit('prediction_path does not exist.')
        return groundtruth_path, prediction_path, output_path1, output_path2

def gen_label_list(t_file):
        label_list = []
        with codecs.open(t_file, 'r', 'utf-8') as fid:
                true_lines = fid.read().strip().split('\n')
                for i in range(len(true_lines)):
                        this_line = true_lines[i]
                        true_labels = re.split(',',this_line.strip().split(' ')[1])
                        for true_label in true_labels:
                                if (not true_label in label_list) and true_label != '' and true_label != u'其它':
                                        label_list.append(true_label)
        return label_list

def gen_label_dict(t_file):
        label_dict = {}
        with codecs.open(t_file, 'r', 'utf-8') as fid:
                true_lines = fid.read().strip().split('\n')
                for i in range(len(true_lines)):
                        this_line = true_lines[i]
                        true_labels = re.split(',',this_line.strip().split(' ')[1])
                        for true_label in true_labels:
                                if true_label in label_dict.keys():
                                        label_dict[true_label] += 1
                                else:
                                        label_dict[true_label] = 1
        return label_dict

def gen_gdtruth_dict(true_file):
        gdtruth_dict = {}
        with codecs.open(true_file, 'r', 'utf-8') as fid:
                true_lines = fid.read().strip().split('\n')
                for i in range(len(true_lines)):
                        this_line = true_lines[i]
                        true_labels = re.split(',',this_line.strip().split(' ')[1])
                        mp4_path = this_line.strip().split(' ')[0].split('/')[-1]
                        if not gdtruth_dict.has_key(mp4_path):
                                gdtruth_dict[mp4_path] = true_labels
        return gdtruth_dict

def gen_predict_dict(predict_file):
        predict_dict = {}
        with codecs.open(predict_file, 'r', 'utf-8') as fid:
                predict_lines = fid.read().strip().split('\n')
                for i in range(len(predict_lines)):
                        if len(predict_lines[i].strip().split(' ')) != 2:
                                predict_labels = {}
                                mp4_path = predict_lines[i].strip().split('|')[0].strip().split('/')[-1]
                        else:
                                org_predict_labels = re.split('|',predict_lines[i].strip().split(' ')[1])[0].split('#')
                                predict_labels = {}
                                for label in org_predict_labels:
                                        predict_labels[re.split('@',label)[0]] = re.split('@',label)[1]
                                mp4_path = predict_lines[i].strip().split(' ')[0].split('/')[-1]
                        if not predict_dict.has_key(mp4_path):
                                predict_dict[mp4_path] = predict_labels
        return predict_dict

if __name__ == '__main__':
    true_file, predict_file, output_file, bad_case_file = check_argv()

    label_dict = gen_label_dict(true_file)
    label_list = gen_label_list(true_file)
    gdtruth_dict = gen_gdtruth_dict(true_file)
    predict_dict = gen_predict_dict(predict_file)
    precision_dict = {}
    predict_wrong_dict = {}
    recall_dict = {}
    recall_miss_list = {}
    # count recall
    for mp4 in predict_dict.keys():
        predict_labels = predict_dict[mp4]
        if not gdtruth_dict.has_key(mp4):
            continue
        true_labels = gdtruth_dict[mp4]
        for true_label in true_labels:
            if recall_dict.has_key(true_label):
                recall_dict[true_label][1] += 1
            else:
                recall_dict[true_label] = [0,1]
            if true_label in predict_labels:
                recall_dict[true_label][0] += 1
        for predict_label in predict_labels.keys():
            if precision_dict.has_key(predict_label):
                precision_dict[predict_label][1] += 1
            else:
                precision_dict[predict_label] = [0,1]
            if predict_label in true_labels:
                precision_dict[predict_label][0] += 1
            else:
                wrong_case_line = mp4 + ' '
                for this_label in true_labels:
                    wrong_case_line += this_label+','
                wrong_case_line = wrong_case_line.rstrip(',') + '*'
                for this_label in predict_labels.keys():
                    wrong_case_line += this_label + '@' + predict_labels[this_label] + '#'
                if predict_wrong_dict.has_key(predict_label):
                    predict_wrong_dict[predict_label].append(wrong_case_line.rstrip('#'))#+' '+predict_labels[predict_label])
                else:
                    predict_wrong_dict[predict_label] = [wrong_case_line.rstrip('#')]#+' '+predict_labels[predict_label]]

    for precision_label in precision_dict.keys():
        precision_dict[precision_label] = float(precision_dict[precision_label][0]) / precision_dict[precision_label][1]
    for recall_label in recall_dict.keys():
        recall_dict[recall_label] = float(recall_dict[recall_label][0]) / recall_dict[recall_label][1]

    # write precision and recall
    writer = codecs.open(output_file, 'w','utf-8')
    writer.write('precision:\n')
    for precision_label in label_list:
        if precision_label == u'其它':
                continue
        if not label_dict.has_key(precision_label):
                label_dict[precision_label] = 0
        if not precision_dict.has_key(precision_label):
                precision_dict[precision_label] = 0
        writer.write(precision_label + '\t' + str(precision_dict[precision_label]) + '\t' +  str(label_dict[precision_label]) + '\n')
    writer.write('\nrecall:\n')
    for recall_label in label_list:
        if precision_label == u'其它':
                continue
        if not label_dict.has_key(recall_label):
                label_dict[recall_label] = 0
        if not recall_dict.has_key(recall_label):
                recall_dict[recall_label] = 0
        writer.write(recall_label + '\t' + str(recall_dict[recall_label]) + '\t' + str(label_dict[recall_label]) + '\n')
    writer.close()

    # write bad cases
    writer = codecs.open(bad_case_file, 'w', 'utf-8')
    #writer.write('\n......Predict wrong cases......\n')
    for wrong_label in predict_wrong_dict.keys():
        #writer.write(wrong_label+':\n')
        if wrong_label in label_list:
                writer.write('\n')
                writer.write('predict_err '+wrong_label+'\n')
                for wrong_case in predict_wrong_dict[wrong_label]:
                        writer.write(wrong_case+'\n')
                writer.write('\n')
        else:
                for wrong_case in predict_wrong_dict[wrong_label]:
                        for label in label_list:
                                if label in wrong_case:
                                        writer.write(wrong_case+'\n')
                                        break
    writer.close()

