# ODD and EVEN numbers separator.
<b>
Write a Python program that reads a text file named numbers.txt that contains 20 integers. The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.
</b>

# Program Sequence
+ Open file source
+ List the contents
+ Determine if the number is even or odd
+ Transfer contents of line to even.txt if the number is Even.
+ Transfer contents of line to odd.txt if the number is odd.

# Guide
+ Open the file source
  ```
  with open('numbers.txt', 'r') as f:
  ```
+ List the contents of numbers.txt

  ```
  with open('numbers.txt', 'r') as f:
    for line in f:              #List all the contents of numbers.txt
    
  ```
+ Determine if the number is even or odd
  ```
  mod_num = int(line)%2         #Determine if the number is even or odd
        if mod_num == 0:        #Check if the boolean is working
  ```
  
+ Transfer contents of line to even.txt if the number is Even.
  ```
  if mod_num == 0:                          #If the mod_num is 1, the content odd. If the mod_num is 0, the content is even.
  with open('even.txt', 'a') as wf:         #Appends the contents of line to even.txt if it is even number.
                wf.write(line)
  ```
+ Transfer contents of line to odd.txt if the number is odd.
  ```
  else:
    with open('odd.txt', 'a') as wf:         #Appends the contents of line to odd.txt if it is odd number.
                wf.write(line)
  ```
