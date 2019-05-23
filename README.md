# Primer Design Program

Designing new primers for metabarcoding is one of the primary challenges in genomics.
This project seeks to help automate and simplify that process, by taking a limited 
number of inputs from the user (e.g. target group, gene, purpose of primer - like 
eDNA metabarcoding, just amplifying a certain gene, etc.) and churning out primers, with
information included about those primers and how they can be used.

The metabarcode amplified by the MiSebastes primers is unique for almost 2/3 of the genus 
Sebastes. However, for the remaining 1/3 of the genus, multiple species share the same barcode. This program, which can also be used on other datasets containing multiple sequences for the same barcodes, determines which species share the same barcode. It formats this output as a table detailing which species have an identical barcode, and then uses another script to append a new column to a taxonomy output file generated using the Anacapa pipeline. This new column will tell you which species your barcode matches to, and thus tells you which species you my have found in your eDNA sample.
## Getting Started

This program has two parts:
1) Creating the table of barcodes with different species that share a barcode
2) Using the table to append a new column to an Anacapa taxonomy file idnetifying which species the barcode may belong to.

Here is how to run each of the parts:

1) identical-barcodes.py input_fasta_file output_file_name
2) append_taxonomy.py input_anacapa_file output_anacapa_file

### Example usage

1) identical-barcodes.py NOAA_barcodes.fasta barcodes_table.csv
2) append_taxonomy.py Min_Sebastes_ASV_taxonomy Min_Sebastes_ASV_taxonomy_appended

### Prerequisites

This program requires Biopython and Anacapa.

## Authors

* **Markus Min** - *Initial work* - [markusmin](https://github.com/markusmin)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thank you very much to Emily Curd and Daniel Chavez for helping with the design of this program.

