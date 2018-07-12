import codecs
import json

if __name__ == '__main__':
	
	file_path2 = 'F:\\scene_classification\\part_0004_tags.txt'
	file_path1 = 'F:\\scene_classification\\80_tags.txt'
	writer = codecs.open('F:\\scene_classification\\tags_sub.txt', 'w', encoding='utf8')

	with codecs.open(file_path1, 'r') as fid:
		tag1 = fid.readlines()

	with codecs.open(file_path2, 'r') as fid1:
		for tag2 in fid1.readlines():
			if not tag2 in tag1:
				writer.write(json.dumps(tag2.strip('\n'), encoding='UTF-8', ensure_ascii=False).strip('\"') + '\n')
