def lang_pow(l, n):
    if n == 0:
        return {""}
    return {i + j for i in l for j in lang_pow(l, n-1)}.union(lang_pow(l, n-1))

def reverse(l):
    return {i[::-1] for i in l}

def concat(l1, l2):
    return {i + j for i in l1 for j in l2}

def prefix_check(string: str):
    for i in range(1, len(string) + 1):
        if string[:i].count("a") < 2 * string[:i].count("b"):
            return False
    return True

def output_answer(res_lang, output_file, min_length, word_count):
    count = 0
    with open(output_file, "w") as f:
        for string in res_lang:
            if len(string) >= min_length:
                f.write(string)
                count += 1
                if count == word_count:
                    break
                f.write("\n")

PREFIX="EN25"