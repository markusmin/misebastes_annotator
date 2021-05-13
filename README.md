# MiSebastes Annotator

#### Last updated 13 May 2021
* Written by *Markus Min* (mmin@uw.edu)

## Introduction

##### Background on Environmental DNA Metabarcoding
Environmental DNA metabarcoding is a new method for sampling the biodiversity of marine ecosystems through the sequencing of DNA extracted from water samples (Taberlet et al. 2012). It relies on the identification of suitable metabarcodes, highly variable regions of the genome capable of distinguishing individual species that are flanked on either side by highly conserved regions that allow for primer annealing to a wide variety of taxa. 

##### The MiSebastes Primer Set
The MiSebastes primer set is a new set of primers developed specifically for rockfishes, genus *Sebastes*. This group of commercially and ecologically important fishes radiated very recently (many within the last million years), leading to a high degree of interspecific genetic similarity between different species in this genus (Hyde & Vetter 2007). As universal teleost primers lack the resolution to distinguish between different *Sebastes* spp. (Miya et al. 2015), MiSebastes was developed to develop a new metabarcode for these fishes. However, because of the extreme genetic similarity between *Sebastes* spp., this metabarcode is still identical for some species. This program first determines which species share the same barcode and then appends a new column to a taxonomy output file generated using the Anacapa pipeline. This new column will tell you the different species your barcode matches to, and thus tells you which species you my have found in your eDNA sample.

## Workflow

This program essentially has two parts: 
(1) Taking a raw fasta file and trimming it down so that each DNA sequence is only listed once, with all species that share the barcode assigned to the sequence barcodes with different species that share a barcode. This fasta file is one of the outputs.
  - The raw fasta file supplied in the Vignette is an ecoPCR output for the MiSebastes primers, which this first step uses to detect all *Sebastes* spp. that share a barcode and outputs 
(2) Using the fasta file to append a new column to an Anacapa ASV file, identifying all species that share the particular barcode.

The first step can also be used independently to detect which species share a sequence for your metabarcode.

### Example usage/Instructions

#### Misebastes_annotator

If you have a fasta file containing all of your barcodes and an ASV table that you wish to annotate, use the following command to run the complete script:

python3 misebastes_annotator.py ecoPCR_RF_barcodes.fasta Min_sebastes_ASV_sum_by_taxonomy_40.txt > output_file.txt

In this example usage, the fasta file that contains your barcodes is ecoPCR_RF_barcodes.fasta and the anacapa taxonomy file that you wish to annotate is Min_sebastes_ASV_sum_by_taxonomy_40.txt. This will produce two output files:
1) The trimmed fasta file, called trimmed_ecoPCR_RF_barcodes.fasta
2) The annotated Anacapa taxonomy file, called "output_file.txt".

Prior to running this program, you must have the misebastes_annotator.py, your fasta file, and your Anacapa ASV file all in the same directory. The annotated Anacapa ASV file can then be viewed in Excel.

#### Find-identical-barcodes

This script can also be used for other metabarcodes, based largely on this Biopython [script](https://biopython.org/wiki/Sequence_Cleaner). If you want to figure out for which species your barcode is identical, you can create the trimmed fasta file by running the following script:

python3 find-identical-barcodes.py ecoPCR_RF_barcodes.fasta.

Your output file will be trimmed_ecoPCR_RF_barcodes.fasta.

### Dependencies

This program requires **Biopython** (Cock et al. 2009) and the **Anacapa Toolkit** (Curd et al. 2019).

**Biopython** can be found here: https://biopython.org/
Installation instructions can be found at this link:
https://biopython.org/wiki/Download

**Anacapa** can be found here: https://github.com/limey-bean/Anacapa

## Authors

* **Markus Min** - [markusmin](https://github.com/markusmin)

## References

Cock, P.J., Antao, T., Chang, J.T., Chapman, B.A., Cox, C.J., Dalke, A., Friedberg, I., Hamelryck, T., Kauff, F., Wilczynski, & De Hoon, M. J. (2009). Biopython: freely available Python tools for computational molecular biology and bioinformatics. Bioinformatics, 25(11), 1422-1423.

Curd, E. E., Gold, Z. , Kandlikar, G. S., Gomer, J. , Ogden, M. , O'Connell, T. , Pipes, L. , Schweizer, T. M., Rabichow, L. , Lin, M. , Shi, B. , Barber, P. H., Kraft, N. , Wayne, R. and Meyer, R. S. (2019), Anacapa Toolkit: an environmental DNA toolkit for processing multilocus metabarcode datasets. Methods Ecol Evol. Accepted Author Manuscript. doi:10.1111/2041-210X.13214

Hyde, J. R., & Vetter, R. D. (2007). The origin, evolution, and diversification of rockfishes of the genus Sebastes (Cuvier). Molecular phylogenetics and evolution, 44(2), 790-811.

Miya, M., Sato, Y., Fukunaga, T., Sado, T., Poulsen, J.Y., Sato, K., Minamoto, T., Yamamoto, S., Yamanaka, H., Araki, H. & Kondoh, M. (2015). MiFish, a set of universal PCR primers for metabarcoding environmental DNA from fishes: detection of more than 230 subtropical marine species. Royal Society open science, 2(7), 150088.

Taberlet, P., Coissac, E., Hajibabaei, M., & Rieseberg, L. H. (2012). Environmental DNA. Molecular ecology, 21(8), 1789-1793.

## Acknowledgments

Thank you very much to Emily Curd and Daniel Chavez for helping with the design of this program.

## DOI and Citation

DOI: https://doi.org/10.5281/zenodo.3246598

Citation: 

Min, Markus. (2019, June 14). MiSebastes Annotator (Version 1.0). Zenodo. http://doi.org/10.5281/zenodo.3246598
