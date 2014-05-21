def find_motif(haystack, needle):
    match_indices = []
    i = 1
    while(len(haystack) >= len(needle)):
        if needle == haystack[:len(needle)]: match_indices.append(i)
        haystack = haystack[1:]
        i+=1
    print match_indices
    return ' '.join([str(x) for x in match_indices])
