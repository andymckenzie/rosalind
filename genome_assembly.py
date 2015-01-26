from Bio import SeqIO

#don't feel like seeing warnings right now?
import warnings
warnings.simplefilter('ignore', FutureWarning)

sequences = list(SeqIO.parse("/Users/amckenz/Dropbox/rosalind/genome_assembly_test.fasta", "fasta"))

#read in the sequences .... 
#find a directed list of the longest overlaps for each string, in order, as well as an "initiator" string, which has no parent
#store the locations in each of the parent and child that correspond to the longest string, as tuples in a separate list 
#this makes some assumptions, eg that the strings are relatively similar length, but that should be OK

edge_list = []
location_overlap_tuple_list = []
location_max_overlap = []
edge_dictionary = {}
size_overlap_dictionary = {}
#i = parent, j = child; if found_flag = 0, then that is the terminator 
for i_index, i in enumerate(sequences): 
    max_overlap = 0 
    location_max_overlap = 0
    index_of_max_overlap = 0 
    found_flag = 0 
    print i.seq, "i"
    #maybe create a dict that each of indices of the sequences can access and that gives its corresponding max overlap node
    for j_index, j in enumerate(sequences): 
        #check that the sequences are not identical to prevent directed loops 
        if i.seq != j.seq: 
            for k in xrange(1, len(i.seq), 1):     
                if k >= ((len(i.seq)/2) - 1) and str(j.seq).startswith(str(i.seq)[len(i.seq)-k:len(i.seq)]) and k > max_overlap:
                    #k >= len(i.seq)/2 and 
                    found_flag = 1
                    index_of_max_overlap = j_index
                    location_max_overlap = k
                    max_overlap = k 
                    print str(j.seq), str(i.seq)[len(i.seq)-k:len(i.seq)]
    if found_flag == 1:
        edge_list.append(index_of_max_overlap)
        edge_dictionary[str(i_index)] = str(index_of_max_overlap)
        size_overlap_dictionary[str(i_index)] = location_max_overlap
        #sequences[index_of_max_overlap]
    #set this node as the intitiator 
    if found_flag == 0: 
        edge_dictionary[str(i_index)] = "terminator"
        size_overlap_dictionary[str(i_index)] = location_max_overlap
        
                
print edge_dictionary  
print size_overlap_dictionary          
#to loop over the dictionary 
#start with the initiator as the "first parent"
#then, for each string, the parent becomes the next child 
superstring = ""
next_child = ""   
parent = ""
for i in range(len(sequences)): 
    if i == 0: 
        #get terminator index to start 
        terminator_key = edge_dictionary.keys()[edge_dictionary.values().index("terminator")]
        superstring += sequences[int(terminator_key)].seq
        next_child = terminator_key
    if i > 0: 
        parent = edge_dictionary.keys()[edge_dictionary.values().index(next_child)]
        next_child = parent
        string_to_chomp = str(sequences[int(next_child)].seq)
        print string_to_chomp
        string_to_add = string_to_chomp[0:len(string_to_chomp)-(int(size_overlap_dictionary[parent]))]
        print string_to_add
        superstring = string_to_add + superstring
    print i, next_child, parent, superstring

print superstring
    

    

    
    
    
