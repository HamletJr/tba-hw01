from tba_helper import *

LANG_NO=41
OUTPUT_FILE=f"{PREFIX}{LANG_NO}.txt"

l1 = ["ab", "aca", "b", "ccab"]
l4 = ["ca", "aab", "b", "caac"]

l1pow4 = lang_pow(l1, 4)
l4pow4 = lang_pow(l4, 4)
l4pow4reverse = reverse(l4pow4)
l4pow4reverseconcatl1pow4 = concat(l4pow4reverse, l1pow4)
res = sorted(l4pow4reverseconcatl1pow4, key= lambda x: (len(x), x))

output_answer(res, OUTPUT_FILE, 5, 10)