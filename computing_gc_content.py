def dna_id(input):
        strs=[x for x in input.replace('\n','').split('>') if x is not '']
        curr_max = ('',0)
        for st in strs:
                vals = {'GC':0,'LEN':0}
                for itm in ('A','C','G','T'):
                        num_let = st.count(itm)
                        if itm in 'GC':
                                vals['GC']+=num_let
                        vals['LEN']+=num_let
                gc_cnt = float(vals['GC'])/vals['LEN']
                if gc_cnt > curr_max[1]:
                        str_name = re.sub('[ACTG]','',st)
                        curr_max = (str_name, gc_cnt)
        print curr_max[0]
        print curr_max[1]*100.00000
