# coding: utf-8
true = True
false = False
null = None

import sys
import BeautifulSoup
def chill():
    return
if(len(sys.argv)<3):
	print """
Please provide the input and output files as space deliminated arguments -i.e.>
python pretty.py ifile.html ofile.html "aditional args are ignored"
"""

iFile = sys.argv[1]
print "input file: "+iFile
oFile = sys.argv[2]

if "http" in iFile:
	import mechanize
	chrome = mechanize.Browser()
	chrome.set_handle_robots(False)
	chrome.addheaders = [('User-agent', '')]
	htmltext = chrome.open(iFile).read()
	soup = BeautifulSoup.BeautifulSoup(htmltext)
else:
	htmlfile = open(iFile,"r")
	htmltext = htmlfile.read()
	soup = BeautifulSoup.BeautifulSoup(htmltext)
	htmlfile.close()

prettyText = soup.prettify()
lines = prettyText.split("\n")

modelChunks = [k for k in lines if "DOCS_modelChunk " in k]
for n,k in enumerate(modelChunks):
        eIndx = len(modelChunks)-1
        while(not(k[eIndx-1]=="]"and k[eIndx]==";")):
            eIndx-=1
        sIndx = 0
        while(k[sIndx]==" "):
            sIndx+=1
        #print("\n\n\n@@\n"+modelChunks[n][sIndx:eIndx]+"\n$$\n\n\n")
        modelChunks[n] = eval(modelChunks[n][sIndx+18:eIndx])
        links = []
        for k2 in modelChunks[n]:
                try:
                    if(k2["sm"]["lnks_link"]["lnk_type"]==0):
                        links.append(k2)
                except:
                    chill()
        temp = {"text":modelChunks[n][0]["s"],"links":links}
        modelChunks[n] = temp
from really import PrettyNest as pretty
#print(pretty(modelChunks))
print "output file: "+oFile
opText = ""
for chunk in modelChunks:
	opText+="<p>"
	fill = chunk["text"].split(" ")
	count = 0
	temp = ""
	fillLines = ""
	for k in fill:
		if(count>35):
			if("\u000b" in temp):
				temp = temp.replace("\u000b","<br>")
			fillLines += "<font>"+temp+"</font><br>\n"
			temp = ""
			count = 0
		temp += k+" "
		count += len(k)
	fillLines += "<font>"+temp+"</font><br>\n"
	opText+=fillLines
	opText+="</p>"
from fill import makeContentFiller
template = makeContentFiller("index.html")
output = open(oFile,"w")
output.write(template(opText))
output.close()






