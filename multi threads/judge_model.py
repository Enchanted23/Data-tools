# -*- coding: UTF-8 -*-
import os

############################ 1. generate groundtruth
# 是否已经生成 groundtruth 文件
gt_flag = '0'
# 作为测试文件的起始日期
begin_date = '2018-06-07'
end_date = '2018-06-25'
# 关系映射文件地址
project_file = ''
# 存放测试文件的目录
test_dir = ''
# 第一步生成的groundtruth文件
gt_file = ''
############################ 2. split input file
# 是否已经将输入文件分割
split_flag = '1' # 0 means not splited, 1 means splited
# 存放分割后的文件的文件夹
tmp_dir = './tmp_input_data/'
# 线程数
k = '32'
############################ 3. test samples using our model
# 是否已经测试过模型
test_flag = '1'
# 运行的cpp文件
cpp_name = './BatchRun'
# 模型路径
model_path = './model/VideoLabel.xbin'
# 预测结果输出文件夹
predict_dir = './06_28/'
# 预测结果整合后的文件
predict_file = './06_28_game_out.txt'
############################ 3. calculate precision and recall & get bad cases
# 存放 precision 和 recall 的文件路径
output_file = './prec_recall_game.txt'
# 存放 bad case 的文件路径
bad_case_file = './bad_case_game.txt'

if gt_flag == '0':
    os.system('python gen_gdtruth.py '+begin_date+' '+end_date+' '+project_file+' '+test_dir+' '+gt_file)
if split_flag == '0':
    os.system('python split_input.py '+k+' '+gt_file+' '+tmp_dir)
if test_flag == '0':
    os.system('python multi_thread_test.py '+tmp_dir+' '+k+' '+cpp_name+' '+ model_path+' '+gt_file+' '+predict_dir)
    # cat files in predict_dir
    os.system('find '+predict_dir+ ' -type f -exec cat {} \;>'+predict_file)
os.system('python caculate_data_multimodel.py '+gt_file+' '+predict_file+' '+output_file+' '+bad_case_file)
