
library(gtools)
library(bayesbio)
library(seqinr)


setwd("/Users/amckenz/Desktop/rosalind")

ex = read.fasta("/Users/amckenz/Downloads/rosalind_revp.txt")
dna = toupper(paste(ex[[1]], sep = "", collapse = ""))

rev_comp = data.frame(
  init = c("A", "C", "G", "T"),
  res = c("T", "G", "C", "A"))

identify_perms <- function(length){
  combos2 = permutations(4, length, c("A", "C", "G", "T"), repeats.allowed = TRUE, set = TRUE)
  combos2 = apply(combos2, 1, paste, sep = "", collapse = "")
  combos4 = vector()
  for(i in 1:length(combos2)){
    tmp_combos = vector()
    combos_split = strsplit(combos2[i], split = "")[[1]]
    for(j in length(combos_split):1){
      rev_comp_letter = rev_comp[rev_comp$init == combos_split[j], "res"]
      tmp_combos = c(tmp_combos, rev_comp_letter)
    }
    combos4[i] = paste0(combos2[i], paste0(tmp_combos, collapse = ""), collapse = "")
  }
  return(combos4)
}

combos4 = identify_perms(2)
combos6 = identify_perms(3)
combos8 = identify_perms(4)
combos10 = identify_perms(5)
combos12 = identify_perms(6)

list_restrict = list(combos4, combos6, combos8, combos10, combos12)
length_restrict = c(4, 6, 8, 10, 12)

matches = data.frame(x= numeric(0), y= numeric(0))
for(j in 1:length(list_restrict)){
  for(i in 1:length(list_restrict[[j]])){
    if(grepl(list_restrict[[j]][i], dna)){
      print(list_restrict[[j]][i])
      match_locs = as.numeric(gregexpr(list_restrict[[j]][i], dna)[[1]])
      for(k in 1:length(match_locs)){
        matches_tmp = cbind(match_locs[k], length_restrict[j])
        matches = rbind(matches, matches_tmp)
      }
    }
  }
}

matches = matches[order(as.numeric(matches[,1])), ]

write.table(matches, file = "restricts_res.txt", row.names = FALSE,
  col.names = FALSE, quote = FALSE, sep = " ")
