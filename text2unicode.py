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

def regexRules(tmp_line):
		#shift choti i maatra to end when it is prepended with consonant or  ou matra  or aM and followed by any consonant
	tmp_line = re.sub(u'([\u094c\u0902\u0915-\u0939])\u093f([\u0915-\u0939])',r'\1\2ि', tmp_line)

	#shifit choti i maatra to end when it is prepended by aM and followed by consonant and virama and consotant
	tmp_line = re.sub(u'([\u0902])\u093f([\u0915-\u0939])\u094d([\u0915-\u0939])',u'\u0902\\2\u094d\\3\u093f', tmp_line)

	#shift choti i maatra to end when क ि ्  र with क ् र ि 
	tmp_line = re.sub(u'([\u0915-\u0939])\u093f\u094D([\u0915-\u0939])', u'\\1\u094D\\2\u093f', tmp_line)

	#replace ु ् ा with  ा
	tmp_line = re.sub(u'\u094d\u093E\u0941', u'\u0941', tmp_line)
	
	#shifting choti i maatra to end when line begins with space of vowel a 
	tmp_line = re.sub(u'([ \u0905])\u093f([\u0915-\u0939])',r'\1\2ि', tmp_line)

	#shifting choti i maatra when it is directly in the begging of consonant
	tmp_line = re.sub(u'^\u093f([\u0915-\u0939])',u'\\1\u093f', tmp_line)

	#shifitng choto i maatra to a consonant when it is followed by a vowel mfpr => उिचत => उचित
	tmp_line = re.sub(u'([\u0905-\u0914])\u093f([\u0915-\u0939])',u'\\1\\2\u093F', tmp_line)

	#shifting choti i maatra between two consonants
	tmp_line = re.sub(u'([\u093E-\u094C])\u093F([\u0915-\u0939])', u'\\1\\2\u093F', tmp_line)

	#shifting choti i maatra when followed by long vowel A and with pattern CViramaC
	tmp_line = re.sub(u'\u0906\u093F([\u0915-\u0939])\u094D([\u0915-\u0939])', u'\u0906\\1\u094D\\2\u093F', tmp_line)

	#consonat followed by letter ra followed by virama, shift the consonat to end
	tmp_line = re.sub(u'([\u0915-\u0939])\u0930\u094D', u'\u0930\u094D\\1', tmp_line, flags=re.UNICODE)

	#consonant followed by choti i matra and virama then letter r move i maatra after cosonant halant consoant कि्रया to क्रिया
	tmp_line = re.sub(u'([\u0915-\u0939])\u093F\u094d([\u0915-\u0939])', u'\\1\u094D\\2\u093F', tmp_line)

	

	#below are rules to normalize two dependent vowels occuring side by side
	tmp_line = re.sub(u'\u094d\u093E', u'\u093E', tmp_line)
	tmp_line = re.sub(u'\u094d\u094B', u'\u094B', tmp_line)
	tmp_line = re.sub(u'\u093E\u094B', u'\u094B', tmp_line)
	tmp_line = re.sub(u'\u093E\u093E', u'\u093E', tmp_line)
	tmp_line = re.sub(u'\u093F\u093E', u'\u093F', tmp_line)
	tmp_line = re.sub(u'\u093E\u094C', u'\u094C', tmp_line)
	tmp_line = re.sub(u'\u093E\u0940', u'\u0940', tmp_line)
	tmp_line = re.sub(u'\u093E\u0942', u'\u0942', tmp_line)


	# to replace त ् र ा with त ् र
	tmp_line = re.sub(u'\u0924\u094D\u0930\u093E', u'\u0924\u094D\u0930', tmp_line)

	# to replace consonant followed by  ा र ् with र ् consonant
	tmp_line = re.sub(u'([\u0915-\u0939])\u093E\u0930\u094D', u'\u0930\u094D\\1\u093E', tmp_line)

	#post processing rules
	tmp_line = re.sub(r'पx0', 'फ', tmp_line)
	tmp_line = re.sub(r'1\/4', '\u0926\u094d', tmp_line)
	tmp_line = re.sub(r'\u0935\u0947\u0902x0', u'\u0915\u0947\u0902', tmp_line)
	tmp_line = re.sub(r'\u0935\u0947\u0902x0', u'\u0915\u0947\u0902', tmp_line)
	tmp_line = re.sub(r'\u0935\u0941x0', u'\u0915\u0941', tmp_line)
	tmp_line = re.sub(r'([\u0915-\u0939])ोx6', u'\u0930\u094D\\1ों', tmp_line)
	return tmp_line		

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

#read input file line by line
for k in lines:
	#print(k)
	#lang = find_lang(k)

	#to solve - input=fo"k;ksa;output=विषायों
	k = re.sub(r'\"k', u"\u0937", k)
	#to solve .k (णा) 
	k = re.sub(r'\.k', u'\u0923',k)

	k = re.sub(r'osQ', 'ds', k)
	k = re.sub(r'oSQ', 'dS', k)

	
	#LokLFk => स्वास्था => स्वास्थ
	#k = re.sub(r'Fk', u'\u0925', k)



	#convert current line into a list of characters
	chars = list(k)

	out_line = ''
	#get mapping values of each input character in the current line
	for c in chars:
		#print(c, map_dict[c])
		if c in map_dict:
			out_line += map_dict[c]
		else:
			out_line += c


	#after immediate mapping replacement, apply consonant virama aa matra rule to make it full character
	out_line = re.sub(r'([\u0915-\u0939])\u094D\u093E' , u'\\1', out_line)
	#print(out_line)
	#to solve FkksZ => थोर् => र्थो		
	out_line = re.sub(u'([\u0915-\u0939])\u093E\u0947\u0930\u094D', u'\u0930\u094D\\1\u094B' ,out_line)
	
	out_line = normalization(out_line)
	#to solve ण्ाु

	out_line = regexRules(out_line)


	output.write(out_line+"\n")
