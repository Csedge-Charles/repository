##Input sentence and recieve both the longest word and the shortest word


def string(lists):
    word = ''
    for i in range(len(lists)):
        word += lists[i]
    return word

#turns lists into string

sentence = input('Write a sentence: ')
word = [] #Seperates sentence into words
word_list = [] #All words in the sentence goes into this list


for i in range(len(sentence)):
    #Forms words in sentence and redirects it to word
    word.append(sentence[i])
    if sentence[i] == ' ':
        #Ends word when space is detected
        word.remove(' ')
        word_list.append(string(word))
        #word is deposited into word_list and word is resetted
        word = []

word_list.append(string(word))

len_list = [] #List that express the length of each word in word_list
sorted_list = [] #Duplicate list that is in order

for i in word_list:
    #Finds the length of each word
    len_list.append(len(i))
    sorted_list.append(len(i))

sorted_list.sort()
#Sorted list is sorted in order from least to greatest

for i in range(len(len_list)):
    #Checking where the greatest number is located on len_list that corresponds it to greatest number on sorted list or sorted_list[-1]
    if len_list[i] == sorted_list[-1]:
        #Once i or location is found loop stops
        break

for t in range(len(len_list)):
    #T is checking where the least number is located on len_list that corresponds it to least number on sorted list or sorted_list[0]
    if len_list[t] == sorted_list[0]:
        break
#i corresponds with both len_list and word_list so the longest word is found in both locations

print('')
print(f'The longest word is: {word_list[i]}, and the shortest word is: {word_list[t]}')
