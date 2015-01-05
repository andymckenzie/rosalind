sequence = "MA"

codon_table = {
    'A': 4,
    'C': 2,
    'D': 2,
    'E': 2,
    'F': 2,
    'G': 4,
    'I': 3,
    'H': 2,
    'K': 2,
    'L': 6,
    'M': 1,
    'N': 2,
    'P': 4,
    'Q': 2,
    'R': 6,
    'S': 6,
    'T': 4,
    'V': 4,
    'W': 1,
    'Y': 2,
    '*': 3,
}

combinations = 1 
for i in xrange(0, len(sequence)): 
    combinations *= codon_table[sequence[i]]
    
#account for stop codon 
combinations *= codon_table["*"]

combo_mod_mil = combinations % 1000000
    
print combo_mod_mil
