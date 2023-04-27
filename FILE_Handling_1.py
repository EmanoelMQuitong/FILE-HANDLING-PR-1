#P-1( 25 points). Write a Python program that reads a text file named numbers.txt that contains 20 integers. The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

#List the contents of numbers.txt
with open('numbers.txt', 'r') as f:
    for line in f:              #List all the contents of numbers.txt
        mod_num = int(line)%2   #Determine if the number is even or odd
        if mod_num == 0:        #Check if the boolean is working
            with open('even.txt', 'a') as wf:   #Append the contents of line to even.txt if it is even
                wf.write(line)      

