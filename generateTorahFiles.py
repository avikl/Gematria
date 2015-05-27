import urllib.request

hebrewAlphabet = [" ","א","ב","ג","ד","ה","ו","ז","ח","ט","י","כ","ל","מ","נ","ס","ע","פ","צ","ק","ר","ש","ת","ך","ם","ן","ף","ץ"]

baseurl = ["http://tanach.us/TextServer?","*&content=Consonants"]
books = ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy"]

def getRawHebrew(filePath):
	readFile = open(filePath,"r")
	writeFile = open(filePath[:12]+"hebrew"+filePath[12:],"w")
	text = ""
	for line in readFile:
		if line.startswith("X"):
			pass
		else:
			temp = ""
			for i in line:
				if i in hebrewAlphabet:
					temp = temp + i
			text = text + temp + "\n"
	writeFile.write(text)

for i in books:
	url = baseurl[0]+i+baseurl[1]
	page = urllib.request.urlopen(url)
	pageText = page.read()
	webFile = open("Torah_Files/" + i + ".txt","w")
	webFile.write(pageText.decode("utf-8"))
	webFile.close()
	webFile = open("Torah_Files/" + i + ".txt","r")
	getRawHebrew("Torah_Files/" + i + ".txt")
	webFile.close()