# NGS Bioinformatics Pipeline
Author: 31042228
# Description: Pipeline for NGS data processing
# Quality Control Module
def run_fastqc(input_file) :
# Quality Control Module
def run_fastqc(input_file):
    print('Running FastQC on', input_file)
    min_quality = 20
    min_length = 50
    adapter_removal = True
    print('Min quality score:', min_quality)
    print('Min read length:', min_length)
    print('Adapter removal:', adapter_removal)
    print('QC complete.')
