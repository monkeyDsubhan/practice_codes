# num=list(map(int,input("enter the number:").split()))
# target=5
# def sum_number():
#     for i in num:
#         for j in num:
#             sum=num[i]+num[j]
#             if sum == target:
#                 print(sum[i])
# numbers=[1,2,3,4,5]
# target=5
# count=0
# for i in numbers:
#     for j in numbers:
#         sum=numbers[i]+numbers[j]
        
#         if sum==target:
#             count+=1
#             print(count)
#         else:
#             j+=1
# numbers=[8,4,6,7,2,3]
# def bubble_sort(numbers):
#     for i in range(len(numbers)-1):
#         for j in range(len(numbers)-1):
#             if numbers[j]>numbers[j+1]:
#                 temp=numbers[j]
#                 numbers[j]=numbers[j+1]
#                 numbers[j+1]=temp
#     return numbers
# x=bubble_sort(numbers)
# print(x)
numbers=[8,4,6,7,2,3,5,1,0]
target=9
def sum_numbers(numbers):
    for index, value in enumerate(numbers):
        for index2, value in enumerate(numbers):
            sum=numbers[index]+numbers[index2]
            if sum==target:
                print(f"Index of {value}: {index}")
            index2+=1

    return numbers
sum_numbers(numbers)
    
    







