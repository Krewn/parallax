def makeContentFiller(inputFile):
	templateOnDisk = open(inputFile,"r")
	headNtail = templateOnDisk.read().split("|DO NOT EDIT BETWEEN THE BARS $pageContent$ DO NOT EDIT BETWEEN THE BARS|")
	templateOnDisk.close()
	if(len(headNtail)!=2):
		print("template file error using::"+inputFile+'\n!!!\nlen(templateOnDisk.read().split("|DO NOT EDIT BETWEEN THE BARS $pageContent$ DO NOT EDIT BETWEEN THE BARS|"))!!!=2\n!\nUsing builtin headNtail:')
		headNtail=["<!DOCTYPE html><html><head></head><body>","</body></html>"]
		print headNtail
	def templateDefinition(fill):
		return(headNtail[0]+str(fill)+headNtail[1])
	return(templateDefinition)

#template = makeContentFiller("index.html")
#output = template("fill")

