#this program will print powerset


def find_powerset(inp, out):
    if (inp == ''):
        print(out)
        return

    find_powerset(inp[1:], out)
    find_powerset(inp[1:], out + inp[0])



if __name__ == '__main__':
    inp = 'abc'
    find_powerset(inp, '');
