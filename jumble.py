import random
def jumble(w):
    w.split()
    print(w)
    word=random.shuffle(w)
    print(word)
    # k=''
    # #k.join(word)
    # word=k
    import random
 
# initializing list
test_list = ['a','b','c','d']
 
# Printing original list
print ("The original list is : " + str(test_list))
 
# using random.shuffle()
# to shuffle a list
random.shuffle(test_list)
 
# Printing shuffled list
print ("The shuffled list is : " +  str(test_list))
k=""
k=k.join(test_list)
print(k)
print(jumble('swfwfgw'))