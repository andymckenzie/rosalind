from __future__ import division
from Bio import SeqIO 

fasta_input_file = "/Users/amckenz/Dropbox/rosalind/rosalind_gc.txt"
fasta_sequences = SeqIO.parse(open(fasta_input_file),'fasta')

FASTA_names = []
GC_content_list = []
for fasta in fasta_sequences: 
    name = fasta.id
    FASTA_names.append(name)
    GC = 0 
    AT = 0 
    for base in fasta.seq:
        if base == "G":  
            GC += 1 
        if base == "C":
            GC += 1
        if base == "T":
            AT += 1
        if base == "A":
            AT += 1
    GC_content = GC/(GC+AT) * 100 
    GC_content_list.append(GC_content)
    
for i in xrange(len(FASTA_names)):
    print FASTA_names[i]
    print GC_content_list[i]
    
