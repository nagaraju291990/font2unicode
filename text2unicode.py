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

en = {}

#map_dic = choose_font()

abcd = open(map_file,"r")
for i in abcd:
	#print(i)
	map_list = i.strip().split()
	#print(map_list)
	if(len(map_list)==2):
		en[map_list[0]]=map_list[1]

en[" "]=" "
en[" "]="इ"
#print(en)
output = open("output.txt","w")

full_char = ['क', 'ख', 'ग', 'घ', 'ड', 'ढ', 'च', 'छ', 'ज', 'झ','ट', 'ठ', 'न', 'ण', 'फ', 'प', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'स', 'श', 'ह', 'त', 'थ', 'द','ध','त्र', 'क्त','क्क','द्ब', 'व','ग्न','द्ध', 'ह्य', 'क्ष', 'ह्र', 'द्म', 'ट', 'त्र', 'श्व', 'श्न','श्र', 'रू', 'ड्य', 'द्भ', 'ढ्य', 'ठ', 'ड्ड', 'ट्ट', 'ट्ठ','ञ्ज', 'ञ्च', 'च्च', 'ज्ज', 'ल्ल', 'ह्न', 'ह्ण', 'ह्ल', 'ह्व', 'ड्ढ', 'ङ्क', 'ङ्ख', 'ङ्ग', 'ङ्घ', 'ङ्क्ष', 'छ्व', 'ज्ञ', 'ळ', 'हृ', 'क्व','ट्व', 'द्र', 'द्ग','श्ल','प्त', 'च्य','द्य' 'ह्म', 'स्त्र', 'ङ', 'ड़','द्द', 'द्ध', 'श्च', 'न्न', 'ऋ','व', 'ठ्य', 'द्न', 'ज़', 'ठ्ठ', 'द्व', 'रु','फ़', 'ष्ट', 'त्त','ष्ठ','ष']
half_char =['्','र्','ळ्','श्','ल्','य्','व्','द्य्','श्र्','त्त्','्ँ','ज्ञ्','ड़्क्त','ज़्','ज्ज्','च्च्','ज्','च्','म्','भ्','ब्','फ्','प्','ध्','थ्','त्','ण्','ञ्','ज्','घ्','ग्','ख्','क्','ह्म्','श्र्','ष्','स्','न्']
matra = ['ु','ू','ि','ी','े','ै','ो','ौ','ँ']
numbers=['1','2','3','4','5','6','7','8','9','0',':','−','/']
special_char=["आ","ो"]

for k in lines:
	#print(k)
	#lang = find_lang(k)
	k = re.sub(r'osQ', 'ds', k)
	k = re.sub(r'oSQ', 'dS', k)
	char = list(k)
	word = ""
	temp, flag =-1, False
	for i in range(0,len(char)):
		#print(len(word))
		if(char[i] in en):
			c =en[char[i]]
			#print(char[i]+" "+c)
			if(c=="ि"):
				rule1 ="ि"
				temp=True
			elif(temp==True and c in full_char):
				#print(word)
				word = word+c+rule1
				#print(word, c, rule1)
				temp=False
			elif(temp==True and en[char[i-1]]=='श्' and c=='ा'):
				word = word[:-2]                    
				word = word+'श'+rule1
				temp=False
			#rule updated by Nagaraju for 
			#input = input : vfHkdkjd;output : अभकिारक;expected output : अभिकारक
			elif(temp==True and en[char[i-1]]=='भ्' and c=='ा'):
				word = word[:-2]                    
				word = word + 'भ' + rule1
				temp=False
			elif(word[-1:] =='ं' and c in matra):
				word = word[:-1]
				word = word+c+'ं'
			elif(c=='र्' and len(word)>=1 and word[-1]!="इ"):
				count =-1
				for i in range(len(word)):
					if(word[count] in full_char):
						word = word[:count]+c+word[count:]
						break
					count=count-1  
			elif(c=="ा" and len(word)>=1 and word[-1] in half_char):
				word=word[:-1]
			elif(c=="े" and len(word)>=1 and word[-1]=="ं"):
				word = word[:-1]+c+word[-1:]
			elif(c=="ै" and len(word)>=1 and word[-1]=="ं"):
				word = word[:-1]+c+word[-1:]
			elif(c=='र्' and len(word)>=1 and word[-1]==' '):
				word=word[:-1]+'ई'
			elif(c=='इ' and len(word)>=1 and word[-1] in numbers ):
				word=word+' '
			else:
				word = word+c
			#print(word)
	word =normalization(word)
	output.write(word+"\n")
