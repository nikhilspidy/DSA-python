#this program will reverse list without creating new list

def reverse(listData):
    if(len(listData)==1):
        return;

    value = listData.pop()
    reverse(listData)

    listData.insert(0,value)



if __name__ == "__main__":
    listData = [4,3,2,1,0]


    reverse(listData)
    print(listData)
