
# -*- coding:utf8 -*-

import re


#chia doan van thanh list cac text dua tren cac chi so bat dau cua cac doan trong array
def split(string,array):
	result = []
	for i in range(0,len(array)) :
		if(i != (len(array)-1)) :
			result.append(string[array[i]:array[i+1]])
		else:
			result.append(string[array[i]:(len(string)-1)])
	return result	
#sua lai gia tri bat dau cho cac index trong array
def check(string,array):
	for i in range(0,len(array)) :
		if(string[(array[i]-2):array[i]] == "**"):
			array[i] = array[i]-2
	return array
#check xem trong dong chua tu do co in dam hay ko (**xxx**)
def reFind(string,array):
	for i in range(0,len(array)):
		count = 0;
		tempInt = array[i] - 2
		tempC = string[tempInt]
		while tempC != '\n':
			if (tempC == '*'):
				count += 1
			tempInt += 1
			tempC = string[tempInt]
		if count < 2 :
			del array[i]
	return array
#do dai cua list
def lenIterator(list):
	sum = 0
	for i in list :
		sum += 1
	return sum

#Chia theo phan
def divPart(string):
	limitText = len(string)
	partIndex = []
	it = re.finditer(r"(\*\*Phần thứ (\w|\s)*(\*\*|))", string)
	if lenIterator(it) > 0 :
		it = re.finditer(r"(\*\*Phần thứ (\w|\s)*(\*\*|))", string)
		for match in it:
		    partIndex.append(match.span()[0])
		result = {
			"totalPart": len(partIndex),
			"parts" : ""
		}
		listParts = []

		for i in range(0,len(partIndex)):
			if i!=(len(partIndex)-1):
				part = {
					"start":partIndex[i],
					"end": (partIndex[i+1]),
					"totalChap": "",
					"chaps": ""
				}
				res = divChapter(string[partIndex[i]:partIndex[i+1]],partIndex[i])
				part['chaps'] = res[0]
				part['totalChap'] = res[1]
				listParts.append(part)
			else :
				part = {
					"start":partIndex[i],
					"end": limitText,
					"totalChap": "",
					"chaps": ""
				}
				res = divChapter(string[partIndex[i]:limitText],partIndex[i])
				part['chaps'] = res[0]
				part['totalChap'] = res[1]
				listParts.append(part)
		result['[parts'] = listParts
	else :
		result = {
			"totalPart": 0,
			"parts" : ""
		}
		listParts = []
		part = {
					"start": 0,
					"end": len(string),
					"totalChap": "",
					"chaps": ""
				}
		res = divChapter(string,0)
		part['chaps'] = res[0]
		part['totalChap'] = res[1]
		listParts.append(part)
	result['parts'] = listParts
	return result

#Chia theo chuong
def divChapter(string, startIndex) :
	it = re.finditer(r"(\*\*Chương\s.*\*\*)", string)
	chapterIndex = [] #chuoi cac index bat dau cua cac chapter
	listChaps = []
	sum =  0
	a = lenIterator(it)
	if  a >0:
		it = re.finditer(r"(\*\*Phần thứ (\w|\s)*(\*\*|))", string)
		sum = a
		for match in it:
		    chapterIndex.append(match.span()[0])
		for j in range(0,len(chapterIndex)):
			if j!=(len(chapterIndex)-1):
				chap = {
					"start":(chapterIndex[j]+startIndex),
					"end": (chapterIndex[j+1]+startIndex),
					"totalSec": "",
					"secs": ""
				}
				res = divSection(string[chapterIndex[i]:chapterIndex[j+1]],chapterIndex[j]+startIndex)
				chap['secs'] = res[0]
				chap['totalSec'] = res[1]
				listChaps.append(chap)
			else :
				chap = {
					"start":chapterIndex[j]+startIndex,
					"end": len(string)+startIndex,
					"totalSec": "",
					"secs": ""
				}
				res = divSection(string[chapterIndex[j]:len(string)],chapterIndex[j]+startIndex)
				chap['secs'] = res[0]
				chap['totalSec'] = res[1]
				listChaps.append(chap)
	else :
		chap = {
					"start": startIndex ,
					"end": startIndex+len(string),
					"totalSec": "",
					"secs": ""
				}
		res = divSection(string,startIndex)
		chap['secs'] = res[0]
		chap['totalSec'] = res[1]
		listChaps.append(chap)
	resultlist = []
	resultlist.append(listChaps)
	resultlist.append(sum)
	return resultlist	

#Chia theo muc
def divSection(string, startIndex):
	it = re.finditer(r"(\*\*Mục\s.*\*\*)", string)
	sectionIndex = []
	listSecs = []
	sum = 0
	a = lenIterator(it)
	if a>0:
		sum = a
		it = re.finditer(r"(\*\*Mục\s.*\*\*)", string)
		for match in it:
		    sectionIndex.append(match.span()[0])
		for j in range(0,len(sectionIndex)):
			if j!=(len(sectionIndex)-1):
				sec = {
					"start":(sectionIndex[j]+startIndex),
					"end": (sectionIndex[j+1]+startIndex),
					"totalLaw": "",
					"laws": ""
				}
				res = divideLaw(string[chapterIndex[i]:chapterIndex[j+1]],chapterIndex[j]+startIndex)
				sec['laws'] = res[0]
				sec['totalLaw'] = res[1]
				listSecs.append(sec)
			else :
				sec = {
					"start":sectionIndex[j]+startIndex,
					"end": len(string) +startIndex,
					"totalLaw": "",
					"laws": ""
				}
				res = divideLaw(string[sectionIndex[j]:len(string)],sectionIndex[j]+startIndex)
				sec['laws'] = res[0]
				sec['totalLaw'] = res[1]
				listSecs.append(sec)
	else :
		sec = {
					"start": startIndex,
					"end": startIndex+len(string),
					"totalLaw": "",
					"laws": ""
				}
		res = divideLaw(string,startIndex)
		sec['laws'] = res[0]
		sec['totalLaw'] = res[1]
		listSecs.append(sec)
	resultlist = []
	resultlist.append(listSecs)
	resultlist.append(sum)
	return resultlist

#chia theo dieu
#dont need change name variable
def divideLaw(string,startIndex):
	it = re.finditer(r"(\*\*Điều [0-9]*(\.|)\*\*)", string)
	sectionIndex = []
	listSecs = []
	sum = 0
	a = lenIterator(it)
	if a>0:
		sum = a
		it = re.finditer(r"(\*\*Mục\s.*\*\*)", string)
		for match in it:
		    sectionIndex.append(match.span()[0])
		for j in range(0,len(sectionIndex)):
			if j!=(len(sectionIndex)-1):
				sec = {
					"start":(sectionIndex[j]+startIndex),
					"end": (sectionIndex[j+1]+startIndex)
				}
				listSecs.append(sec)
			else :
				sec = {
					"start":sectionIndex[j]+startIndex,
					"end": len(string) +startIndex
				}
				listSecs.append(sec)
	else :
		sec = {
					"start": startIndex,
					"end": startIndex+len(string)
				}
		listSecs.append(sec)
	resultlist = []
	resultlist.append(listSecs)
	resultlist.append(sum)
	return resultlist
def getTotalPart(result) :
	return result['totalPart']
#from part, result is a part
def getTotalChapter(result) :
	return result['totalChap']
def getTotalSecton(result) :
	return result['totalSec']
def getTotalLaw(result) :
	return result['totalLaw']
def getPart(result,index):
	return result['parts'][index]
def getChapter(result,index):
	return result['chaps'][index]
def getSection(result,index):
	return result['secs'][index]
def getLaw(result,index):
	return result['laws'][index]
#problem with iterator -> generator