# -*- coding:utf-8 -*-
import codecs
import json

if __name__ == '__main__':

    file_path = 'F:\\scene_classification\\part_0004_result.txt'
    writer = codecs.open('F:\\scene_classification\\part_0004_tags_freq.txt', 'w', encoding='utf8')
    writer_1 = codecs.open('F:\\scene_classification\\part_0004_tags.txt', 'w', encoding='utf8')

    tags_dict = {}
    with codecs.open(file_path, 'r', encoding='utf8') as fid:
        lines = fid.readlines()

        for line in lines:
            splits = line.split(' ')[1].split('+')

            for tag_pair in splits:
                if len(tag_pair.split(':')) != 2:
                    continue
                [tag, tag_conf] = tag_pair.split(':')
                if tags_dict.has_key(tag):
                    tags_dict[tag] = tags_dict[tag]+1
                else:
                    tags_dict[tag] = 1
                    writer_1.write(tag+'\n')

    for tag in tags_dict.keys():
        writer.write(json.dumps(tag, encoding='UTF-8', ensure_ascii=False) + ' ' + str(tags_dict[tag]) + '\n')

    writer.close()
    writer_1.close()