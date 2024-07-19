def induct(elements,val):
    inserted = False
    for i,v in enumerate(elements):
        if v < val:
            inserted = True
            elements.insert(i,val)
            break;
    if not inserted:
        elements.append(val)

def sort(elements):
    if(len(elements)==1):
        return

    val = elements.pop()
    sort(elements)

    induct(elements,val)


if __name__ == '__main__':
    elements = [3,1,0,2]
    value = elements[0]
    sort(elements)
    print(elements)
