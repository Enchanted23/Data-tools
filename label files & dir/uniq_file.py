import os
import sys
import codecs
import random

if __name__ == '__main__':
    input_file = '/cephfs/darnellzhou/game_0709/other.txt'
    output_file = '/cephfs/darnellzhou/game_0709/other_uniq.txt'
    writer = codecs.open(output_file, 'w','utf-8')
    mp4_set = []
    with codecs.open(input_file, 'r','utf-8') as fid:
        for line in fid.read().strip().split('\n'):
                mp4_path = line.split(' ')[0]
                if not (mp4_path in mp4_set):
                        writer.write(line+'\n')
                        mp4_set.append(mp4_path)
    writer.close()
