from tba_helper import *

LANG_NO=31
OUTPUT_FILE=f"{PREFIX}{LANG_NO}.txt"

l3 = ["bb", "bac", "a", "cbab"]
l5 = ["bc", "c", "bca", "cbac"]
l7 = ["ab", "bc"]
l8 = ["ba", "ac"]

l3unionl5 = set(l3).union(l5)
l8concatl3unionl5 = concat(l8, lang_pow(l3unionl5, 6))
l7pow6 = lang_pow(l7, 6)
l8concatl3unionl5diffl7pow6 = l7pow6.difference(l8concatl3unionl5)
res = sorted(l8concatl3unionl5diffl7pow6, key= lambda x: (len(x), x))

output_answer(res, OUTPUT_FILE, 5, 10)