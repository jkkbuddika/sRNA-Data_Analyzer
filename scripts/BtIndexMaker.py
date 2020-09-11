import os
import subprocess as sp
import ColorTextWriter

class BtIndexMaker:

    def __init__(self, home_dir, threads, genes_fa, extensions):
        self.home_dir = home_dir
        self.threads = threads
        self.genes_fa = genes_fa
        self.extensions = extensions

    def bt2_index_maker(self):

        outdir = os.path.join(self.home_dir, 'bt_index')
        if not os.path.isdir(outdir): os.mkdir(outdir)

        ctw = ColorTextWriter.ColorTextWriter()

        if len(os.listdir(outdir + '/')) == 0:

            print(ctw.CBEIGE + ctw.CBOLD + 'Generating Bowtie Genome Indices ...' + ctw.CEND + '\n')

            bt2_index_path = outdir + '/' + 'bt_index'

            command = [
                'bowtie-build',
                '--threads', self.threads, '-q',
                self.genes_fa, bt2_index_path
            ]

            command = ' '.join(command)
            sp.check_call(command, shell=True)

            print('\n' + ctw.CRED + ctw.CBOLD + 'Bowtie Genome Indices Generated!!!' + ctw.CEND + '\n')

        else:
            print(ctw.CRED + "Destination directory contain files. Ignoring Bowtie Genome Index generation!!!" + ctw.CEND + '\n')