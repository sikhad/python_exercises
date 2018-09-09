def anagram(s):

    aList = s.split() # split sentence into words
    aList = set(aList) # remove duplicate words 
    aDict = {} # create a dictionary to store the words/anagrams

    for word in aList:
        key = tuple(sorted(word, key=str.lower)) # store keys as letters of a word
        if key in aDict: # if the letters already exist, add the word associated with the key
            aDict[key].append(word)
        else: # otherwise, define a new key of letters
            aDict[key] = [word]

    item = ""
    
    for key in aDict: # to print the distinct anagrams 
        if len(aDict[key]) > 1:
            for x in aDict[key]:
                item = item + x + " "
            print(item)
            item = ""
            
