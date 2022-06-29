#####################################################################################################
# This program will read from a file of english words, determine the pattern of characters of each  #
# word, and save the patterns to a new file. We will then accept input from a user for the pattern  #
# they would like to search and return a list of english words that match that pattern.             #
#####################################################################################################


# define a function to convert words to a pattern
def wrd_ptrn(x):
    count = 97  # count set at 97 which is ASCII for 'a'
    i = 0  # use to walk through the mapping{} dict and reset to 0 for each new word
    pattern = ''  # create a string called 'pattern'
    mapping = {}  # create a dictionary to map the unique characters (important for matching
                  # repeated characters with their respective pattern character)

    for char in x:  # for loop to walk through each word and compare individual characters
        if char not in mapping.values() and char != '\n':  # looking for unique letters (not mapped)
                                                           # and also dont include '\n' character
            mapping[i] = char  # adding unique character to dictionary
            pattern += chr(count)  # pattern string will convert 'count' to its ASCII character
            count += 1  # pattern will start at 'a' and increment by 1
                        # (reason for count being equal to ASCII 'a' (97))
            i += 1  # incrementing i for use in mapping dict

        elif char != '\n':  # character is not unique and not '\n'
            for key, val in mapping.items():  # for loop to find key:value pairs in the dict
                if val == char:  # find the location of current character so we can get the key for next step)
                    temp = key + 97  # this will keep the pattern character consistent if it
                    # shows up again later in the word. think aardvark pattern
                    # is aabcdabe because 'a' = 'a' and 'r' = 'b'
                    pattern += chr(temp)  # attach the temp value from above to the pattern string

    pattern += '\n'  # add a new line after each pattern is completed.
    return pattern  # return the pattern

# define a function to find words that match the pattern
def ptrn_wrd(pattern_list, user_input):
    k = 0  # use counter 'k' to match english words to patterns (since the location of a word and its
           # pattern would be the same for both lists)
    for x in pattern_list: # search through the list of patterns
        if user_input == x and len(user_input) == len(pattern_list[k]): # select a pattern in the list equal to user input and check that lengths are equal
            match = eng_list[k] # if there is a match, save it to the created list match[]
            print(match) # display the english word(s) that match(es) the pattern(s)
        elif user_input not in pattern_list: # error message if the pattern given isn't in the list
            print("Error! That pattern is not in the pattern list.")
            exit()
        k += 1 # increment k by 1

def conv_dec(y):
    test_list1 = "7 12 26 20   14 4   22 4 15   14 4   7 12 3 2   22 4 15   12 26 16 3   2 15 6 3 24 25 5   5 4 14 3 23 24 26 20 12 3 24   20 12 26 2   26 8 9 12 26 18 3 20 25 5  26 2 23 7 3 24    20 12 3   23 26 6 3   20 12 25 2 10    23 25 6 9 8 3   23 15 18 23 20 26 20 25 4 2 23  24 3 9 8 26 5 3   4 2 3   23 22 6 18 4 8   4 21   9 8 26 25 2 20 3 17 20   7 25 20 12   4 2 3  23 22 6 18 4 8   4 21   5 25 9 12 3 24 20 3 17 20"
    test_list = []
    test_list = test_list1.split('  ')
    string1 = ' '.join(test_list)
    test_list = string1.split(' ')
    for n, i in enumerate(test_list):
        if i == '':
            test_list[n] = ord(' ')

    test_list = [int(i) for i in test_list]

    s = ''
    for char in test_list:
        if char != 32:
            s += chr(char + 96)
        if char == 32:
            s += chr(char)
    return s

def dec_to_ascii(z):
    test_list = []
    test_list = z.split('  ')
    print('\n')
    string1 = ' '.join(test_list)
    test_list = string1.split(' ')
    # print("After separating individual integers and spaces: ", test_list)
    print('\n')
    for n, i in enumerate(test_list):
        if i == '':
            test_list[n] = ord(' ')
    # print("After replacing spaces with ASCII values: ", test_list)
    print('\n')

    test_list = [int(i) for i in test_list]
    # print("After converting list elements from string to int: ", test_list)
    print('\n')

    s = ''
    for char in test_list:
        if char != 32:
            s += chr(char + 96)
        if char == 32:
            s += chr(char)

    print("After converting list elements from int to ASCII: ", s)
    print('\n')

# open english word list in read mode. create a new list and fill list with the contents of text file
eng_words_file = open("words_alpha.txt", "r") # open the english word list in 'read' mode
eng_list = [] # create a list to hold each word
for line in eng_words_file: # for loop to run through the english word list text file
    eng_list.append(line.rstrip('\n')) # each element of eng_list is given a word from the file

# create and open a text file to write the newly converted patterns
out_file = open("patterns.txt", "w")
pattern_list = [] # create a list to hold all of the patterns
for line in eng_list: # for loop to read each word in the english list
    out_file.write(wrd_ptrn(line)) # call our function that was defined earlier to find patterns
out_file.close() # close the out file

# open the patterns.txt file in read mode
pattern_words_file = open("patterns.txt", "r") # open the patterns text file in read mode
for word in pattern_words_file: # for loop to run through the pattern list text file
    pattern_list.append(word.rstrip('\n')) # each element of eng_list is given a word from the file

# ask the user to find words that match a pattern or to convert a word to a pattern
print("Type '1' if you want to enter a pattern and receive a list of possible words.")
print("Type '2' if you want to enter a word and receive the pattern.")
print("Type '3' if you want to convert decimal to ASCII.")
choice = input(": ")

user_input = '' # create a string to hold the user's input
match = [] # create a list to hold all matching values

# if the user chooses to enter a pattern
if choice == '1':
    user_input = input("Enter the pattern: ") # accept and store the user input
    ptrn_wrd(pattern_list, user_input)

# if the user chooses to enter a word
elif choice == '2':
    user_input = input("Enter the word : ") # accept and store the user input
    print(wrd_ptrn(user_input))
    while user_input != "aaaaa":
        user_input = input("Enter another word or type aaaaa to quit: ")
        print(wrd_ptrn(user_input))

# if the user wants to decode numerical cipher. 
elif choice == '3':
    code = "7 12 26 20   14 4   22 4 15   14 4   7 12 3 2   22 4 15   12 26 16 3   2 15 6 3 24 25 5 " \
           "  5 4 14 3 23 24 26 20 12 3 24   20 12 26 2   26 8 9 12 26 18 3 20 25 5  26 2 23 7 3 24    " \
           "20 12 3   23 26 6 3   20 12 25 2 10    23 25 6 9 8 3   23 15 18 23 20 26 20 25 4 2 23  24 3 9 8 26 5 3  " \
           " 4 2 3   23 22 6 18 4 8   4 21   9 8 26 25 2 20 3 17 20   7 25 20 12   4 2 3  23 22 6 18 4 8   " \
           "4 21   5 25 9 12 3 24 20 3 17 20"
    decode = conv_dec('')
    print(decode)

# error message if the user's input is not 1 or 2 or 3
else:
    print("Error. That is not an option!")
    exit()

pattern_words_file.close()
eng_words_file.close()
