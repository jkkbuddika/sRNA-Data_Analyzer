import os
import glob
import subprocess as sp
import ColorTextWriter

class SamTools():

    def __init__(self, home_dir, input_dir, threads, extensions):
        self.home_dir = home_dir
        self.input_dir = input_dir
        self.threads = threads
        self.extensions = extensions

    def sam_sorting(self):

        outdir = os.path.join(self.home_dir, 'sam_sorted')
        if not os.path.isdir(outdir): os.mkdir(outdir)

        bam_files = sorted(glob.glob(self.input_dir + '*.bam'))

        ctw = ColorTextWriter.ColorTextWriter()

        for i in bam_files:
            print(ctw.CRED + 'Filtering and Sorting: ' + ctw.CBLUE + os.path.basename(i) + ctw.CRED + ' ...' + ctw.CEND + '\n')

            output_file = outdir + '/' + os.path.basename(i).split('.bam')[0] + 'sorted' + self.extensions[4]

            command = [
                'samtools sort -@', self.threads, i, '|',
                'samtools view -F 4 -O BAM', '-@', self.threads,
                '-o', output_file
            ]

            command = ' '.join(command)
            sp.check_call(command, shell=True)

            print('\n' + ctw.CRED + 'Indexing: ' + ctw.CBLUE + os.path.basename(output_file) + ctw.CRED + ' ...' + ctw.CEND + '\n')

            command = [
                'samtools index', output_file
            ]

            command = ' '.join(command)
            sp.check_call(command, shell=True)

        print(ctw.CBEIGE + ctw.CBOLD + 'Filtering, Sorting and Indexing Completed!!!' + ctw.CEND)
