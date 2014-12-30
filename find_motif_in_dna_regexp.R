input_string = ""

pattern_string = "(?=AGCTGGAAG)"

indices = gregexpr(pattern = pattern_string,input_string,perl= TRUE)