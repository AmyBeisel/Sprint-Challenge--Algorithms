'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #need a base case for recursion
    #if the word is an empty string, return 0
    if len(word)==0:
        return 0
    #if the word only has 1 letter
    if len(word) < 2:
        return 0
    
    #ok, now we need to recuse back to base case
    #check if the substring matches
    if word[:2] == 'th':
        return  1 + count_th(word[2:]) 

    #otherwise, if the first two letters are not 'th', then we need
    #to just move over once, count from the remaining index and repeat
    else:
        return count_th(word[1:])

#check 
print(count_th('abcthxyz'))
    

