### Anacapa Annotator
  
infile = anacapa_file
capa = open(infile,'r')
    
    for line in capa:
		# Split the lines
        line2=line.strip('\n')
		# Split the line into elements by tab
        Element=line2.split('\t')
		#print(Element[0])
        Element1 = Element[0]
        taxa=Element1.split(";")
        if len(taxa) > 6:
        	#matching_species = sequences[sequence[(taxa[6])]]
        	for key in sequences.keys():
        		if str(taxa[6]) in str(sequences[key]):
        			newColumn = str(sequences[key])
        	print(Element[0], newColumn, Element[1:])