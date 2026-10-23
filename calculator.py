def add (n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2 

def multiplication(n1,n2):
    return n1 * n2

def division(n1,n2):
    if n2 == 0 :
        raise ValueError("Cannot Divide by 0")
    else:
        return n1 / n2
