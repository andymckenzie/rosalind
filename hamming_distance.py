
string_1 = "CTAGTTCCATCCTTACACAATGGTTACGGCCCTCGAATACCACAGGACCCTAAACCGGGTTTTCAGACGCTATATTTTGGTCTCGCGGCTATATGGGCACTGGTGATTTCACCGGCGCCCCTATAAGCCCGATCCCGCGAAGAGTGCTCCGCCGGCAGGGTTATGAACTTCTTCATACACTTCAAAATGGCGTTCAGCCTTCAGAATCGTCCCGGGTAGAGTGTTAGCACGGCTCAACAAGTCGACATTCGTGGACTTAATACCAAATGGGAGGGTTGGCTTCCACGCTATACTGTCATTTCGCCAGGTTGACCACGCCTTCATGGACCGGACCCCCACGTGTACATGGATAAATCGTGGTGATTATAGCTGGGGTTCAAATATAGATGGGCACGTCCCTGACATCAATATGGAAGCACTATTAGGTCGGCGGCTTGGGCGTGCAACGCGAAGTCACCACCGTCTCGCAATTGGACCAATAGCCCCTCCGATAAGTGAATGCAATTCGAACATCAACGTATAACGCATGATCACCCTAACCATGCAAGGTGGTGTATGGGAGCTGTCGGTGGATTACGGAGGGGCTAGTCCGCAGGGGAAAGTAGACAAGTCGGGGGACACGGTGCTAGTTTTTGTAATTACCAATGGGTTGCTTTACCTACGCGACTTAGCATTTTAATCTCCCACTAAACTTGAGGCCTATTAACAAGGGTCCATTCCCGCGTTTGGGGGTCCCGACTCGTCTTACCATACAGGCCAGGAAGTTACCTGGTCGCTCTCACCACCATTGGTACCGAGAGGGGCTTACTTTCGTTACTCTTCCATCGGATGATTGGGTACAAGTTTAGAATATAACCATCAGTTCGAGGAACTGACAACTCGCCGTACTACAAGTCGCAAACGGCGAGGTGGATTCGTTCTATAGGTGTTCATTCATATACGGGTGAAGTCATGAGGGGGGCTTCCATACAAGCAACATCGGCGGAGCACCAAGATTCTG"
string_2 = "CTATTTCAAACCTTCGGCTATGGTCATGACGATCCCTTCGCAGAGGACCCTTAATCTTGGTTAAACACACTGTACTTTCAAAGCACCGATATCTAGAATCTAGAACGCGCAAACGAACCGCAGTATGCTGGTTACGGCGGATAATGCTTCCCCTGCAGCGTCGAGAACCTCCTTAAGGAAATGAAAAACGCGGTATGCATCAGGCAGCCTCGCAGGTTGACTCTCTGCTTGTCTCAGAAGGTCTACTGACTGGGATTTATTTCTCCCCGGTAGATACGGCGTATAAGCCACAGGCTACCTACAGAAGTGCGTCAGCGGACGAAGTGTACAGCCCCCCGACTGTGCCCGGCAAAGTCGTGTTTATGATATCTGAGTATCATCTAGAAATGACTAAACTCTTACTCCCATTAAAGCGGGTCACTTTATTTTTCGTATTAGCTCAACATCGTGAGCGAACATTCTTGTCTGAAGCAAGTCAGTTCTCCGCCCGATAAGGGAATGCAATTCTGCGTCGGACGTAATCCGCAAAGTAACCCGACTTATAATAAAGGCAGTTGGAGATCTGGGCACGTACATAGGGGCTCGTAGTACGAAGGGGAATATGGTAAATTAGTTATGGGAATAGTTCTTCTCTGGAGTACTGTAAGAGCACCTGTCCCTGTGCGATTGGGCGTGTTAATAGAGTACCGCGTTCTTTGCCAAGTAGCACGGGTTCATCACAATGATCTAGTGGTCCTACAGGTGTGGGCGCACGAGCAAGGCGGTTATTTGTTGTGTTTTGAAACCCTACGGGTCGAAAGACGTCTGGTAATACACCTTCACGCGCCAAAGACTCGGAACGCCCATGGCATATAAAGGAAATCTCAAGTATCTAAACACAGCCACTACTACTAATCGCACGACCCCACTTGCAGTGATTCCGTCAGTGTTCACTCTTGAGTACGAAACGAAGCTCGGCGGGCCTCCCCTTGGGCCTAGCCTCATGCGTTCGACTAAGGTG"

mismatches = 0
for i in xrange(len(string_1)):
    if string_1[i] != string_2[i]:
        mismatches += 1 
        
print mismatches

