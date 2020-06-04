n = [None] * 1000

# O(1) - space doesn't increase as it's input is one


def simple_function(n):
    return n


simple_function(n)
########################

# O(n) =  space increases as the input increases


def make_another_array(n):
    inner_array = []

    for i in n:
        inner_array.append(i)

    return inner_array


make_another_array(n)

#########################

# O(n^2) space complexity - doubling the input
def make_matrix(n):
    matrix = []

    for item in n:
        row = []
        for i in n:
            row.append(i * 2)

        matrix.append(row)

make_matrix(n)