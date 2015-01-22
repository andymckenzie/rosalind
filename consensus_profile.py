from Bio import SeqIO

filename = "/Users/amckenz/Dropbox/rosalind/rosalind_cons.txt"

length_sequences = 0
for record in SeqIO.parse(filename, 'fasta'):
    length_sequences = len(record.seq)
    break

A_list = [0 for x in xrange(length_sequences)]
C_list = [0 for x in xrange(length_sequences)]
G_list = [0 for x in xrange(length_sequences)]
T_list = [0 for x in xrange(length_sequences)]
for record in SeqIO.parse(filename, 'fasta'):
    for i in range(len(record.seq)): 
        if record.seq[i] == "A": 
            A_list[i] += 1
        if record.seq[i] == "C": 
            C_list[i] += 1
        if record.seq[i] == "G": 
            G_list[i] += 1
        if record.seq[i] == "T": 
            T_list[i] += 1

#create the conesnsus sequence
consensus_sequence = "" 
for i in range(length_sequences):
    print i, A_list[i], C_list[i], G_list[i], T_list[i]
    if A_list[i] >= C_list[i] and A_list[i] >= G_list[i] and A_list[i] >= T_list[i]:
        consensus_sequence += "A"
        next
    if C_list[i] > A_list[i] and C_list[i] >= G_list[i] and C_list[i] >= T_list[i]:
        consensus_sequence += "C"
        next
    if G_list[i] > C_list[i] and G_list[i] > A_list[i] and G_list[i] >= T_list[i]:
        consensus_sequence += "G"
        next
    if T_list[i] > C_list[i] and T_list[i] > G_list[i] and T_list[i] > A_list[i]:
        consensus_sequence += "T"
        next
        
print consensus_sequence
print "A:", ' '.join(map(str, A_list))
print "C:", ' '.join(map(str, C_list))
print "G:", ' '.join(map(str, G_list))
print "T:", ' '.join(map(str, T_list))