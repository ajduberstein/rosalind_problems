# Simulation of gene pool
def mendelian(k,m,n):
        gene_pool = []
        for i in xrange(0,k):
                gene_pool.append(('HH'))
        for i in xrange(0,m):
                gene_pool.append(('Hh'))
        for i in xrange(0,n):
                gene_pool.append(('hh'))
        gene_pool = tuple(gene_pool)
        pairings = []
        for x in itertools.combinations(gene_pool, 2):
                pairings.append(x)
        dominant_pairs, total_pairs = 0, 0
        for mother, father in pairings:
                inheritance = (x+y for x in mother for y in father)
                for gene_set in inheritance:
                        if 'H' in gene_set: dominant_pairs += 1
                        total_pairs+=1
        print float(dominant_pairs)/total_pairs
