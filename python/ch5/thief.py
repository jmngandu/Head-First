balance = 10500  #balance is a global variable.
camera_on = True
def steal(balance, amount): #..but it’s shadowed by this parameter.
    global camera_on
    camera_on = False
    if (amount < balance):
        balance = balance - amount #So when you change the balance in the function steal,
                                   #you’re not changing the actual bank balance!
    return amount      #We’re returning the amount stolen...
    camera_on = True 
proceeds = steal(balance, 1250)
print('Criminal: you stole', proceeds)   


#And, in addition to not actually stealing any money, the criminal forgets to turn the camera back on,
#which is a dead giveaway to the police that something nefarious is going on. Remember, when you return
#from a function, the function stops executing, so any lines of code after the return are ignored!