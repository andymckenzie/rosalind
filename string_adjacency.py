from Bio import SeqIO

#don't feel like seeing warnings right now?
import warnings
warnings.simplefilter('ignore', FutureWarning)

overlap_amount = 3

sequences = list(SeqIO.parse("/Users/amckenz/Dropbox/rosalind/string_adjacency_fas.fasta", "fasta"))

edge_list = []
for i in sequences: 
    for j in sequences: 
        #check that the sequences are not identical to prevent directed loops 
        if i.seq != j.seq:  
            location_of_max_overlap 
            i_ending_rev = i.seq[len(i.seq)-overlap_amount:len(i.seq)]
            j_ending = j.seq[0:overlap_amount]
            if str(i_ending_rev) == str(j_ending):
                edge_list.append((i.id, j.id))
            
for edge in edge_list: 
    print ' '.join(edge)