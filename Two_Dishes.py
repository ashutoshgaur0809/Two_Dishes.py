T = int(input("enter no. of test caes = "))
for i in range(T):
  N = int(input("Enter no. of Guests = "))
  F = int(input("Enter no. of Fruits = "))
  V = int(input("Enter no. of Veg = "))
  Fi = int(input("Enter no. of Fishes = "))
  temp = F + Fi
  if(V >= N or temp >= N):
    print("Yes")
  else:
    print("No")  
  