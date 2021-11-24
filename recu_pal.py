#Recirsive Method to find the length of the longest palindromic sub-string

# Function to calculate max of two integers
def max(x, y):
    if (x > y):
        return x
    else:
        return y


# Function to find the length of the  largest possible sub-tring
def len_long_sub_string(strn, i, j):
    
    # If there is only 1 character
    if (i==j):
        return 1
  

    # If there is only 2 characters and both are same
    if (strn[i]==strn[j] and i+1==j):
        return 2
 

    # If the first and last characters are same
    # Remove those charcters and new string go through function again
    # 2 is aaded to the lenth each time
    if (strn[i]==strn[j]):
      return len_long_sub_string(strn, i+1, j-1) + 2

    # If the first and last characters do not match
    #new strings taken one withot first charector and other without last charector
    # Both will go through the function and maximum will be returned
    return max(len_long_sub_string(strn,i,j-1),len_long_sub_string(strn,i+1,j))


string = input("Enter the string: ")
n = len(string)
print("The length of Largest pallindrome subsequence is ",len_long_sub_string(string,0,n-1))

