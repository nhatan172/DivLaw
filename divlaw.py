
# -*- coding:utf8 -*-

import re

class DivLaw :
	@staticmethod
	def split(string,array):
		result = []
		for i in range(0,len(array)) :
			if(i != (len(array)-1)) :
				result.append(string[array[i]:array[i+1]])
			else:
				result.append(string[array[i]:(len(string)-1)])
		return result	
	@staticmethod
	def check(string,array):
		for i in range(0,len(array)) :
			if(string[(array[i]-2):array[i]] == "**"):
				array[i] = array[i]-2
		return array
	@staticmethod
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
	@staticmethod
	def lenIterator(list):
		sum = 0
		for i in list :
			sum += 1
		return sum	
	@staticmethod
	def DivPart(string):
		limitText = len(string)
		partIndex = []
		it = re.finditer(r"(Phần\s[A-Z]*(\*\*|)\n)", string)
		if DivLaw.lenIterator(it) != 0 :
			for match in it:
			    partIndex.append(match.span()[0])
			partIndex = DivLaw.check(string,partIndex)
			result = {
				"totalPart": len(chapterIndex),
				"parts" : ""
			}
			listParts = []

			for i in range(0,len(chapterIndex)):
				if i!=(len(chapterIndex)-1):
					part = {
						"start":chapterIndex[i],
						"end": (chapterIndex[i+1]),
						"totalChap": "",
						"chaps": ""
					}
					listParts.append(part)
				else :
					part = {
						"start":chapterIndex[i],
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
						"start": "NA",
						"end": "NA",
						"totalChap": "",
						"chaps": ""
					}
					listParts.append(part)
			parts = listParts
		return DivLaw.DivChapter(string,result)
	@staticmethod
	def DivChapter(string, result) :
		totalPart = result['totalPart']
		limitText = len(string)
		if totalPart == 0 :
			chapterIndex = []
			it = re.finditer(r"(Chương\s[A-Z]*(\*\*|)\n)", string)
			for match in it:
			    chapterIndex.append(match.span()[0])
			chapterIndex = DivLaw.check(string,chapterIndex)
			result = {
				"totalChap": len(chapterIndex),
				"chaps" : ""
			}
			listChaps = []

			for i in range(0,len(chapterIndex)):
				if i!=(len(chapterIndex)-1):
					chap = {
						"start":chapterIndex[i],
						"end": (chapterIndex[i+1]),
						"totalSec": "",
						"secs": ""
					}
					listChaps.append(chap)
				else :
					chap = {
						"start":chapterIndex[i],
						"end": limitText,
						"totalSec": "",
						"secs": ""
					}
					listChaps.append(chap)
			result['chaps'] = listChaps
			return DivLaw.DivSection(string,result)	
	@staticmethod
	def DivSection(string, result):
		totalChap = result['totalChap']
		chaps = result['chaps']
		for i in range(0,totalChap):
			chapText = string[chaps[i]['start']:chaps[i]['end']]
			it = re.finditer(r"(Mục\s[0-9]*(\*\*|)\n)", chapText)
			sectionIndex = []
			limitText = chaps[i]['end']
			for match in it:
			    sectionIndex.append(chaps[i]['start']+match.span()[0])
			sectionIndex = DivLaw.check(string,sectionIndex)
			listSecs = []
			chaps[i]['totalSec'] = len(sectionIndex)
			for j in range(0,len(sectionIndex)):
				if j!=(len(sectionIndex)-1):
					sec = {
						"start":(sectionIndex[j]),
						"end": (sectionIndex[j+1]),
						"totalLaw": "",
						"laws": ""
					}
					print "___________"
					print string[sectionIndex[j]:sectionIndex[j+1]]
					print "___________"
					listSecs.append(sec)
				else :
					sec = {
						"start":sectionIndex[j],
						"end": limitText,
						"totalLaw": "",
						"laws": ""
					}
					print "___________"
					print string[sectionIndex[j]:limitText]
					print "___________"
					listSecs.append(sec)
			chaps[i]['secs']= listSecs		
		return result
	def DivideLaw(string):
		lawIndex = []
		it = re.finditer(r"(Điều\s[0-9])", string)
		for match in it:
		    lawIndex.append(match.span()[0])
		lawIndex = check(string,lawIndex)
		lawIndex = reFind(string,lawIndex)
		result = split(string,lawIndex)
		return result

#    def ReturnResult(string):
