import os
import glob
import subprocess as sp
import ColorTextWriter

class CutAdapt:

    def __init__(self, home_dir, input_dir,  extensions):
        self.home_dir = home_dir
        self.input_dir = input_dir
        self.extensions = extensions

    def cutadapt(self):

        outdir = os.path.join(self.home_dir, 'cutadapt')
        if not os.path.isdir(outdir): os.mkdir(outdir)

        ctw = ColorTextWriter.ColorTextWriter()

        print(ctw.CBEIGE + ctw.CBOLD + 'Running CutAdapt ...' + ctw.CEND + '\n')

        fastq_list = sorted(glob.glob(self.input_dir + '*R1.fastq'))

        for i in fastq_list:
            print('\n' + ctw.CBEIGE + ctw.CBOLD + 'CutAdapting: ' + ctw.CBLUE + os.path.basename(i) + ctw.CBEIGE + ctw.CBOLD + ' ...' + ctw.CEND + '\n')

            output_file = outdir + '/' + os.path.basename(i).split('.fastq')[0] + '_trimmed' + self.extensions[0]
            illumina_adap = 'AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC'

            command = [
                'cutadapt -m 18 -M 30 -u 4',
                '-a NNNN' + illumina_adap,
                '-o', output_file, i,
                '>', output_file.split('_trimmed')[0] + '_trim.matrics' + self.extensions[3]
            ]

            command = ' '.join(command)
            sp.check_call(command, shell=True)

        print('\n' + ctw.CRED + ctw.CBOLD + 'CutAdapt Trimming Completed!!!' + ctw.CEND)