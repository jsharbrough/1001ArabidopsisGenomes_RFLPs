import sys

def buildSeqDict(fasta):
	infile = open(fasta,'r')
	seqName = ''
	seqDict = {}
	seqList = []
	currSeq = ''
	for line in infile:
		if line[0] == '>':
			if seqName != '':
				seqDict[seqName] = currSeq
			seqName = line[1:]
			while seqName[-1] == '\t' or seqName[-1] == '\r' or seqName[-1] == '\n':
				seqName = seqName[0:-1]
			seqList.append(seqName)
			currSeq = ''
		else:
			currSeq += line
			while currSeq[-1] == '\t' or currSeq[-1] == '\r' or currSeq[-1] == '\n':
				currSeq = currSeq[0:-1]
	seqDict[seqName] = currSeq
	return seqList,seqDict

EcoRI='GAATTC'
BamHI='GGATCC'
HindIII='AAGCTT'
NotI='GCGGCCGC'
PstI='CTGCAG'
reList = ['EcoRI','BamHI','HindIII','NotI','PstI']
atNucList,atNucDict = buildSeqDict(sys.argv[1])
sys.stderr.write('genome read in\n')
for chrm in atNucList:
	sys.stderr.write(chrm + '\n')
	i = 0
	seq = atNucDict[chrm]
	while i < len(seq)-8:
		if seq[i:i+6] == EcoRI:
			outfile = open('TAIR10.EcoRI.txt','a')
			outfile.write(chrm + '\t' + str(i+1) + '\t' + str(i+6) + '\n')
			outfile.close()
		elif seq[i:i+6] == BamHI:
			outfile = open('TAIR10.BamHI.txt','a')
			outfile.write(chrm + '\t' + str(i+1) + '\t' + str(i+6) + '\n')
			outfile.close()
		elif seq[i:i+6] == HindIII:
			outfile = open('TAIR10.HindIII.txt','a')
			outfile.write(chrm + '\t' + str(i+1) + '\t' + str(i+6) + '\n')
			outfile.close()
		elif seq[i:i+6] == PstI:
			outfile = open('TAIR10.PstI.txt','a')
			outfile.write(chrm + '\t' + str(i+1) + '\t' + str(i+6) + '\n')
			outfile.close()
		if seq[i:i+8] == NotI:
			outfile = open('TAIR10.NotI.txt','a')
			outfile.write(chrm + '\t' + str(i+1) + '\t' + str(i+8) + '\n')
			outfile.close()
		i += 1
