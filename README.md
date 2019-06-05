# MiSebastes Annotator

#### Last updated June 4th, 2019
* Written by *Markus Min* (markus.min@gmail.com)

## Introduction
Environmental DNA metabarcoding is a new method for sampling the biodiversity of marine ecosystems through the sequencing of DNA extracted from water samples. It relies on the identification of suitable metabarcodes, highly variable regions of the genome capable of distinguishing individual species that are flanked on either side by highly conserved regions that allow for primer annealing to a wide variety of taxa. The MiSebastes primer set is a new set of primers developed specifically for rockfishes, genus *Sebastes*. This group of commercially and ecologically important fishes radiated very recently (many within the last million years), leading to a high degree of interspecific genetic similarity between different species in this genus. As universal teleost primers lack the resolution to distinguish between different *Sebastes* spp., MiSebastes was developed to develop a new metabarcode for these fishes. However, because of the extreme genetic similarity between *Sebastes* spp., this metabarcode is still identical for some species. This program first determines which species share the same barcode and then appends a new column to a taxonomy output file generated using the Anacapa pipeline. This new column will tell you the different species your barcode matches to, and thus tells you which species you my have found in your eDNA sample.

## Workflow

This program essentially has two parts: 
(1) Taking your raw fasta file and trimming it down so that each DNA sequence is only listed once, with all species that share the barcode assigned to the sequence barcodes with different species that share a barcode. This fasta file is one of the outputs.
(2) Using the fasta file to append a new column to an Anacapa ASV file, identifying all species that share the particular barcode.

These two steps can also be used independently.

### Example usage

#### Misebastes_annotator

python3 misebastes_annotator.py ecoPCR_RF_barcodes.fasta Min_sebastes_ASV_sum_by_taxonomy_40.txt

In this example usage, the fasta file that contains your barcodes is ecoPCR_RF_barcodes.fasta and the anacapa taxonomy file that you wish to annotate is Min_sebastes_ASV_sum_by_taxonomy_40.txt. This will produce two output files:
1) The trimmed fasta file, called trimmed_ecoPCR_RF_barcodes.fasta
2) The annotated Anacapa taxonomy file, called Min_sebastes_ASV_sum_by_taxonomy_40_annotated.txt

Prior to running this program, you must have the misebastes_annotator.py, your fasta file, and your Anacapa ASV file all in the same directory. The annotated Anacapa ASV file can then be viewed in Excel.

#### Find-identical-barcodes

This script can also be used for other metabarcodes, based largely on this Biopython [script](https://biopython.org/wiki/Sequence_Cleaner). If you want to figure out for which species your barcode is identical, you can create the trimmed fasta file by running the following script:

python3 find-identical-barcodes.py ecoPCR_RF_barcodes.fasta

Your output file will be trimmed_ecoPCR_RF_barcodes.fasta

#### Anacapa-annotator

If you already know which species share a sequence and have a trimmed fasta file for it, you can use this fasta file to annotate an Anacapa ASV file with the following script:

python3 Anacapa-annotator trimmed_ecoPCR_RF_barcodes.fasta Min_sebastes_ASV_sum_by_taxonomy_40.txt

Your output file will be the annotated Anacapa ASV file, Min_sebastes_ASV_sum_by_taxonomy_40_annotated.txt

### Prerequisites

This program requires **Biopython** and **Anacapa**.
**Biopython** can be found here: https://biopython.org/
**Anacapa** can be found here: https://github.com/limey-bean/Anacapa

## Authors

* **Markus Min** - [markusmin](https://github.com/markusmin)

## Acknowledgments

* Thank you very much to Emily Curd and Daniel Chavez for helping with the design of this program.