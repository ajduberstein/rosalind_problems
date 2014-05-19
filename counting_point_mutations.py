def hamming_dist(str1, str2):
        hd = 0
        for i in xrange(0, len(str1)):
                if str1[i] != str2[i]:
                        hd += 1
        return hd
