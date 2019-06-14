# Vignette

### Running the program

Using the two test datasets "ecoPCR_RF_barcodes.fasta" and "Min_sebastes_ASV_sum_by_taxonomy_40.txt", you can run the complete script, which will look for identical barcodes in your fasta file and then use these to annotate the ASV table. To run the complete script, you will need to be in the directory that contains these two files as well as the scripts, and then use the following command:

python3 misebastes_annotator.py ecoPCR_RF_barcodes.fasta Min_sebastes_ASV_sum_by_taxonomy_40.txt > output_file.txt

This will give two outputs: "trimmed_ecoPCR_RF_barcodes.fasta", which reveals which species share a barcode, and "output_file.txt", which uses the information about from the trimmed fasta table to add a new column to the ASV table of all species that share that barcode. 

Alternatively, if you wish to only take a fasta file containing all your sequences to see which ones shared a barcode, run the following code:

python3 find_identical_barcodes.py ecoPCR_RF_barcodes.fasta

This will give one output file: identical_barcodes_ecoPCR_RF_barcodes.fasta.