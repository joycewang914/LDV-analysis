# download LDV relative abundance files from scratch

# if done manually, this is what the command looks like:
# download /scratch/esnitkin_root/esnitkin/apirani/Project_VRE_metagenomics_analysis/2021_06_03_LDV_Simulation/data/Part1/0.001perc/A_varcall_result/A_LDV_abund_frequency.csv ../../genome_alignments/MI_simulations "specific output name"

import os, argparse,re

parser = argparse.ArgumentParser(description='This script takes a file')

parser.add_argument('-input', action = 'store', dest='LDV_file', help ='text file containing location of LDV data')
args = parser.parse_args()

input = args.LDV_file

csv_files = open(input, "r")
for i in csv_files:

    f = i.split('/')
    
    if len(f) == 12:
        ff = f[11]
        ff = ff.strip('\n')
        ff = ff.replace('.csv','')
        pct = f[9]
        pct = pct.strip('\n')
        output = '../genome_alignments/MI_simulations/' + str(ff) + '_' + str(pct) + '.csv'

        
    elif len(f) == 11:
        ff = f[10]
        ff = ff.strip('\n')
        ff = ff.replace('.csv', '')
        output = '../genome_alignments/MI_simulations/' + str(ff) + '.csv'
       
    input_dir = i.strip('\n')

    command = "scp -r wangjoy@greatlakes-xfer.arc-ts.umich.edu:%s %s" % (input_dir, output)
    print(command)
    os.system(command)
