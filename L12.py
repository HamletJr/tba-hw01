from tba_helper import *

LANG_NO=12
OUTPUT_FILE=f"{PREFIX}{LANG_NO}.txt"

l2 = ["ac", "c", "bab", "bcaa"]
l3 = ["bb", "bac", "a", "cbab"]
l8 = ["ba", "ac"]

l2pow3 = concat(concat(l2, l2), l2)
l3pow2 = concat(l3, l3)
l2concatl3 = concat(l2pow3, l3pow2)
l8pow3 = lang_pow(l8, 7)
l2l3diffl8 = l2concatl3.difference(l8pow3)
res = sorted(l2concatl3, key= lambda x: (len(x), x))

output_answer(res, OUTPUT_FILE, 5, 10)