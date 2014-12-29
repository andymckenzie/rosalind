from Bio.Seq import Seq
from Bio.Alphabet import generic_rna
messenger_rna = Seq("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA", generic_rna)
test_result = messenger_rna.translate()
print test_result