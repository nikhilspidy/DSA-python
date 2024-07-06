

def search(number,elements):
    if len(elements)==0:
        return False

    mid_index = len(elements)-1
    mid_index = mid_index //2
    mid_index_number = elements[mid_index]
    if number == mid_index_number:
        return True;

    if number > mid_index_number:
        return search(number,elements[mid_index+1:])

    elif number <=mid_index_number:
        return search(number,elements[:mid_index])


    return False;



if __name__ == '__main__':
    elements = [3,4,2,1,5,8,6,10]
    elements.sort()
    number = int(input("enter number : "))
    print(search(number,elements))