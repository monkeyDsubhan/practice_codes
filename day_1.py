# s=[1,2,3,4]
# s1=[4,5,6]
# i=0
# j=0
# for i in range(5):
#     while i <len(s):
#         print(s)
#         break
#     for j in range(3):
#         while j<len(s):
#             print(s1)
#             break
#     print()
# machine=16
# shirt=2
# pant=4
# i=0
# x=shirt+pant
# while x==machine:
#     print(x)
#     break
# # print(x)
# def max_clothes_in_washer():
#     """Calculates the maximum number of shirts and pants that fit in a washer.

#     Returns:
#         tuple: A tuple containing the maximum number of shirts and pants.
#     """
#     washer_capacity = 16  # Total washer capacity in kg
#     shirt_weight = 2      # Weight of one shirt in kg
#     pant_weight = 4       # Weight of one pant in kg

#     remaining_capacity = washer_capacity - shirt_weight - pant_weight 
#     max_shirts = remaining_capacity // shirt_weight
#     max_pants = remaining_capacity // pant_weight

#     return max_shirts, max_pants


# if __name__ == "__main__":
#     max_shirts, max_pants = max_clothes_in_washer()

#     print(f"Maximum shirts that can fit: {max_shirts}")
#     print(f"Maximum pants that can fit: {max_pants}")
#     print("Note: This assumes at least one shirt and one pant are already in the washer.")


        
# def max_clothes_in_washer_nested_loops():
#     washer_capacity = 16
#     shirt_weight = 2
#     pant_weight = 4

#     max_shirts = 0
#     max_pants = 0

#     # Outer loop: Iterates through possible number of shirts
#     for num_shirts in range(1, washer_capacity // shirt_weight + 1):
        
#         # Inner loop: Iterates through possible number of pants
#         for num_pants in range(1, washer_capacity // pant_weight + 1):

#             total_weight = num_shirts * shirt_weight + num_pants * pant_weight

#             if total_weight <= washer_capacity and num_shirts > max_shirts and num_pants > max_pants:
#                 max_shirts = num_shirts
#                 max_pants = num_pants

#     return max_shirts, max_pants


# if __name__ == "__main__":
#     max_shirts, max_pants = max_clothes_in_washer_nested_loops()

#     print(f"Maximum shirts that can fit: {max_shirts}")
#     print(f"Maximum pants that can fit: {max_pants}")
# s=['hi','this is ',]
# s1=['1','2','3','4'].join(s)
# print(s1)
# def number(num):
#     count=0
#     while num!=0:
#         num //=10
#         count+=1
#     return count
# x=number(500)
# print(x)

# def number(num):
#     count=0
#     while num !=0:
#         num//=10
#         count+=1
#     return count
# x=number(500)
# print("The number:",x)

# s=int(input("Enter the number:"))
# def main():
    
#     while s !=0:
#         match s:
#             case 1:
#                 print("Mon")
#             case 2:
#              print("tues")
#             case 3:
#              print("wednes")
#             case 4:
#              print("Thurs")
#             case 5:
#                 print("fri")
#             case 6:
#                 print("satur")
#             case 7:
#                 print('sunday')
#             case other:
#                 print("Invalid")
#         break
# main()
#number[0,2,3,4], target=7, for interger1 in number + number2=for integer2 in number
# num=list(map(int,input("Numbers:").split()))
# target=int(input("Enter the target:"))
# count=0
# def sum_of_numbers():
#     for i in num:
#         for j in num:
#             sum=[i]+[j]
#         if sum == target:
#             return num[i],num[j]
#         else:
#             j+=1
#         i+=1
# x=sum_of_numbers()
# print(x)
# class Solution(object):
#     def twoSum(nums, target):
#         for i in range(0,len(nums)):
#             for j in range(1,len(nums)):
#                 sum=nums[i]+nums[j]
#                 if sum==target:
#                      return(i,j)
#                 j+=1
#             i+=1
# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
    
# num_terms=int(input("enter the no of terms:"))
# for i in range(num_terms):
#     print(f"fibonacci({i})={fibonacci(i)}")
        
    



    
# class Solution(object):
#    def twoSum(nums, target):
#         for i in range(1,len(nums)):
#             for j in range(0,len(nums)):
#                 sum=nums[i]+nums[j]
#                 if sum==target:
#                      print(i,j)
#                 j+=1
#             i+=1
#     twoSum() 
#     nums=list(input().split())
#     target=int(input("Enter the target:"))



# class person:
#     def __init__(self,name):#
#         self.name=name      # CONSTRUCTOR
#     def say_hi(self):       #
#         print('hello,my name is',self.name)# METHOD
#     def say_bye(self):
#         print("bye ",self.name)
# p=person("subhan")#object
# p.say_hi()#ACCESSING METHOD USING OBJECT
# p.say_bye()
# the thing required to create an object
# a.constructor
# class
# build in function
# user defined
#  inheritence
# polymorphism
# data encapsulation
# data abstraction

# class test:
#     def __init__(self):
#         self.x=0
# class derived_test(test):
#     def __init__(self):
#         self.y=1
#         test.__init__(self)
# def main():
#     b=derived_test()
#     print(b.x,b.y)
# main()

# class parent:
#     def func1(self):
#         print("Function 1")
# class child(parent):
#     def func2(self):
#         return super().func1()
#     print("Functin 2")
# ob=child()
# ob.func2()
# class parent:
#     def func1(self):
#         print('hi')
# class child(parent):
#     def func2(self):
#         super().func1()
#         print("bye")
# ob1=child()
# ob1.func2()
# class Animal: 
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print("Animal sound")
# class lion(Animal):  
#     def speak(self):
#         super().speak() 
#         print("roar!")
# my_dog = lion("Buddy")
# my_dog.speak() 
# class Animals:
#     def init(self,name,species,sound):
#         self.name=name
#         self.species=species
#         self.sound=sound
#     def make_sound(self):
#         print(f"The '{self.species}' named '{self.name}' sounds '{self.sound} '")
# class Lion(Animals):
#     def _init_(self,name):
#         super()._init_(name, "Lion","roar")
#     def get_info(self):
#         print("lions are the kings of the jungle")
# class Elephant(Animals):
#     def _init_(self,name):
#         super()._init_(name, "Elephant","Trumpet")
#     def get_info(self):
#         print("Elephants are the largest land animals")
# class Snake(Animals):
#     def _init_(self,name):
#         super()._init_(name, "Snake","Hiss")
#     def get_info(self):
#         print("Snakes can be found on every continent except antartica")

# leo=Lion()
# ellie=Elephant()
# slyther=Snake()

# leo.make_sound()
# leo.get_info()
# print()

# ellie.make_sound()
# ellie.get_info()
# print()

# slyther.make_sound()
# slyther.get_info()
# print()
# first='Hi'
# last='iam doing great'
# print(f'{first} {last}'.upper())    
# print('f{first}{last}')
# l1=[1,5,6]
# l2=[7,5,6]
# for i in range(len(l1)-1,-1,-1):
#         (sum(l1))

# class lateral:
#         def __init__(self,name,age):
#                 self.name=name
#                 self.age=age
        
#         def details(self):
#                 print(f"hi iam {self.name} my age is {self.age}")
#         def speak(self,lang):
#                 print(f"hi iam {self.name} my age is {self.age}i can speak {lang}")


# ob=lateral('subhan',18)
# ob.details()
# ob.speak("urdu")

# class Animal:
#     def __init__(self,name,food,sleep):
#         self.name=name
#         self.food=food
#         self.sleep=sleep
#     def roar(self):
#         print(f"His name is {self.name} and his food is {self.food} it wil sleep {self.sleep}") 
# tiger=Animal('tiger','meat',5)
# tiger.roar()

# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def discription(self):
#         print(f'this is {self.name} and he/she: {self.age}')
# class Dog(Animal):
#     def __init__(self, name, age,breed):
#         super().__init__(name, age)
#         self.breed=breed
#     def discription(self):
# #         print(f'this guy {self.name} is cute and he is {self.age}old. his breed is {self.breed}')
# # class bird(Animal):
# #     def __init__(self,name,age,character):
# #         super().__init__(name,age)
# #         self.character=character
# #     def colour(self):
# #         print(f'this bird name name is {self.name}its age {self.age}its colour{self.character}')

# # bard=Animal("rosy",15,'green colour')
# # bard.colour()

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def description(self):  # Fixed typo in method name
#         print(f"This is {self.name} and he/she is {self.age} years old.")

# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed

#     def description(self):
#         print(f"This guy {self.name} is cute and he is {self.age} years old. His breed is {self.breed}.")

# class Bird(Animal):  # Inheriting directly from Animal
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color  # Renamed to 'color'

#     def colour(self):
#         print(f"This bird's name is {self.name}, its age is {self.age}, and its color is {self.color}.")
# class insect(Animal):
#     def __init__(self, name, age,legs):
#         super().__init__(name, age)
#         self.legs=legs
#     def walk(self):
#         print(f'the insect name {self.name}, its age {self.age} how many legs does have it {self.legs} legs')
# class test:
#     def __init__(self,) -> None:
        
# # # Create a bird object
# # bard = Bird("Rosy", 15, "green")  # Pass color as 'green'
# # bard.colour()  # Call the colour method on the bird object
# answer=insect("beetle",1,"6")
# answer.walk()
# bard=Bird("rosy",2,"green")
# bard.colour()

# arr=input("Enter the list numbers separated by spaces:").split()
# arr=[int(x) for x in arr ]
# target=int(input("Enter the target value to search:"))
# found=False
# for i in range(len(arr)):
#     if arr[i]==target:
#         print(f'Target number {target} and its found at {i} index')
#         found=True
#         break
# if not found:
# #     print("The number {target} is not found")
# arr=[int(x) for x in input("Enter the sorted list of numbers separated by spaces:").split()]
# target=int(input('Enter the target value to search:'))
# start,end=0,len(arr)-1
# found=False
# while start<=end:
#     mid =(start+end)//2
#     if arr[mid]==target:
#         print(f"target {target} found at index {mid}.")
#         found=True
#         break
#     elif arr[mid]<target:
#         start =mid+1
#     else:
#         end=mid-1
# if not found :
#     print(f'Target {target} not fond in the array.')


# lst1=int(input())
# lst2=int(input())
# for i in lst1(-1,-1,-1):
#     x=tuple(lst1)

# for j in lst2(-1,-1,-1):
#     v=tuple(lst2)
# sum=x+v
# r=sum.reversed()
# b=list(r)


# def first_occr(arr,n,key):
#     s,e=0,n-1
#     ans=-1
#     while s<=0:
#         mid=s +(e-s)//2
#         if arr[mid]==key:
#             ans=mid
#             e=mid-1
#         elif key >arr[mid]:
#             s=mid+1
#         else:
#             e=mid-1
#     return ans

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        

# numbers = [10, -5, 25, -8, 30]

# for i, num in enumerate(numbers):
#     if num < 0:
#         numbers[i] = 0

# print(numbers)  # Output: [10, 0, 25, 0, 30]

# def authenticate():
#     password="subhan123"
#     attempt=3
#     while attempt>0:
#         user_input=input("Enter the password:")
#         if user_input==password:
#             print('Welcome')
#             break
#         else:
#             attempt-=1
#             if attempt>0:
#                 print(f"Wrong password ! You have {attempt} attemps left.")
#             else:
#                 print("Account blocked.")
#                 break
# authenticate()
# class Verification():
#     def __init__(self,user_input,password):
#         self.user_input=user_input
#         self.password=password
#     def authentication(self):
#         password="subhan123"
#         attempt=3
#         while attempt>0:
#              user_input=input("Enter the password:")
#              if user_input==password:
#                 print('Welcome')
#                 break
#              else:
#                 attempt-=1
#                 if attempt>0:
#                     print(f"Wrong password ! You have {attempt} attemps left.")
#                 else:
#                     print("Account blocked.")
#                     break
# ob=Verification(password="venkat",attempts=3)
# ob.authentication()
# class authentication():
#     def _init_(self,password,attempts):
#         self.password=password
#         self.attempts=attempts

#     def user_input(self):
#         while self.attempts>0:
#             user_input=input("Enter the password:")

#             if user_input==self.password:
#                 print("welcome!")
#                 break
#             else:
#                 self.attempts-=1
#                 if self.attempts>0:
#                     print(f"wrong password! you have {self.attempts} attempts left.")
#                 else:
#                     print("Account Blocked.")
#                     break

# authenticator=authentication(password="venkat",attempts=3)
# authenticator.user_input()
# arr1=[6,7,8,9,10]
# x=0
# y=[]
# for i in range(len(arr1)):
#     x=arr1[i]
#     print(*arr1)    
# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
# my_list=[64,34,25,12,22,11,90]
# print("Original List:",my_list)
# bubble_sort(my_list)
# print("Sorted List:",my_list)

# for i in range(len(arr1)):
#     x=arr1[i]
#     print(*arr1) 
# def get_x_values(arr):
#     x_values = []
#     for i in range(len(arr)):
#         x_values.append(arr[i])  

#     return x_values

# arr1 = [6, 7, 8, 9, 10]
# # result = get_x_values(arr1)
# def selection_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         minimum_numuber=i
#         for j in range(i+1,n):
#             if arr[j]<arr[minimum_numuber]:
#                 minimum_numuber=j 
#         arr[i],arr[minimum_numuber]=arr[minimum_numuber],arr[i]
#          #arr[i]=arr[minimum_numuber]
#          #arr[minimum_number]=arr[i]
        
# my_list=[64,34,25,12,22,11,90]
# print("Original List:",my_list)
# selection_sort(my_list)
# # print("Sorted List:",my_list)

# # 
# # def sum(arr):
# #     return arr*(arr+1)//2
# # arr=123456
# # x=sum(arr)
# # print(x)
# def merge_sort(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
#         left_half=arr[:mid]
#         right_half=arr[mid:]
#         merge_sort(left_half)
#         merge_sort(right_half)
#         merge(arr,left_half)
# def merge(arr,left,right):
#     i=j=k=0
#     while i<len(left) and j< len(right):
#         if left[i]< right[j]:
#             arr[k]=left[i]
#             i+=1
#         else:
#             arr[k]=right[j]
#             j+=1
#         k+=1
#     while i<len(left):
#         arr[k]=right[i]
#         i+=1
# #         k+=1
# #     while j <len(right):
# #         arr[k]=right[j]
# #         j+=1
# #         k+=1
# # my_list=[64,34,25,12,22,11,90]
# # print("original list",my_list)
# # merge_sort(my_list)
# # print('sorted:',my_list)

# # time complexity = O(N log N)
# def merge_sort(arr):
#     if len(arr) > 1:
#         # Divide the array into two halves
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         # Recursive call on each half
#         merge_sort(left_half)
#         merge_sort(right_half)

#         # Merge the sorted halves
#         merge(arr, left_half, right_half)


# def merge(arr, left, right):
#     i = j = k = 0

#     # Compare and merge the elements from left and right halves
#     while i < len(left) > j < len(right):
#         if left[i] < right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1

#         # If there are any remaining elements in left or right halves, add them to the merged array
#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1


# my_list = [64, 34, 25, 12, 22, 11, 90]
# print("Original list:", my_list)
# merge_sort(my_list)
# print("Sorted List:", my_list)



