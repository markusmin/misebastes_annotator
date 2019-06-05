
import sys
import Bio
from Bio import SeqIO

def find_identical_barcodes(fasta_file):
    # Create our hash table to add the sequences
    sequences={}

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
    with open("clear_2_" + fasta_file, "w+") as output_file:
        # Just read the hash table and write on the file as a fasta format
        for sequence in sequences:
            output_file.write(">" + sequences[sequence] + "\n" + sequence + "\n")

    print("CLEAN!!!\nPlease check clear_2_" + fasta_file)

userParameters = sys.argv[1:]

find_identical_barcodes(userParameters[0])

