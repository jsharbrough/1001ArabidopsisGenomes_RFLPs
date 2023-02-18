import sys,gzip
infile = open(sys.argv[1],'r')
reDict = {}
for line in infile:
	realLine = line
	while realLine[-1] == '\t' or realLine[-1] == '\r' or realLine[-1] == '\n':
		realLine = realLine[0:-1]
	lineSplit = realLine.split('\t')
	reSplit = lineSplit[0].split('-')
	re = reSplit[0]
	if re not in reDict:
		reDict[re] = {lineSplit[1]:{lineSplit[2]:lineSplit[0]}}
	else:
		currDict = reDict[re]
		if lineSplit[1] not in currDict:
			currDict[lineSplit[1]] = {lineSplit[2]:lineSplit[0]}
		else:
			chrmDict = currDict[lineSplit[1]]
			chrmDict[lineSplit[2]] = lineSplit[0]
			currDict[lineSplit[1]] = chrmDict
		reDict[re] = currDict

infile.close()
infile = gzip.open(sys.argv[2],'r')
for line in infile:
	if line[0] == '#':
		if line[1:5] == 'CHRO':
			sys.stdout.write('RE_SITE_ID\t' + line)
		else:
			sys.stdout.write(line)
	else:
		realLine = line
		while realLine[-1] == '\t' or realLine[-1] == '\r' or realLine[-1] == '\n':
			realLine = realLine[0:-1]
		lineSplit = realLine.split('\t')
		if lineSplit[4] != '.':
			for re in reDict:
				currDict = reDict[re]
				chrmDict = currDict[lineSplit[0]]
				if lineSplit[1] in chrmDict:
					sys.stdout.write(chrmDict[lineSplit[1]] + '\t' + line)

infile.close()
