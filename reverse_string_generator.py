def reverse_gen(string):
    for i in range(len(string)-1,-1,-1):
        yield string[i]


for i in reverse_gen('Keerthana'):
    print(i)
