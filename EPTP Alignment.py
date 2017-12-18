from Bio import pairwise2
import os
from Bio import SeqIO
from Bio.pairwise2 import format_alignment
os.chdir('C:/Users/bag019/Dropbox/Intro To Bioinf/FASTA Prot')
seq=[]
i_d = []
def local(start, end):
    end +=1
    try:
        alignment = pairwise2.align.localxx(seq[0][start:end], seq[1][start:end])
        print(format_alignment(*alignment[0]))    
    except:
       print("Try Again")
for record in SeqIO.parse("Human 1.fasta", "fasta"):
    seq.append(record.seq)
    i_d.append(record.id)
for record in SeqIO.parse("Human 2.fasta", "fasta"):
    seq.append(record.seq)
    i_d.append(record.id)



