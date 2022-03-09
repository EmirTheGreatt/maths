#euclidian division
noremainderdivision=lambda x,y:x//y
#remainder
remain=lambda x,y:x%y
#greatest common divisor
def gcd(a,b):
    aa=abs(a)
    bb=abs(b)
    if aa%bb==0:
        return bb
    if bb%aa==0:
        return aa
    if aa>bb:
        return gcd(aa%bb,bb)
    else:
        return gcd(bb%aa,aa)
#least common multiple
lcm=lambda a,b:a*b/gcd(a,b)
