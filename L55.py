from tba_helper import *

LANG_NO=55
OUTPUT_FILE=f"{PREFIX}{LANG_NO}.txt"

lang = ["a", "b"]
langpow8 = lang_pow(lang, 6)
l55pow8 = {string for string in langpow8 if prefix_check(string)}
res = sorted(l55pow8, key= lambda x: (len(x), x))

output_answer(res, OUTPUT_FILE, 5, 10)