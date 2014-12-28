from Bio import SeqIO
from Bio.Seq import Seq
import warnings
from Bio import BiopythonWarning

#I don't feel like seeing warnings right now
warnings.simplefilter('ignore', BiopythonWarning)

seq = Seq("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
#in case you want to read in the dataset from a file
#seq = SeqIO.read("/Users/amckenz/Dropbox/rosalind/test_orf.fasta", "fasta")

#translation table
table = 1

#from wikipedia 
start_wiki = ["ATG"]
stop_wiki = ["TAA", "TGA", "TAG"]

#can also add translate = to_stop = True, but this reduces the total down to one protein per 
protein_list = []
for strand, nuc in [(+1, seq), (-1, seq.reverse_complement())]:
    for frame in range(3):
        start_sites = []
        stop_sites = []
        real_starts = []
        real_stops = []
        for i in xrange(0,len(nuc),3):
            if str(nuc[i+frame:i+3+frame]) in start_wiki: 
                start_sites.append(i)
               # print i, str(nuc[i+frame:i+3+frame]), "start codon"
            if str(nuc[i+frame:i+3+frame]) in stop_wiki: 
                stop_sites.append(i)
                #print i, str(nuc[i+frame:i+3+frame])
        for start in start_sites: 
            #this only works because search is linear and monotonic
            for stop in stop_sites: 
                if stop > start: 
                    real_stops.append(stop) 
                    real_starts.append(start)
                    break
        print real_starts            
        print real_stops
        for i in range(len(real_starts)): 
            protein = str(*nuc[frame+real_starts[i]:frame+real_stops[i]].translate(table).split("*"))
            protein_list.append(protein)
        
for protein_i in list(set(protein_list)): 
    print protein_i