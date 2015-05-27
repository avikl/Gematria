hebrewToGematria = {"aleph":1,"bet":2,"gimel":3,"dalet":4,"heh":5,"vav":6,"zayin":7,"het":8,"tet":9,"yud":10,"kaf":20,"lamed":30,"mem":40,"nun":50,"samech":60,"ayin":70,"peh":80,"tzadik":90,"koof":100,"reish":200,"shin":300,"taf":400,"kafF":500,"memF":600,"nunF":700,"pehF":800,"tzadikF":900}
codeToHebrew = {"א":"aleph","ב":"bet","ג":"gimel","ד":"dalet","ה":"heh","ו":"vav","ז":"zayin", "ח":"het","ט":"tet","י":"yud","כ":"kaf","ל":"lamed","מ":"mem","נ":"nun","ס":"samech","ע":"ayin","פ":"peh","צ":"tzadik","ק":"koof","ר":"reish","ש":"shin","ת":"taf","ך":"kafF","ם":"memF","ן":"nunF","ף":"pehF","ץ":"tzadikF"}

books = ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy"]

gematria = {}
for book in books:
	mean = 0
	largest = 0
	fileText = open("Torah_Files/" + "hebrew" + book + ".txt","r")
	rawText = ""
	for line in fileText:
		rawText = rawText + line
	hebrew = rawText.split()
	for word in hebrew:
		total = 0
		for letter in word:
			number = hebrewToGematria[codeToHebrew[letter]]
			total += number
		mean += total
		if total > largest:
			largest = total
		gematria[word] = total
	mean = mean/len(hebrew)
	print(book + ": " + str(mean) + ", max: " + str(largest))
#print(gematria)