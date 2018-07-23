# Write a function that removes the dollar sign (“$”) in a string, named remove_dollar_sign, 
# takes 1 arguments: s, where s is the input string, returns the new string with no dollar sign in it

def remove_dollar_sign(s):
    newstr = s.replace("$", "")
    return(newstr)


print(remove_dollar_sign("$80% percent of $life is to show $up"))
