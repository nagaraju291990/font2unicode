# -*- coding: utf-8 -*-
#import enchant
import sys
import re

from argparse import ArgumentParser

parser = ArgumentParser(description='Text to Unicode \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=inputfie" + " -f=shree|Chanakya"
						)

parser.add_argument("-i", "--input", dest="inputfile",
					help="provide .txt file name",required=True)
parser.add_argument("-m", "--mapping_file", dest="map_file",
					help="mapping file",required=True)

args = parser.parse_args()

inputfile = args.inputfile
map_file = args.map_file

		
def normalization(word):                    #Word Normalization
	word = word.replace('अा','आ')
	word = word.replace('इर्','ई')
	word = word.replace('आे', 'ओ')
	word = word.replace('आै', 'औ')
	word = word.replace('ाै', 'ौ')
	word = word.replace('ाे', 'ो')
	word = word.replace('अो','ओ')
	word = word.replace('अौ', 'औ')
	word = word.replace('एे', 'ऐ')
	word = word.replace('ि्र', '्रि')
	word = word.replace('ि्भ', '्भि')
	word = word.replace('।ं','ं।')
		
	#print("Converting---")
	return word

k = sys.argv    #for command line arguments
			   
f = open(inputfile,"r")     #Opening input file
lines = []
c=0

for line in f:
	if(len(line)>1):
		lines.append(line.rstrip())

map_dict = {}

#map_dic = choose_font()

mappings = open(map_file,"r")
for m in mappings:
	#print(i)
	map_line = m.strip().split()
	#print(map_list)
	if(len(map_line)==2):
		map_dict[map_line[0]]=map_line[1]

map_dict[" "]=" "
map_dict[" "]="इ"
#print(en)
output = open("output.txt","w")

full_char = ['क', 'ख', 'ग', 'घ', 'ड', 'ढ', 'च', 'छ', 'ज', 'झ','ट', 'ठ', 'न', 'ण', 'फ', 'प', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'स', 'श', 'ह', 'त', 'थ', 'द','ध','त्र', 'क्त','क्क','द्ब', 'व','ग्न','द्ध', 'ह्य', 'क्ष', 'ह्र', 'द्म', 'ट', 'त्र', 'श्व', 'श्न','श्र', 'रू', 'ड्य', 'द्भ', 'ढ्य', 'ठ', 'ड्ड', 'ट्ट', 'ट्ठ','ञ्ज', 'ञ्च', 'च्च', 'ज्ज', 'ल्ल', 'ह्न', 'ह्ण', 'ह्ल', 'ह्व', 'ड्ढ', 'ङ्क', 'ङ्ख', 'ङ्ग', 'ङ्घ', 'ङ्क्ष', 'छ्व', 'ज्ञ', 'ळ', 'हृ', 'क्व','ट्व', 'द्र', 'द्ग','श्ल','प्त', 'च्य','द्य' 'ह्म', 'स्त्र', 'ङ', 'ड़','द्द', 'द्ध', 'श्च', 'न्न', 'ऋ','व', 'ठ्य', 'द्न', 'ज़', 'ठ्ठ', 'द्व', 'रु','फ़', 'ष्ट', 'त्त','ष्ठ','ष']
half_char =['्','र्','ळ्','श्','ल्','य्','व्','द्य्','श्र्','त्त्','्ँ','ज्ञ्','ड़्क्त','ज़्','ज्ज्','च्च्','ज्','च्','म्','भ्','ब्','फ्','प्','ध्','थ्','त्','ण्','ञ्','ज्','घ्','ग्','ख्','क्','ह्म्','श्र्','ष्','स्','न्']
matra = ['ु','ू','ि','ी','े','ै','ो','ौ','ँ']
numbers=['1','2','3','4','5','6','7','8','9','0',':','−','/']
special_char=["आ","ो"]

#read input file line by line
for k in lines:
	#print(k)
	#lang = find_lang(k)
	k = re.sub(r'osQ', 'ds', k)
	k = re.sub(r'oSQ', 'dS', k)

	chars = list(k)

	out_line = ''
	for c in chars:
		if c in map_dict:
			out_line += map_dict[c]
		else:
			out_line += c

	out_line = normalization(out_line)
	#to solve ण्ाु

	out_line = re.sub(u'([\u094c\u0902\u0915-\u0939])\u093f([\u0915-\u0939])',r'\1\2ि', out_line)
	out_line = re.sub(u'([\u0902])\u093f([\u0915-\u0939])\u094d([\u0915-\u0939])',u'\u0902\\2\u094d\\3\u093f', out_line)

	out_line = re.sub(u'\u094d\u093E\u0941', u'\u0941', out_line)
	
	out_line = re.sub(u'([ \u0905])\u093f([\u0915-\u0939])',r'\1\2ि', out_line)
	out_line = re.sub(u'^\u093f([\u0915-\u0939])',u'\\1\u093f', out_line)
	out_line = re.sub(u'([\u093E-\u094C])\u093F([\u0915-\u0939])', u'\\1\\2\u093F', out_line)
	out_line = re.sub(u'\u0906\u093F([\u0915-\u0939])\u094D([\u0915-\u0939])', u'\u0906\\1\u094D\\2\u093F', out_line)
	out_line = re.sub(u'([\u0915-\u0939])\u0930\u094D', u'\u0930\u094D\\1', out_line, flags=re.UNICODE)

	out_line = re.sub(u'\u094d\u093E', u'\u093E', out_line)
	out_line = re.sub(u'\u094d\u094B', u'\u094B', out_line)
	out_line = re.sub(u'\u093E\u094B', u'\u094B', out_line)
	out_line = re.sub(u'\u093E\u093E', u'\u093E', out_line)
	out_line = re.sub(u'\u093F\u093E', u'\u093F', out_line)
	out_line = re.sub(u'\u093E\u094C', u'\u094C', out_line)
	out_line = re.sub(u'\u093E\u0940', u'\u0940', out_line)
	out_line = re.sub(u'\u093E\u0942', u'\u0942', out_line)


	out_line = re.sub(u'\u0924\u094D\u0930\u093E', u'\u0924\u094D\u0930', out_line)
	out_line = re.sub(u'([\u0915-\u0939])\u093E\u0930\u094D', u'\u0930\u094D\\1', out_line)

	out_line = re.sub(r'पx0', 'फ', out_line)
	out_line = re.sub(r'1\/4', '\u0926\u094d', out_line)
	out_line = re.sub(r'\u0935\u0947\u0902x0', u'\u0915\u0947\u0902', out_line)
	out_line = re.sub(r'\u0935\u0947\u0902x0', u'\u0915\u0947\u0902', out_line)
	out_line = re.sub(r'\u0935\u0941x0', u'\u0915\u0941', out_line)
	out_line = re.sub(r'([\u0915-\u0939])ोx6', r'\1ों', out_line)
	output.write(out_line+"\n")
