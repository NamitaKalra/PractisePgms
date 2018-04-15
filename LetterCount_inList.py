def count_letters(word_list):
    """ See question description """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0
        
    for item in word_list:
        for letter in item:
            letter_count[letter]+=1
     
    max_value=0
    list1=[]

    for key,value in letter_count.items():
        if value>max_value:
            max_value=value
        
        
    for key,value in letter_count.items():
        if value==max_value:
            list1.append(key)
        
    list2= sorted(list1)
    return list2[0]

monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

monty_words = monty_quote.split(" ")
    
print(count_letters(monty_words))
    
        
    # enter code here