def multiplication(first, second):
    row_of_first = len(first) - 1
    row_of_second = len(second) - 1
    column_of_first = len(first[0]) - 1
    column_of_second = len(second[0]) - 1

    # print(row_of_first)
    # print(row_of_second)
    # print(column_of_first)
    # print(column_of_second)

    if row_of_first == 1 and column_of_first == 2:  # first ones are completed 2x1--2x2--2x3
        if row_of_second == 2 and column_of_second == 1:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1]
            result = [[0, 0],
                      [0, a]]
            print("*" * 20)
            print(a)
            print("*" * 20)
        elif row_of_second == 1 and column_of_second == 2:
            not_exist = True
            return not_exist

        elif row_of_second == 2 and column_of_second == 2:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1]
            b = first[1][1] * second[1][2] + first[1][2] * second[2][2]
            result = [[0, 0, 0],
                      [0, a, b]]

            print("*" * 20)
            print(a, b)
            print("*" * 20)

        elif row_of_second == 2 and column_of_second == 3:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1]
            b = first[1][1] * second[1][2] + first[1][2] * second[2][2]
            c = first[1][1] * second[1][3] + first[1][2] * second[2][3]
            result = [[0, 0, 0, 0],
                      [0, a, b, c]]
            print("*" * 20)
            print(a, b, c)
            print("*" * 20)
        elif row_of_second == 3 and column_of_second == 2:
            not_exist = True
            return not_exist

    elif row_of_first == 2 and column_of_first == 1:  # first ones is completed 1x2
        # 2 le 1 olan bir ifadenin çarpımları
        if row_of_second == 1 and column_of_second == 2:
            a = first[1][1] * second[1][1]
            b = first[2][1] * second[1][2]
            result = [[0, 0, 0],
                      [0, a, b]]

            print("*" * 20)
            print(a, b)
            print("*" * 20)
            return result

    elif row_of_first == 2 and column_of_first == 2:  # first ones are completed 2x1--2x2--2x3
        # 2 le 2 olan bir ifadenin çarpımları
        if row_of_second == 2 and column_of_second == 1:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1]
            b = first[2][1] * second[1][1] + first[2][2] * second[2][1]
            result = [[0, 0],
                      [0, a],
                      [0, b]]

            print("*" * 20)
            print(a, "\n" + str(b))
            print("*" * 20)
            return result

        elif row_of_second == 2 and column_of_second == 2:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1]
            b = first[1][1] * second[1][2] + first[1][2] * second[2][2]
            c = first[2][1] * second[1][1] + first[2][2] * second[2][1]
            d = first[2][1] * second[1][2] + first[2][2] * second[2][2]
            result = [[0, 0, 0],
                      [0, a, b],
                      [0, c, d]]
            print("*" * 20)
            print(a, b, "\n" + str(c), d)
            print("*" * 20)
            return result

        elif row_of_second == 2 and column_of_second == 3:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1]
            b = first[1][1] * second[1][2] + first[1][2] * second[2][2]
            c = first[1][1] * second[1][3] + first[1][2] * second[2][3]
            d = first[2][1] * second[1][1] + first[2][2] * second[2][1]
            e = first[2][1] * second[1][2] + first[2][2] * second[2][2]
            f = first[2][1] * second[1][3] + first[2][2] * second[2][3]
            
            result = [[0, 0, 0, 0],
                      [0, a, b, c],
                      [0, d, e, f]]
            
            print("*" * 20)
            print(a, b, c, "\n" + str(d), e, f)
            print("*" * 20)
            return result
    
    elif row_of_first == 2 and column_of_first == 3:  # first ones are completed 3x1--3x2--3x3
        # 2 le 3 olan bir ifadenin çarpımları
        if row_of_second == 3 and column_of_second == 1:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1] + first[1][3] * second[3][1]
            b = first[2][1] * second[1][1] + first[2][2] * second[2][1] + first[2][3] * second[3][1]
            
            result = [[0, 0],
                      [0, a],
                      [0, b]]
            print("*" * 20)
            print(a, "\n", b)
            print("*" * 20)
            return result

        elif row_of_second == 3 and column_of_second == 2:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1] + first[1][3] * second[3][1]
            b = first[1][1] * second[1][2] + first[1][2] * second[2][2] + first[1][3] * second[3][2]
            c = first[2][1] * second[1][1] + first[2][2] * second[2][1] + first[2][3] * second[3][1]
            d = first[2][1] * second[1][2] + first[2][2] * second[2][2] + first[2][3] * second[3][2]
            result = [[0, 0, 0],
                      [0, a, b],
                      [0, c, d]]

            print("*" * 20)
            print(a, b, "\n" + str(c), d)
            print("*" * 20)
            return result

        elif row_of_second == 3 and column_of_second == 3:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1] + first[1][3] * second[3][1]
            b = first[1][1] * second[1][2] + first[1][2] * second[2][2] + first[1][3] * second[3][2]
            c = first[1][1] * second[1][3] + first[1][2] * second[2][3] + first[1][3] * second[3][3]
            d = first[2][1] * second[1][1] + first[2][2] * second[2][1] + first[2][3] * second[3][1]
            e = first[2][1] * second[1][2] + first[2][2] * second[2][2] + first[2][3] * second[3][2]
            f = first[2][1] * second[1][3] + first[2][2] * second[2][3] + first[2][3] * second[3][3]
            result = [[0, 0, 0, 0],
                      [0, a, b, c],
                      [0, d, e, f]]

            print("*" * 20)
            print(a, b, c, "\n" + str(d), e, f)
            print("*" * 20)
            return result

    elif row_of_first == 3 and column_of_first == 2:  # first ones are completed 2x1--2x2--2x3
        # 3 le 2 olan bir ifadenin çarpımları
        if row_of_second == 2 and column_of_second == 1:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1]
            b = first[2][1] * second[1][1] + first[2][2] * second[2][1]
            c = first[3][1] * second[1][1] + first[3][2] * second[2][1]
            result = [[0, 0],
                      [0, a],
                      [0, b],
                      [0, c]]

            print("*" * 20)
            print(a, "\n" + str(b) + "\n" + str(c))
            print("*" * 20)
            return result


        elif row_of_second == 2 and column_of_second == 2:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1]
            b = first[1][1] * second[1][2] + first[1][2] * second[2][2]
            c = first[2][1] * second[1][1] + first[2][2] * second[2][1]
            d = first[2][1] * second[1][2] + first[2][2] * second[2][2]
            e = first[3][1] * second[1][1] + first[3][2] * second[2][1]
            f = first[3][1] * second[1][2] + first[3][2] * second[2][2]
            result = [[0, 0, 0],
                      [0, a, b],
                      [0, c, d],
                      [0, e, f]]

            print("*" * 20)
            print(a, b, "\n", c, d, "\n", e, f)
            print("*" * 20)
            return result


        elif row_of_second == 2 and column_of_second == 3:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1]
            b = first[1][1] * second[1][2] + first[1][2] * second[2][2]
            c = first[1][1] * second[1][3] + first[1][2] * second[2][3]
            d = first[2][1] * second[1][1] + first[2][2] * second[2][1]
            e = first[2][1] * second[1][2] + first[2][2] * second[2][2]
            f = first[2][1] * second[1][3] + first[2][2] * second[2][3]
            g = first[3][1] * second[1][1] + first[3][2] * second[2][1]
            h = first[3][1] * second[1][2] + first[3][2] * second[2][2]
            j = first[3][1] * second[1][3] + first[3][2] * second[2][3]
            result = [[0, 0, 0],
                      [0, a, b, c],
                      [0, d, e, f],
                      [0, g, h, j]]

            print("*" * 20)
            print(a, b, c, "\n", d, e, f, "\n", g, h, j)
            print("*" * 20)
            return result

    elif row_of_first == 3 and column_of_first == 3:  # first ones are comleted 3x1--3x2--3x3
        # 3 le 3 olan bir ifadenin çarpımları
        if row_of_second == 3 and column_of_second == 2:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1] + first[1][3] * second[3][1]
            b = first[2][1] * second[1][1] + first[2][2] * second[2][1] + first[2][3] * second[3][1]
            c = first[3][1] * second[1][1] + first[3][2] * second[2][1] + first[3][3] * second[3][1]
            
            result = [[0, 0],
                      [0, a],
                      [0, b],
                      [0, c]]

            print("*" * 20)
            print(a, "\n" + str(b) + "\n" + str(c))
            print("*" * 20)
            return result
        
        elif row_of_second == 3 and column_of_second == 2:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1] + first[1][3] * second[3][1]
            b = first[1][1] * second[1][2] + first[1][2] * second[2][2] + first[1][3] * second[3][2]
            c = first[2][1] * second[1][1] + first[2][2] * second[2][1] + first[2][3] * second[3][1]
            d = first[2][1] * second[1][2] + first[2][2] * second[2][2] + first[2][3] * second[3][2]
            e = first[3][1] * second[1][1] + first[3][2] * second[2][1] + first[3][3] * second[3][1]
            f = first[3][1] * second[1][2] + first[3][2] * second[2][2] + first[3][3] * second[3][2]
            result = [[0, 0, 0],
                      [0, a, b],
                      [0, c, d],
                      [0, e, f]]

            print("*" * 20)
            print(a, b, "\n", c, d, "\n", e, f)
            print("*" * 20)
            return result

        elif row_of_second == 3 and column_of_second == 3:
            a = first[1][1] * second[1][1] + first[1][2] * second[2][1] + first[1][3] * second[3][1]
            b = first[1][1] * second[1][2] + first[1][2] * second[2][2] + first[1][3] * second[3][2]
            c = first[1][1] * second[1][3] + first[1][2] * second[2][3] + first[1][3] * second[3][3]
            d = first[2][1] * second[1][1] + first[2][2] * second[2][1] + first[2][3] * second[3][1]
            e = first[2][1] * second[1][2] + first[2][2] * second[2][2] + first[2][3] * second[3][2]
            f = first[2][1] * second[1][3] + first[2][2] * second[2][3] + first[2][3] * second[3][3]
            g = first[3][1] * second[1][1] + first[3][2] * second[2][1] + first[3][3] * second[3][1]
            h = first[3][1] * second[1][2] + first[3][2] * second[2][2] + first[3][3] * second[3][2]
            j = first[3][1] * second[1][3] + first[3][2] * second[2][3] + first[3][3] * second[3][3]

            result = [[0, 0, 0, 0],
                      [0, a, b, c],
                      [0, d, e, f],
                      [0, g, h, j]]
            print("*" * 20)
            print(a, b, str(c) + "\n" + str(d), e, str(f) + "\n" + str(g), h, j)
            print("*" * 20)
            return result
    else:
        return print("not exist")

""" 
def division(first,second):
row_of_first = len(first) - 1
row_of_second = len(second) - 1
column_of_first = len(first[0]) - 1
column_of_second = len(second[0]) - 1
"""


def addition(first, second):
    row_of_first = len(first) - 1
    row_of_second = len(second) - 1
    column_of_first = len(first[0]) - 1
    column_of_second = len(second[0]) - 1
    # example first[][] + second[][]
    if row_of_first == row_of_second and column_of_first == column_of_second:
        if row_of_first == 1 and column_of_first == 1:

            a = first[1][1] + second[1][1]

            result = [[0, 0],
                      [0, a]]
            
            print(str(a))
            return result

        elif row_of_first == 1 and column_of_first == 2:

            a = first[1][1] + second[1][1]
            b = first[1][2] + second[1][2]

            result = [[0, 0, 0],
                      [0, a, b]]

            print(str(a), str(b))
            return result
        elif row_of_first == 2 and column_of_first == 1:
            a = first[1][1] + second[1][1]
            b = first[2][1] + second[2][1]

            result = [[0, 0],
                      [0, a],
                      [0, b]]

            print(str(a) + "\n" + str(b))
            return result

        elif row_of_first == 2 and column_of_first == 2:
            a = first[1][1] + second[1][1]
            b = first[1][2] + second[1][2]
            c = first[2][1] + second[2][1]
            d = first[2][2] + second[2][2]

            result = [[0, 0, 0],
                      [0, a, b],
                      [0, c, d]]

            print(str(a), str(b) + "\n" + str(c), str(d))
            return result

        elif row_of_first == 3 and column_of_first == 2:
            a = first[1][1] + second[1][1]
            b = first[1][2] + second[1][2]
            c = first[2][1] + second[2][1]
            d = first[2][2] + second[2][2]
            e = first[3][1] + second[3][1]
            f = first[3][2] + second[3][2]

            result = [[0, 0, 0],
                      [0, a, b],
                      [0, c, d],
                      [0, e, f]]

            print(str(a), str(b) + "\n" + str(c), str(d) + "\n" + str(e), str(f))
            return result

        elif row_of_first == 2 and column_of_first == 3:
            a = first[1][1] + second[1][1]
            b = first[1][2] + second[1][2]
            c = first[1][3] + second[1][3]
            d = first[2][1] + second[2][1]
            e = first[2][2] + second[2][2]
            f = first[2][3] + second[2][3]

            result = [[0, 0, 0, 0],
                      [0, a, b, c],
                      [0, d, e, f]]

            print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f))
            return result

        elif row_of_first == 3 and column_of_first == 3:
            a = first[1][1] + second[1][1]
            b = first[1][2] + second[1][2]
            c = first[1][3] + second[1][3]
            d = first[2][1] + second[2][1]
            e = first[2][2] + second[2][2]
            f = first[2][3] + second[2][3]
            g = first[3][1] + second[3][1]
            h = first[3][2] + second[3][2]
            j = first[3][3] + second[3][3]

            result = [[0, 0, 0, 0],
                      [0, a, b, c],
                      [0, d, e, f],
                      [0, g, h, j]]

            print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))

            return result


def substraction(first, second):
    row_of_first = len(first) - 1
    row_of_second = len(second) - 1
    column_of_first = len(first[0]) - 1
    column_of_second = len(second[0]) - 1

    if row_of_first == row_of_second and column_of_first == column_of_second:
        if row_of_first == 1 and column_of_first == 1:

            a = first[1][1] - second[1][1]

            result = [[0, 0],
                      [0, a]]

            print(str(a))
            return result

        elif row_of_first == 1 and column_of_first == 2:

            a = first[1][1] - second[1][1]
            b = first[1][2] - second[1][2]

            result = [[0, 0, 0],
                      [0, a, b]]

            print(str(a), str(b))

            return result
        elif row_of_first == 2 and column_of_first == 1:
            a = first[1][1] - second[1][1]
            b = first[2][1] - second[2][1]

            result = [[0, 0],
                      [0, a],
                      [0, b]]

            print(str(a) + "\n" + str(b))

            return result

        elif row_of_first == 2 and column_of_first == 2:
            a = first[1][1] - second[1][1]
            b = first[1][2] - second[1][2]
            c = first[2][1] - second[2][1]
            d = first[2][2] - second[2][2]

            result = [[0, 0, 0],
                      [0, a, b],
                      [0, c, d]]

            print(str(a), str(b) + "\n" + str(c), str(d))
            return result

        elif row_of_first == 3 and column_of_first == 2:
            a = first[1][1] - second[1][1]
            b = first[1][2] - second[1][2]
            c = first[2][1] - second[2][1]
            d = first[2][2] - second[2][2]
            e = first[3][1] - second[3][1]
            f = first[3][2] - second[3][2]

            result = [[0, 0, 0],
                      [0, a, b],
                      [0, c, d],
                      [0, e, f]]

            print(str(a), str(b) + "\n" + str(c), str(d) + "\n" + str(e), str(f))
            return result

        elif row_of_first == 2 and column_of_first == 3:
            a = first[1][1] - second[1][1]
            b = first[1][2] - second[1][2]
            c = first[1][3] - second[1][3]
            d = first[2][1] - second[2][1]
            e = first[2][2] - second[2][2]
            f = first[2][3] - second[2][3]

            result = [[0, 0, 0, 0],
                      [0, a, b, c],
                      [0, d, e, f]]

            print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f))
            return result

        elif row_of_first == 3 and column_of_first == 3:
            a = first[1][1] - second[1][1]
            b = first[1][2] - second[1][2]
            c = first[1][3] - second[1][3]
            d = first[2][1] - second[2][1]
            e = first[2][2] - second[2][2]
            f = first[2][3] - second[2][3]
            g = first[3][1] - second[3][1]
            h = first[3][2] - second[3][2]
            j = first[3][3] - second[3][3]

            result = [[0, 0, 0, 0],
                      [0, a, b, c],
                      [0, d, e, f],
                      [0, g, h, j]]

            print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))
            return result
    else:
        return print("not exist")


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
        # print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))

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
        # a, b, c, d, e, f, g, h, j = cofactors(a, b, c, d, e, f, g, h, j, x=3, y=3)
        # a, b, c, d, e, f, g, h, j = transposed(a, b, c, d, e, f, g, h, j, x=3, y=3)


def adjugate(*args, x, y):
    if x == 3 and y == 3:
        determinant = found_determinant_of_matrix(*args, x=3, y=3)
        a, b, c, d, e, f, g, h, j = minors(*args, x=3, y=3)
        # print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))
        a, b, c, d, e, f, g, h, j = cofactors(a, b, c, d, e, f, g, h, j, x=3, y=3)
        # print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))
        a, b, c, d, e, f, g, h, j = transposed(a, b, c, d, e, f, g, h, j, x=3, y=3)
        # print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))
        a, b, c, d, e, f, g, h, j = a / determinant, b / determinant, c / determinant, d / determinant, e / determinant, f / determinant, g / determinant, h / determinant, j / determinant
        print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))


def cofactors(*args, x, y):
    if x == 3 and y == 3:
        a, b, c, d, e, f, g, h, j = args
        a, b, c, d, e, f, g, h, j = a, -b, c, -d, e, -f, g, -h, j
        # print(str(a), str(b), str(c) + "\n" + str(d), str(e), str(f) + "\n" + str(g), str(h), str(j))

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
two_to_one = [[None, None],
              [None, a],
              [None, b]]

one_to_two = [[0, 0, 0],
              [0, a, b]]

two_to_two = [[0, 0, 0],
              [0, a, b],
              [0, c, d]]

three_to_two = [[0, 0, 0],
                [0, a, b],
                [0, c, d],
                [0, e, f]]

two_to_three = [[0, 0, 0, 0],
                [0, a, b, c],
                [0, d, e, f]]

three_to_three = [[0, 0, 0, 0],
                  [0, a, b, c],
                  [0, d, e, f],
                  [0, g, h, j]]

transposed(a, b, c, d, x=2, y=2)
transposed(a, b, c, d, e, f, x=2, y=3)
transposed(a, b, c, d, e, f, x=3, y=2)  # this one is okey

# print("a,b,c\n" + "d,e,f\n" + "g,h,j\n")
# print("Choose your size of matrix\n")

"""x = int(input("size of row"))
y = int(input("size of column"))

if x == 2 and y == 2:  # 2  ye 2 olan matrixlerde yapılacak işlemeler için
    a = int(input("a değeri giriniz "))
    b = int(input("b değeri giriniz "))
    c = int(input("c değeri giriniz "))
    d = int(input("d değeri giriniz "))
    trace = found_of_trace(a, b, c, d)
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
    h = int(input("h değeri giriniz "))
    j = int(input("j değeri giriniz "))
    adjugate(a, b, c, d, e, f, g, h, j, x=3, y=3)
    found_determinant_of_matrix(a, b, c, d, e, f, g, h, j, x=3, y=3)"""

multiplication(one_to_two, two_to_one)
multiplication(three_to_three, three_to_three)
multiplication(two_to_two, two_to_two)

x = int(input("size of row"))
y = int(input("size of column"))
name = input("choose name of matrix")
if x == 1 and y == 2:
    a = int(input("a enter value "))
    b = int(input("b enter value "))
    name = one_to_two
if x == 2 and y == 1:
    a = int(input("a enter value "))
    b = int(input("b enter value "))
    name = two_to_one

if x == 2 and y == 2:  # 2  ye 2 olan matrixlerde yapılacak işlemeler için
    a = int(input("a enter value "))
    b = int(input("b enter value "))
    c = int(input("c enter value "))
    d = int(input("d enter value "))
    name = two_to_two
if x == 2 and y == 3:  # 2  ye 3 olan matrixlerde yapılacak işlemeler için
    a = int(input("a enter value "))
    b = int(input("b enter value "))
    c = int(input("c enter value "))
    d = int(input("d enter value "))
    e = int(input("e enter value "))
    f = int(input("f enter value "))
    name = two_to_three
if x == 3 and y == 2:  # 3  ye 2 olan matrixlerde yapılacak işlemeler için
    a = int(input("a enter value "))
    b = int(input("b enter value "))
    c = int(input("c enter value "))
    d = int(input("d enter value "))
    e = int(input("e enter value "))
    f = int(input("f enter value "))
    name = three_to_two
if x == 3 and y == 3:  # 3  ye 3 olan matrixlerde yapılacak işlemeler için
    a = int(input("a enter value "))
    b = int(input("b enter value "))
    c = int(input("c enter value "))
    d = int(input("d enter value "))
    e = int(input("e enter value "))
    f = int(input("f enter value "))
    g = int(input("g enter value "))
    h = int(input("h enter value "))
    j = int(input("j enter value "))
    name = three_to_three

# inverse_of_matrix(a, b, c, d)


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
