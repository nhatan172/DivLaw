
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
	if lenIterator(it) != 0 : 
		for match in it:
		    partIndex.append(match.span()[0])
		partIndex = check(string,partIndex)
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
				listParts.append(part)
			else :
				part = {
					"start":partIndex[i],
					"end": limitText,
					"totalChap": "",
					"chaps": ""
				}
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
		listParts.append(part)
		result['parts'] = listParts
	return DivChapter(string,result)

#Chia theo chuong
def divChapter(string, result) :
	totalPart = result['totalPart']
	if totalPart == 0:
		totalPart = 1
	for i in range(0,totalPart):
		partText = string[result['parts'][i]['start']:result['parts'][i]['end']]
		it = re.finditer(r"(\*\*Chương\s.*\*\*)", partText)
		chapterIndex = [] #chuoi cac index bat dau cua cac chapter
		limitText = result['parts'][i]['end']
		listChaps = []
		if lenIterator(it) >0:
			for match in it:
			    chapterIndex.append(chaps[i]['start']+match.span()[0])
			chapterIndex = check(string,chapterIndex)
			chaps[i]['totalChap'] = len(chapterIndex)
			for j in range(0,len(chapterIndex)):
				if j!=(len(chapterIndex)-1):
					chap = {
						"start":(chapterIndex[j]),
						"end": (chapterIndex[j+1]),
						"totalSec": "",
						"secs": ""
					}
					listChaps.append(chap)
				else :
					chap = {
						"start":chapterIndex[j],
						"end": limitText,
						"totalSec": "",
						"secs": ""
					}
					listChaps.append(chap)
		else :
			result['parts'][i]['totalChap'] = 0
			part = {
						"start": result['parts'][i]['start'],
						"end": result['parts'][i]['end'],
						"totalSec": "",
						"secs": ""
					}
			listChaps.append(chap)
		result['parts'][i]['chaps']= listChaps	
	return divSection(string,result)	

#Chia theo muc
def divSection(string, result):
	totalPart = result['totalPart']
	if totalPart == 0:
		totalPart = 1
	for i in range(0,totalPart):
		totalChap = result['parts'][i]['totalChap']
		if totalChap == 0:
			totalChap = 1
		for k in range(0,totalChap):
			chapText = string[result['parts'][i]['chaps'][k]['start']:result['parts'][i]['chaps'][k]['end']]
			it = re.finditer(r"(\*\*Mục\s[0-9]*(\*\*|)\n)", chapText)
			secIndex = []
			limitText = result['parts'][i]['chaps'][k]['end']
			listSecs = []
			if lenIterator(it)>0:
				for match in it:
				    secIndex.append(result['parts'][i]['chaps'][k]['start']+match.span()[0])
				secIndex = check(string,secIndex)
				result['parts'][i]['chaps'][k]['totalSec'] = len(sectionIndex)
				for j in range(0,len(sectionIndex)):
					if j!=(len(sectionIndex)-1):
						sec = {
							"start":(sectionIndex[j]),
							"end": (sectionIndex[j+1]),
							"totalLaw": "",
							"laws": ""
						}
						listSecs.append(sec)
					else :
						sec = {
							"start":sectionIndex[j],
							"end": limitText,
							"totalLaw": "",
							"laws": ""
						}
						listSecs.append(sec)
			else :
				result['parts'][i]['chaps'][k]['totalSec'] = 0
				part = {
							"start": result['parts'][i]['chaps'][k]['start'],
							"end": result['parts'][i]['chaps'][k]['end'],
							"totalSec": "",
							"secs": ""
						}
				listSecs.append(chap)
		result['parts'][i]['chaps'][k]['secs']= listSecs
	return DivSection(string,result)

#chia theo dieu
def divideLaw(string):
	totalPart = result['totalPart']
	if totalPart == 0:
		totalPart = 1
	for i in range(0,totalPart):
		totalChap = result['parts'][i]['totalChap']
		if totalChap == 0:
			totalChap = 1
		for k in range(0,totalChap):
			totalSec = result['parts'][i]['chaps'][k]['totalSec']
			totalSec =
			chapText = string[result['parts'][i]['chaps'][k]['start']:result['parts'][i]['chaps'][k]['end']]
			it = re.finditer(r"(\*\*Điều [0-9]*(\.|)\*\*)", chapText)
			secIndex = []
			limitText = result['parts'][i]['chaps'][k]['end']
			listSecs = []
			if lenIterator(it)>0:
				for match in it:
				    secIndex.append(result['parts'][i]['chaps'][k]['start']+match.span()[0])
				secIndex = check(string,secIndex)
				result['parts'][i]['chaps'][k]['totalSec'] = len(sectionIndex)
				for j in range(0,len(sectionIndex)):
					if j!=(len(sectionIndex)-1):
						sec = {
							"start":(sectionIndex[j]),
							"end": (sectionIndex[j+1]),
							"totalLaw": "",
							"laws": ""
						}
						listSecs.append(sec)
					else :
						sec = {
							"start":sectionIndex[j],
							"end": limitText,
							"totalLaw": "",
							"laws": ""
						}
						listSecs.append(sec)
			else :
				result['parts'][i]['chaps'][k]['totalSec'] = 0
				part = {
							"start": result['parts'][i]['chaps'][k]['start'],
							"end": result['parts'][i]['chaps'][k]['end'],
							"totalSec": "",
							"secs": ""
						}
				listSecs.append(chap)
		result['parts'][i]['chaps'][k]['secs']= listSecs
	return DivSection(string,result)
