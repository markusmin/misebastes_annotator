# MiSebastes Anacapa addon

# USAGE:

# python3 misebastes_annotator.py ecoPCR_RF_barcodes.fasta Min_sebastes_ASV_sum_by_taxonomy_40.txt

# Following three lines are for when the script actually works and you can just
# specify your anacapa file at the start!


### Finding identical barcodes

# Import Biopython tools

# find_identical_barcodes.py


import sys
import Bio
from Bio import SeqIO

def combined_script(fasta_file, anacapa_file):
    # Create our hash table to add the sequences
    sequences={}
    infile = anacapa_file
    capa = open(infile,'r')

    # Using the Biopython fasta parse we can read our fasta input
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
    	# Take the current sequence
        sequence = str(seq_record.seq).upper()
        # If the sequence isn't yet in the hash table, the sequence and its ID
        # will be added
        if sequence not in sequences:
        	sequences[sequence] = seq_record.id.replace("S.","Sebastes ")
    	# If it is already in the hash table, we're just gonna concatenate the ID
    	# of the current sequence to another one that is already in the hash table
        else:
        	sequences[sequence] += ", " + seq_record.id.replace("S.","Sebastes ")

    # Write the sequences

    # Create a file in the same directory where you ran this script
    with open("trimmed_" + fasta_file, "w+") as output_file:
        # Just read the hash table and write on the file as a fasta format
        for sequence in sequences:
            output_file.write(">" + sequences[sequence] + "\n" + sequence + "\n")

    print("CLEAN!!!\nPlease check trimmed_" + fasta_file)


	# assign the second argument where you specified the Anacapa taxonomy table
	# to infile, open as "capa"
	
	# Annotate Anacapa file with all matching species
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
        		

userParameters = sys.argv[1:]

try:
    if len(userParameters) == 2:
    	combined_script(userParameters[0], userParameters[1])
    else:
        print("Please ensure that you entered the right number of arguments!")
except:
    print("There is a problem! You really messed up somewhere...")








