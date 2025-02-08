from tba_helper import *

LANG_NO=51
OUTPUT_FILE=f"{PREFIX}{LANG_NO}.txt"

lang = ["a", "abbb"]

l51 = lang_pow(lang, 6)
res = sorted(l51, key= lambda x: (len(x), x))
res_filtered = []
for string in res:
    if (string.count("b") * 5) >= (3 * string.count("a") + 2):
        res_filtered.append(string)

output_answer(res_filtered, OUTPUT_FILE, 5, 10)