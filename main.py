def read_file(path_to_file):
    dictonary_of_letters = {}
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        number_of_words = len(words)
        

        print(f"-- begin report of {path_to_file}")
        print(f"Number of words: {number_of_words}")

        for word in words:
            for letter in word:
                if letter in dictonary_of_letters:
                    dictonary_of_letters[letter] += 1
                else:
                    dictonary_of_letters[letter] = 1
        
        for i in dictonary_of_letters.items():
            print(f"the character '{i[0]}' occured {i[1]}")


read_file('books/frankenstein.txt')
