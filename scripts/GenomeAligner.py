import os
import glob
import subprocess as sp
import ColorTextWriter

class GenomeAligner:

    def __init__(self, home_dir, input_dir, threads, bt_index, bt_parameter, extensions):
        self.home_dir = home_dir
        self.input_dir = input_dir
        self.threads = threads
        self.bt_index = bt_index
        self.bt_parameter = bt_parameter
        self.extensions = extensions

    def aligner(self):

        outdir = os.path.join(self.home_dir, 'bt_aligned')
        if not os.path.isdir(outdir): os.mkdir(outdir)

        fastq_list = sorted(glob.glob(self.input_dir + '*.fastq'))

        ctw = ColorTextWriter.ColorTextWriter()

        print(ctw.CBEIGE + ctw.CBOLD + 'Running Bowtie Aligner ...' + ctw.CEND + '\n')

        for i in fastq_list:
            print('\n' + ctw.CBEIGE + ctw.CBOLD + 'Mapping: ' + ctw.CBLUE + os.path.basename(i) + ctw.CBEIGE + ctw.CBOLD + ' ...' + ctw.CEND + '\n')

            output_file = outdir + '/' + os.path.basename(i).split('.fastq')[0] + '_aligned' + self.extensions[4]

            command = [
                'bowtie',
                '-p', self.threads, '-x', self.bt_index + 'bt_index',
                self.bt_parameter, '-q', i,
                '-S', output_file,
                '2>', output_file.split(self.extensions[4])[0] + self.extensions[3]
            ]

            command = ' '.join(command)
            sp.check_call(command, shell=True)

        print('\n' + ctw.CRED + ctw.CBOLD + 'Sequence Alignment Completed!!!' + ctw.CEND + '\n')