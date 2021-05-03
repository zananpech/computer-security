from fast_modular_expo import fast_modular_exponentiation

def a_d_test(a, d, m):

    if pow(a, d) % m == 1:
        return True
    return False

def a_2id_test(a, d, m, steps):

    for i in range(steps):
        if pow(a, pow(2,i)*d) % m == m - 1:
            return True
    return False


def miller_rabin_test(n, a=5):

  
    p = n-1
    S = 0
    while(p % 2 != 0):
        p = p//2
        S += 1
    
    if fast_modular_exponentiation(a, p, n) == 1:
        return True
    
    else:
        for i in range(1,S):
            if n - 1 == pow(a, pow(2,i) * p):
                return True
        return False

    return False



if __name__ == "__main__":
    m = 9752768741493992298817014200893084562741439842202317396386675680310424506116191531727817693405484670693201818814744543129154340649150767289498535766493955187357401718419221597009418058055276301253975493129853051188472215593215763551743278496738085033635815236393037486113907123707318944576594729426973 
    print(miller_rabin_test(m, a=2))
