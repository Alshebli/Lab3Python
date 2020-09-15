# Author: Saeed Alshebli saa6016@psu.edu
# Collaborator: Aidan OConnor avo5337@psu.edu
# Collaborator: Lindsey Rich lxr5326@psu.edu
# Collaborator: Siddhant Rajoriya sbr5632@psu.edu
# Section: 2
# Breakout: 11
def sum_n(n):
  if n<=0:
    return 0
  else:
    return n+sum_n(n-1)
def print_n(s, n):
  if n!=0:
    print(f"{s}")
    print_n(s,n-1)
    
def run():
  n=int(input("Enter an int: "))
  N=sum_n(n)
  print(f"sum is {N}.")
  s=str(input("Enter a string: "))
  print_n(s,N)

if __name__== '__main__':
  run ()