
library(gtools)

setwd("/Users/amckenz/Desktop/rosalind")

nperm = 5

combos = permutations(nperm, nperm)

write.table(data.frame(nrow(combos)), file = "perms_res", row.names = FALSE,
  col.names = FALSE, quote = FALSE)
write.table(data.frame(combos), file = "perms_res", row.names = FALSE,
  col.names = FALSE, quote = FALSE, sep = " ", append = TRUE)
