#function definition
def most_frequent(string):
    

    frequency = {}
    test= string
    for x in test:
        if x in frequency:
            frequency[x] +=1
        else:
            frequency [x] =1
     
     
    #sorting and reversing the dictionary values
    sort_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    for i in sort_freq:
            print(i[0] +" = "+ str(i[1]))


#main function
_in = input ("Please enter a string\n")
most_frequent(_in)
            
