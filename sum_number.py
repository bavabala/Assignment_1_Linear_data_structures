def Pairs(arr,number,sum):
    for i in range(0,number):
        for j in range(i+1,number):
            if (arr[i]+arr[j]==sum):
                print(arr[i],arr[j])
arr = [0,1,2,3,4,5,6,7,8,9]
number = len(arr)
sum =9
Pairs(arr,number,sum)


