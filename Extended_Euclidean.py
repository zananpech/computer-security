

def extended_euclidean(a, b):

    if a == 0 : 
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b%a, a)
    
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

if __name__ == "__main__":
    print(extended_euclidean(a=100, b=9))