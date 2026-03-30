# Bioinfo Pipeline

A bioinformatics pipeline for NGS data analysis including 
quality control, variant calling and input validation.

## Dependencies
- Python 3.11
- FastQC 0.11.9
- BWA 0.7.17
- SAMtools 1.17

## Installation
Install required Python packages:
pip install biopython==1.81
pip install pandas==2.1.4

Install bioinformatics tools:
sudo apt install fastqc
sudo apt install bwa
sudo apt install samtools

## Usage
Run the full pipeline:
python src/pipeline.py --input sample.fastq

Run quality control only:
python src/pipeline.py --qc sample.fastq

Run variant calling only:
python src/pipeline.py --variant sample.fastq

## Author
Student: 31042228
Stellenbosch University

