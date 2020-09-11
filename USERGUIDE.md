# User Guide
Please go through this step-by-step guide to setup and begin analysis of your data. This is a ***four*** step process:

### Step 1: Cloning the repository
To clone the current repository on to your local repository using terminal, first navigate to the ***home directory*** (i.e., where you want analyzed data to be deposited), paste and enter the following command:

```
git clone https://github.com/jkkbuddika/sRNA-Data_Analyzer.git
ls
```
> sRNA-Data_Analyzer   

Once cloning is completed:
```
mv sRNA-Data_Analyzer/*/ ./
rm -rf sRNA-Data_Analyzer
ls
```
> environment           
> scripts 

### Step 2: Setup the miniconda environment
There are two ways to set up the conda environment: (1) Using the *environment.yml* file in the **environment** directory or (2) manually creating a conda environment and installing all required packages. The advantage of using the first approach is, it gives the conda environment I used when I was writing this python pipeline. However, the second approach let you install the latest versions of required packages. Note that based on the version of a similar tool, the output results can be varied. Let's go through how to both of these.

#### Install miniconda
Before creating the environment, [install](https://conda.io/projects/conda/en/latest/user-guide/install/index.html?highlight=conda) miniconda and add conda to you PATH. Then update conda by running ```conda update conda```.

#### Setting up the miniconda environment with the *environment.yml* file
Simply copy, paste and run the following command on your terminal window.

```
cd environment
conda env create -f environment.yml
cd ..
```
Running this command will create a conda environment named ***srnaanalyzer*** on your local computer.

#### Setting up the miniconda environment by manually installing required packages and dependencies
In this scenario, to setup the conda environment (i.e., srnaanalyzer), run following terminal commands.

```
conda create -n srnaanalyzer -c conda-forge -c bioconda python=3.7
conda install -n srnaanalyzer -c conda-forge -c bioconda fastqc cutadapt bowtie samtools deeptools subread multiqc pandas
```
#### Activate and deactivate the miniconda environment
To activate the enironment:
```
source activate srnaanalyzer
```
To deactivate the environment run the following terminal command or simply close the terminal window:
```
source deactivate
```

For more details on managing conda enviroments [click here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#).

### Step 3: Input data preparation
The pipeline uses input files in .fastq format for analysis. To upload input data, navigate first to the home directory and create a directory *raw_sequences*.
```
mkdir raw_sequences
ls
```
> environment         
> raw_sequences   
> scripts   

Then upload input sequences to the *raw_sequences* directory. Naming of files is ***very important*** and ***must*** follow the recommended naming scheme. Name of an input fastq file must end in the following order: `_R1.fastq`

If the naming is different than what is required, you can use a bash command like below to automatically rename all files to the correct architecture.
```
for i in `ls *R1*`; do
newname="${i/%_001.fastq/.fastq}"
mv -- "$i" "$newname"; 
done
```
> In the above example, running this command will convert a file name from `esg_WT_T1_R1_001.fastq` to `esg_WT_T1_R1.fastq`.

### Step 4: Executing the pipeline
All executables of the pipeline are written onto *run.py* module. To start analyzing data, activate the conda environment above, navigate to the scripts directory and execute *run.py* using python.
```
source activate srnaanalyzer
cd scripts
python run.py
```
This should intiate running the analysis pipeline. Immediately you will get a couple questions that you have to answer.
- **Enter the species code (Options: hs, mm, dm, ce, dr or custom):** Answer based on the species, **hs**: human, **mm**: mouse, **dm**: fruit fly, **ce**: *C. elegans*, **dr**: zebra fish or **custom**: any other model organism
- **Bowtie run parameters (default runs in the default mode):** Answer **default** if need to run Bowtie in the default mode. Otherwise specify bowtie parameters according to the Bowtie manual.

Note if the species is **custom** this will prompt two more additional questions:
- **FTP link to the genome to download:** Enter the link to the genome FASTA to download. For instance, if the custom species is yeast here is the Ensembl url to download the genome.
> ftp://ftp.ensembl.org/pub/release-100/fasta/saccharomyces_cerevisiae/dna/Saccharomyces_cerevisiae.R64-1-1.dna_sm.toplevel.fa.gz               

- **FTP link to the miRBase annotation to download:** Enter the link to the corresponding annotation to download from [miRBase](http://www.mirbase.org/ftp.shtml). For instance, if the custom species is Arabidopsis here is the miRBase url to download the annotation.
> ftp://mirbase.org/pub/mirbase/CURRENT/genomes/ath.gff3              

You are all set!!! Let it run. Depending on the size of each file and the number of datasets run time can vary so much!

### Retrieve additional information
It is important to track the number of sequences retained after each step. You can use following bash commands to acheive this.

1. If the directory of interest have a series of *.fastq* files, you can use the following bash command to get read counts saved into a *.txt* file in the same directory. As an example let's save read counts of the *raw_sequences* directory.
```
cd raw_sequences

for i in `ls *.fastq`; do
c=`cat $i | wc -l`
c=$((c/4))
echo $i $c
done > raw_readCounts.txt
```
> Executing the above bash command will save a file named *raw_readCounts.txt* in the *raw_sequences* directory with file name and number of reads in each file.

2. If the directory of interest have a series of *.bam* files, you can use the following bash command that uses [SAMtools](https://github.com/samtools/samtools). As an example let's save mapped read counts of the *star_aligned* directory.
```
cd star_aligned

for i in `ls *.bam`; do
echo ${i} $(samtools view -F 4 -c $i)
done > bam_readCounts_aligned.txt
```
> Executing the above bash command will save a file named *bam_readCounts_aligned.txt* in the *star_aligned* directory with bam file names and number of reads that are mapped to the reference genome. Note that the [sam flag](https://broadinstitute.github.io/picard/explain-flags.html) ***4*** eliminates unmapped sequences from the count, thus giving the total number of sequences that are successfully aligned.     
