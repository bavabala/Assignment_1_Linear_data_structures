string = "thisisit"
while string != "":
	slen0 = len(string)
	ch = string[0]
	string = string.replace(ch, "")
	slen1 = len(string)
	if slen1 == slen0-1:
		print ("First non-repeating character = ",ch)
		break;
	else:
		print ("No Unique Character Found!")