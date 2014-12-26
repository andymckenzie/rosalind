#basically all you need for this is the R fxn gregexpr, with perl = T

input_string = ""
pattern_string = "(?=)"
indices = gregexpr(pattern = pattern_string, input_string, perl= TRUE)
