def found_of_trace(a,b,c,d):
    return a + d

def found_determinant_of_matrix(a, b, c, d):
    determinant = (a * d) - (b * c)
    return determinant
def inverse_of_matrix(a,b,c,d):
    det = found_determinant_of_matrix(a,b,c,d)
    b = b * (-1) / det
    c = c * (-1) / det
    trans = a / det
    a = d / det
    d = trans
    print(str(a),str(b)+"\n"+str(c),str(d))

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

print("a,b,c\n" + "d,e,f\n" + "f,g,j\n")
print("Choose your size of matrix\n")

x = int(input("size of row"))
y = int(input("size of column"))

if x == 2 and y == 2:  # 2  ye 2 olan matrixlerde yapılacak işlemeler için
    a = int(input("a değeri giriniz "))
    b = int(input("b değeri giriniz "))
    c = int(input("c değeri giriniz "))
    d = int(input("d değeri giriniz "))
    trace = found_of_trace(a,b,c,d)
    pass
if x == 2 and y == 3:  # 2  ye 3 olan matrixlerde yapılacak işlemeler için
    a = int(input("a değeri giriniz "))
    b = int(input("b değeri giriniz "))
    c = int(input("c değeri giriniz "))
    d = int(input("d değeri giriniz "))
    e = int(input("e değeri giriniz "))
    f = int(input("f değeri giriniz "))
    pass
if x == 3 and y == 2:  # 3  ye 2 olan matrixlerde yapılacak işlemeler için
    a = int(input("a değeri giriniz "))
    b = int(input("b değeri giriniz "))
    c = int(input("c değeri giriniz "))
    d = int(input("d değeri giriniz "))
    e = int(input("e değeri giriniz "))
    f = int(input("f değeri giriniz "))
    pass
if x == 3 and y == 3:  # 3  ye 3 olan matrixlerde yapılacak işlemeler için
    a = int(input("a değeri giriniz "))
    b = int(input("b değeri giriniz "))
    c = int(input("c değeri giriniz "))
    d = int(input("d değeri giriniz "))
    e = int(input("e değeri giriniz "))
    f = int(input("f değeri giriniz "))
    g = int(input("g değeri giriniz "))
    j = int(input("j değeri giriniz "))
    pass
inverse_of_matrix(a,b,c,d)
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
