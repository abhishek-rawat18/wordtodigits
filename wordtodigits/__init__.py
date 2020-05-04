def convert(text): #Function in which the string (sentence) should be passed as argument

    #The part of code below ensures that even those words are accounted for that 
    #have a terminator (fullstop, exclaimation mark, question mark) at the end
    #for example "one thousand?" should convert to "1000?"
    text=text.replace("."," . ") #Ensure full stop has a space before it
    text=text.replace("?"," ? ") #Ensure question mark has a space before it
    text=text.replace("!"," ! ") #Ensure exclamation mark has a space before it

    tokens=text.split() 
    
    #Will just need to store the numbers 0-19 and {20,30,...,90} and 
    #{100,1000,1000000} in a dictionary of word and the corresponding number
    starting_nos=["zero","one","two","three","four","five","six","seven","eight","nine","ten",
                  "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    higher_nos=["hundred","thousand","million"]

    starting_nos_dict=dict()
    #Creating a dictionary of the word and the corresponding number
    for i in range(len(starting_nos)):
        starting_nos_dict[starting_nos[i]]=i

    #Creating a dictionary of the word and the corresponding number
    tens_dict=dict()
    for i in range(len(tens)):
        tens_dict[tens[i]]=(i+2)*10 #since starting from twenty    

    higher_nos_dict={"hundred":100, "thousand":1000, "million":1000000}

    '''Basic idea of how my algorithm works:
            For the digits before the decimal point (if any):
                  We just ensure that all words in 1 to 20 and {20,30,...90} are 
                  summed up till we come across any from hundred,thousand or million,
                  where we end up multiplying the obtained number.
                  Now we just ensure that multiplication with hundred or addition for
                  the digits less than hundred is stored separately (say as a temporary number),
                  till we encounter thousand/million - thats when we add the obtained temporary number
                  to the final number (which initially is taken as 0). 
                  If we reach the end and dont come across any thousand/million, 
                  we add the temporary number to the final number anyway.
            For the digits after the decimal point (if any):
                  We just append the digits in string form to the final sentence
    '''

    temp_number=0 #The temporary number
    final_number=0 #The final number

    point_flag=False #to tell us if we came across a decimal point

    number_flag=False #stating that the number has begun or not 
    #(It will turn to false also if the number before decimal part is over)

    final_string="" #The final string we require in the converted form

    tokens.append("") #To take care of the problem: if a number occurs as the last word 
                      #Not required if we are sure that every sentence does end with a fullstop

    for i in range(len(tokens)): #Going through the separate words one by one

        word=tokens[i]

        if (word.lower() in starting_nos or word.lower() in tens or word.lower() in higher_nos_dict) and point_flag==False: 
        
        #extracting the words which specify numbers 
            
            number_flag=True #saying that the number has begun

            if word.lower() in starting_nos:
                temp_number=temp_number+starting_nos_dict[word.lower()]
            elif word.lower() in tens:
                temp_number=temp_number+tens_dict[word.lower()]

            elif word.lower()=="hundred":
                temp_number=temp_number*100

            elif word.lower() in ["thousand","million"]:
                final_number=final_number+temp_number*higher_nos_dict[word.lower()] #this is a multiplicative scaling
                temp_number=0  
                
        elif word.lower() in starting_nos and point_flag==True: #i.e. when decimal digits

            final_string+=str(starting_nos_dict[word.lower()]) #keep on adding the digits as they are

        elif (word=="and" and (tokens[i+1] in starting_nos or tokens[i+1] in tens or tokens[i+1] in higher_nos )):
           #Peek at the next word and if that is also a number that means the "and" occurs in b/w numbers
           #Skip to the next word
            continue

        elif (word.lower()=="point" and (tokens[i+1] in starting_nos or tokens[i+1] in tens or tokens[i+1] in higher_nos)):
            #If you come across the word "point" then peek at the next word. If its a number that means we have to convert
            #"point" to "." 
            #This peeking will just ensure that if we come across something like "point six.", it would give "0.6" rather than "point 6"
            #and if we come across "This is for one point" it will give "This is for 1 point"

            final_number=final_number+temp_number 
            #If you come across a decimal point, it means that scaling would no longer be required. So just add temp_number to final_number
            #Also +temp_number will be non zero iff its not already used as a scaling factor

            point_flag=True #Stating that you came across a deminal point
            number_flag=False #stating that the number before the decimal part is over
            final_string+=" "+str(final_number)+"."
            continue
        
        else: #i.e. the number has ended 

            point_flag=False

            if number_flag==True: #i.e. if the number began

                final_number=final_number+temp_number 

                if word!="." and word!="?" and word!="!": #else leave no space in between
                    final_string+=" "+str(final_number)+" "+word
                else:
                    final_string+=" "+str(final_number)+word
                number_flag=False
            else:
                if word!="." and word!="?" and word!="!": 
                    #else leave no space in between the termination characters
                    final_string+=" "+word
                else: 
                    final_string+=word
            final_number=0
            temp_number=0

    final_string=final_string[1:] #Remove the initial space
    print(final_string)
            