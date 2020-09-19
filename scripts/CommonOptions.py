import os
import UserDefinedOptions

class CommonOptions:
    gv = UserDefinedOptions.UserDefinedOptions()

    ## General
    home_dir = os.path.dirname(os.getcwd()) + '/'
    raw_sequences_dir = home_dir + 'raw_sequences/'
    Threads = '8'
    extensions = ['.fastq', '.sam', '.csv', '.txt', '.bam', '.bw']
    summary_dir = home_dir + 'summary_files/'

    ## Cutadapt Variables
    cutadapt_dir = home_dir + 'cutadapt/'

    ## Variables for FastQC
    file_type = ['*.fastq', '*.bam']
    fastqc_raw = 'fastqc_raw'
    fastqc_bam = 'fastqc_mapped'

    ## Support Genomes
    dm_genome = 'ftp://ftp.ensembl.org/pub/release-100/fasta/drosophila_melanogaster/dna/Drosophila_melanogaster.BDGP6.28.dna_sm.toplevel.fa.gz'
    ce_genome = 'ftp://ftp.ensembl.org/pub/release-100/fasta/caenorhabditis_elegans/dna/Caenorhabditis_elegans.WBcel235.dna_sm.toplevel.fa.gz'
    hs_genome = 'ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_34/GRCh38.primary_assembly.genome.fa.gz'
    mm_genome = 'ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M25/GRCm38.primary_assembly.genome.fa.gz'
    dr_genome = 'ftp://ftp.ensembl.org/pub/release-100/fasta/danio_rerio/dna/Danio_rerio.GRCz11.dna_sm.toplevel.fa.gz'
    if gv.species == 'custom': custom_genome = input('FTP link to the genome to download: ')

    ## Support Annotations
    dm_annotation = 'ftp://mirbase.org/pub/mirbase/CURRENT/genomes/dme.gff3'
    ce_annotation = 'ftp://mirbase.org/pub/mirbase/CURRENT/genomes/cel.gff3'
    hs_annotation = 'ftp://mirbase.org/pub/mirbase/CURRENT/genomes/hsa.gff3'
    mm_annotation = 'ftp://mirbase.org/pub/mirbase/CURRENT/genomes/mmu.gff3'
    dr_annotation = 'ftp://mirbase.org/pub/mirbase/CURRENT/genomes/dre.gff3'
    if gv.species == 'custom': custom_annotation = input('FTP link to the miRBase annotation to download: ')

    ## Genome Sequence and Annotation Details
    genome_file = os.path.basename(eval(gv.species + '_genome'))
    genome_path = os.path.dirname(eval(gv.species + '_genome')) + '/'
    genome_dir_name = 'genome'
    genome_dir = home_dir + 'genome/'
    genome_fa = genome_dir + os.path.splitext(genome_file)[0]
    feature_file = os.path.basename(eval(gv.species + '_annotation'))
    feature_path = os.path.dirname(eval(gv.species + '_annotation')) + '/'
    feature_dir_name = 'genome_feature'
    feature_dir = home_dir + 'genome_feature/'
    genes_gtf = feature_dir + os.path.splitext(feature_file)[0]

    ## Alignment Variables
    if eval(gv.bt_parameter) == 'default': bt_parameter = ''
    else: bt_parameter = eval(gv.bt_parameter)
    bt_index = home_dir + 'bt_index/'
    bt_aligned = home_dir + 'bt_aligned/'
    shortstack_aligned = home_dir + 'shortstack_aligned/'

    ## DeepTools BigWig Files
    bigwig_files = home_dir + 'bedgraphs/'

    ## Sam Tools Sorting
    sam_sorted = home_dir + 'sam_sorted/'

    ## FeatureCounts
    fc_output = home_dir + 'feature_counts'
    diff_features = ['miRNA']