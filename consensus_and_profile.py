#In progress
def prune(input_dset):
        f = input_dset.replace('\r\n','')[1:]
        f = f.split('>')
        f = [list(x[13:]) for x in f]
        import copy
        transposed = copy.deepcopy(f)
        for x in xrange(0,len(f)):
                for y in range(0,len(f)):
                        transposed[y][x] = f[x][y]
        return transposed

def consensus_and_profile(dna_strings):
        from collections import defaultdict
        profile_matrix = defaultdict(list)
        building_blocks = ('A','T','C','G')
        #Profile matrix
        for sequence in dna_strings:
                for i in building_blocks:
                        profile_matrix[i].append(sequence.count(i))
        #Consensus string
        consensus_string = ''
        for i in xrange(0,len(dna_strings)):
                curr_max = ('',0)
                for j in building_blocks:
                        if profile_matrix[j][i] >= curr_max[1]:
                                curr_max = (j, profile_matrix[j][i])
                consensus_string += curr_max[0]
        print consensus_string
        profile_matrix = str(profile_matrix).replace(', \'','\n')
        return ''.join([x for x in profile_matrix if x in '\n: 1234567890ACTG']).strip()
