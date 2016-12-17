
mass = read.table("/Users/amckenz/Desktop/rosalind/aa_mass.tsv")

protein = "SKADYEK"
protein_split = strsplit(protein, split = "")[[1]]

protein_mass = 0
for(i in 1:length(protein_split)){
  protein_mass = protein_mass + mass[mass$V1 == protein_split[i], "V2"]
}
format(protein_mass, nsmall = 5)
