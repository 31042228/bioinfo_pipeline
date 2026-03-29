# NGS Bioinformatics Pipeline
Author: 31042228
# Description: Pipeline for NGS data processing
# Variant Calling Module
def run_variant_calling(input_file):
    print('Running variant calling on', input_file)
    min_quality = 30
    min_depth = 10
    ploidy = 2
    print('Min quality score:', min_quality)
    print('Min depth:', min_depth)
    print('Ploidy:', ploidy)
    print('Variant calling complete.')
