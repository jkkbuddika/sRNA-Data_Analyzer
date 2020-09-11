# Small RNA (sRNA)-Seq Data Analyzer
The current version of sRNA-Seq data analyzer contain a series of python based modules that automate the analysis process. I ***highly recommend*** reading through this step-by-step manual *carefully* before you start analyzing your data.

## Requirements
The sRNA-seq data analyzer requires following tools to be installed (see [here](https://github.com/jkkbuddika/RNA-Seq-Data-Analyzer/blob/master/USERGUIDE.md#step-2-setup-the-miniconda-environment)) for data analysis.

- [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
- [Cutadapt](https://cutadapt.readthedocs.io/en/stable/)
- [Bowtie](https://github.com/BenLangmead/bowtie)
- [ShortStack](https://github.com/MikeAxtell/ShortStack)
- [SAMtools](https://github.com/samtools/samtools)
- [deepTools](https://github.com/deeptools/deepTools/)
- [featureCounts](http://subread.sourceforge.net/)
- [MultiQC](https://github.com/ewels/MultiQC)

We thank developers of these valueble tools!

## Analysis process
All analyzed data will be saved onto the home directory where you deposited the *scripts* directory. The pipeline first use [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) to assess the quality of raw input files. Conventional illumina adaptors, random UMIs and low quality reads are removed using [Cutadapt](https://cutadapt.readthedocs.io/en/stable/). Based on the user defined species, corresponding genome and miRBase miRNA annotation files will be downloaded. Then, [Bowtie](https://github.com/BenLangmead/bowtie) genome indices will be generated. Next, quality-trimmed sequences are mapped to the reference genome using [Bowtie](https://github.com/BenLangmead/bowtie) genome aligner. The analysis scheme use [SAMtools](https://github.com/samtools/samtools) to coordinate sort, remove unmapped sequences and index alignment output files. The sorted alignment file and the index will be used by [deepTools](https://github.com/deeptools/deepTools/) to generate bigwig files for [IGV](https://software.broadinstitute.org/software/igv/) visualization. Next subread package [featureCounts](http://subread.sourceforge.net/) will be called to quantify, by default, the number of reads aligning to miRNAs. In addition, the pipeline uses [ShortStack](https://github.com/MikeAxtell/ShortStack) to independently align trimmed small RNA-seq data and annotate small RNA-producing genes. Finally, the pipeline integrates [MultiQC](https://github.com/ewels/MultiQC) to generate summary files in an interactive manner.

Now that you know the general outline of the analysis process, go through the step-by-step **user guide** given [here](https://github.com/jkkbuddika/RNA-Seq-Data-Analyzer/blob/master/USERGUIDE.md) to analyze your RNA-seq data.
