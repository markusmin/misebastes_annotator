# MiSebastes Anacapa addon

# USAGE:

# python3 misebastes_annotator.py ecoPCR_RF_barcodes.fasta Min_sebastes_ASV_sum_by_taxonomy_40.txt > output_file.txt


# Import Biopython tools

import sys
import Bio
from Bio import SeqIO

def combined_script(fasta_file, anacapa_file):
    # Create our hash table to add the sequences (empty dictionary)
    # Here we are setting up a dictionary where the sequences act as the keys
    # and the taxonomy acts as the values
    sequences={}
    infile = anacapa_file
    capa = open(infile,'r')

    # Using the Biopython fasta parse we can read our fasta input
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
    	# Take the current sequence
        sequence = str(seq_record.seq).upper()
        # If the sequence isn't yet in the dictionary, the sequence and its ID
        # will be added
        #if sequence not in sequences:
        if sequence not in sequences:
        	sequences[sequence] = seq_record.id.replace("S.","Sebastes ")
        # Don't add the same species twice
        # elif seq_record.id in sequences:
        # 		sequences[sequence] = sequences[sequence]
    	# If it is already in the hash table, we're just gonna concatenate the ID
    	# of the current sequence to another one that is already in the hash table.
    	# But don't concatenate add the same species name twice
        else:
        	sequences[sequence] += ", " + seq_record.id.replace("S.","Sebastes ")
        	
    # Create a new version of the sequence dictionary that doesn't have any repeated taxa;
    # use this version of the dictionary later to ensure that no extra lines are added
    temp = []
    unique_taxa = dict()
    for key, val in sequences.items():
        if val not in temp:
            temp.append(val)
            unique_taxa[key] = val

    # Write the sequences

	# Write one version with all of the unique barcodes; save for reference
    # Create a file in the same directory where you ran this script
    with open("trimmed_" + fasta_file, "w+") as output_file:
        # Just read the hash table and write on the file as a fasta format
        for sequence in sequences:
            output_file.write(">" + sequences[sequence] + "\n" + sequence + "\n")
    
    # Write one version with only the unique species combinations; this isn't necessary,
    # but could be used to keep a record
    # Create a file in the same directory where you ran this script
    #with open("trimmed_" + fasta_file, "w+") as output_file:
        # Just read the hash table and write on the file as a fasta format
        # Create a list of values to store taxa you have already written
        #writtentaxa = []
        #for sequence in sequences:
        	# If we've already written it, don't write it again
            #if sequences[sequence] not in writtentaxa:
                #output_file.write(">" + sequences[sequence] + "\n" + sequence + "\n")
            # Add to the list to make sure we don't write it twice
            #writtentaxa.append(sequences[sequence])

    #print("CLEAN!!!\nPlease check trimmed_" + fasta_file)


	# assign the second argument where you specified the Anacapa taxonomy table
	# to infile, open as "capa"
	
	# Annotate Anacapa file with all matching species

    for line in capa:
        # Split the lines
        line2=line.strip('\n')
		# Split the line into elements by tab
        Element=line2.split('\t')
        Element1 = Element[0]
        if Element[0] == "sum.taxonomy":
        	print('%s\t%s\t%s' % (Element[0],'matching.species', '\t'.join(Element[1:])))
        else:
        	taxa=Element1.split(";")
        	if len(taxa) > 6 and len(str(taxa[6]))>1:
        # Look for matching species
        		for key in unique_taxa.keys():
        			if str(taxa[6]) in str(unique_taxa[key]):
        				newColumn = str(unique_taxa[key])
        				print('%s\t%s\t%s' % (Element[0], newColumn, '\t'.join(Element[1:])))
        	else:
        		print('%s\t%s\t%s' % (Element[0], "NA", '\t'.join(Element[1:])))
        		

userParameters = sys.argv[1:]

try:
    if len(userParameters) == 2:
    	combined_script(userParameters[0], userParameters[1])
    else:
        print("Please ensure that you entered the right number of arguments!")
except:
    print("Error. Please consult the Vignette.")








