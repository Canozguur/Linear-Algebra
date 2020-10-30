def transposed(*args, x, y):
    if x == 2 and y == 2:
        a, b, c, d = args
        trans_c = c
        c = b
        b = trans_c
        print("*" * 25)
        print(str(a), str(b) + "\n" + str(c), str(d))
        print("*" * 25)

    if x == 2 and y == 3:
        a, b, c, d, e, f = args
        trans_b = b
        trans_c = c
        trans_d = d
        trans_e = e
        trans_f = f
        c = b
        e = trans_c
        b = d
        d = trans_e
        print("*" * 25)
        print(str(a), str(b) + "\n" + str(c), str(d) + "\n" + str(e), str(f))
        print("*" * 25)
        return three_to_two

    if x == 3 and y == 2:
        a, b, c, d, e, f = args
        trans_b = b
        trans_c = c
        trans_d = d
        trans_e = e
        trans_f = f
        d = b
        b = c
        c = e
        e = trans_d
        print("*" * 25)
        print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f))
        print("*" * 25)

        # print(two_to_three[0][0],str(two_to_three[0][1]), str(two_to_three[0][2]) + "\n" + str(two_to_three[1][0]), str(two_to_three[1][1]),str(two_to_three[1][2]))
        return two_to_three
    if x == 3 and y == 3:
        a, b, c, d, e, f, g, h, j = args
        trans_b = b
        trans_c = c
        trans_d = d
        trans_e = e
        trans_f = f
        b = d
        c = g
        d = trans_b
        e = e
        f = h
        g = trans_c
        h = trans_f
        j = j
        #print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))

        return a, b, c, d, e, f, g, h, j  # maybe this one is gonna change or not


def found_of_trace(a, b, c, d):
    return a + d


def found_determinant_of_matrix(*args, x, y):
    if x == 2 and y == 2:
        a, b, c, d = args
        determinant = (a * d) - (b * c)
    elif x == 3 and y == 3:
        a, b, c, d, e, f, g, h, j = args
        # determinant = [a*[[e*j]-[f*h]]]+[b*[[d*j]-[f*g]]]+[c[[d*h]-[e*g]]]
        determinant = (a * ((e * j) - (f * h))) + -(b * ((d * j) - (f * g))) + (c * ((d * h) - (e * g)))
        print(determinant)
    return determinant


def minors(*args, x, y):
    if x == 3 and y == 3:
        a, b, c, d, e, f, g, h, j = args
        trans_a = a
        trans_b = b
        trans_c = c
        trans_d = d
        trans_e = e
        trans_f = f
        trans_g = g
        trans_h = h
        trans_j = j

        a = (trans_e * trans_j) - (trans_f * trans_h)
        b = (trans_d * trans_j) - (trans_f * trans_g)
        c = (trans_d * trans_h) - (trans_e * trans_g)
        d = (trans_b * trans_j) - (trans_c * trans_h)
        e = (trans_a * trans_j) - (trans_c * trans_g)
        f = (trans_a * trans_h) - (trans_b * trans_g)
        g = (trans_b * trans_f) - (trans_c * trans_e)
        h = (trans_a * trans_f) - (trans_c * trans_d)
        j = (trans_a * trans_e) - (trans_b * trans_d)
        return a, b, c, d, e, f, g, h, j
        #a, b, c, d, e, f, g, h, j = cofactors(a, b, c, d, e, f, g, h, j, x=3, y=3)
        #a, b, c, d, e, f, g, h, j = transposed(a, b, c, d, e, f, g, h, j, x=3, y=3)

def adjugate(*args, x, y):
    if x == 3 and y == 3:
        determinant = found_determinant_of_matrix(*args,x=3,y=3)
        a, b, c, d, e, f, g, h, j = minors(*args,x=3,y=3)
        #print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))
        a, b, c, d, e, f, g, h, j = cofactors(a, b, c, d, e, f, g, h, j,x=3,y=3)
        #print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))
        a, b, c, d, e, f, g, h, j = transposed(a, b, c, d, e, f, g, h, j,x=3,y=3)
        #print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))
        a, b, c, d, e, f, g, h, j = a/determinant, b/determinant, c/determinant, d/determinant, e/determinant, f/determinant, g/determinant, h/determinant, j /determinant
        print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))


def cofactors(*args, x, y):
    if x == 3 and y == 3:
        a, b, c, d, e, f, g, h, j = args
        a, b, c, d, e, f, g, h, j = a, -b, c, -d, e, -f, g, -h, j
        #print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))

        return a, b, c, d, e, f, g, h, j


def inverse_of_matrix(a, b, c, d):
    det = found_determinant_of_matrix(a, b, c, d, x=2, y=2)
    b = b * (-1) / det
    c = c * (-1) / det
    trans = a / det
    a = d / det
    d = trans
    print(str(a), str(b) + "\n" + str(c), str(d))


a, b, c, d, e, f, g, h, j = 0, 1, 2, 3, 4, 5, 6, 7, 8

two_to_two = [[a, b],
              [c, d]]

three_to_two = [[a, b],
                [c, d],
                [e, f]]

two_to_three = [[a, b, c],
                [d, e, f]]

three_to_three = [[a, b, c],
                  [d, e, f],
                  [g, h, j]]

print(three_to_three[2][2])
transposed(a, b, c, d, x=2, y=2)
transposed(a, b, c, d, e, f, x=2, y=3)
transposed(a, b, c, d, e, f, x=3, y=2)  # this one is okey

print("a,b,c\n" + "d,e,f\n" + "g,h,j\n")
print("Choose your size of matrix\n")

x = int(input("size of row"))
y = int(input("size of column"))

if x == 2 and y == 2:  # 2  ye 2 olan matrixlerde yapılacak işlemeler için
    a = int(input("a enter value "))
    b = int(input("b enter value "))
    c = int(input("c enter value "))
    d = int(input("d enter value "))
    trace = found_of_trace(a,b,c,d)
    pass
if x == 2 and y == 3:  # 2  ye 3 olan matrixlerde yapılacak işlemeler için
    a = int(input("a enter value "))
    b = int(input("b enter value "))
    c = int(input("c enter value "))
    d = int(input("d enter value "))
    e = int(input("e enter value "))
    f = int(input("f enter value "))
    pass
if x == 3 and y == 2:  # 3  ye 2 olan matrixlerde yapılacak işlemeler için
    a = int(input("a enter value  "))
    b = int(input("b enter value  "))
    c = int(input("c enter value  "))
    d = int(input("d enter value  "))
    e = int(input("e enter value  "))
    f = int(input("f enter value  "))
    pass
if x == 3 and y == 3:  # 3  ye 3 olan matrixlerde yapılacak işlemeler için
    a = int(input("a enter value  "))
    b = int(input("b enter value  "))
    c = int(input("c enter value  "))
    d = int(input("d enter value  "))
    e = int(input("e enter value  "))
    f = int(input("f enter value  "))
    g = int(input("g enter value  "))
    h = int(input("h enter value  "))
    j = int(input("j enter value  "))
    adjugate(a, b, c, d, e, f, g, h, j, x=3, y=3)
    found_determinant_of_matrix(a, b, c, d, e, f, g, h, j, x=3, y=3)

#inverse_of_matrix(a, b, c, d)
"""
a = int(input("a değeri giriniz "))
b = int(input("b değeri giriniz "))
c = int(input("c değeri giriniz "))
d = int(input("d değeri giriniz "))
e = int(input("e değeri giriniz "))
f = int(input("f değeri giriniz "))
g = int(input("g değeri giriniz "))
j = int(input("j değeri giriniz "))
"""
