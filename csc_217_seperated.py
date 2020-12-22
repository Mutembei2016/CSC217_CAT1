from csc_217_attendance import data
with open('CSC_217_attendance_ week1_.txt') as fo:
    def csc_217_Separated():
        """ Group the words by length in a text file. """


    if list(" ") =='B141':  # Did the user not supply a file name?
         print('CSC_217_IT.txt')
    elif list(" ") =='B135':
         print('CSC_217_Computer.txt')
    else:  # User provided file name
         print('lecturer.txt')
    groups = []  # Initialize grouping list

with open("CSC_217_attendance_ week1_.txt", 'r') as fo:  # Open the file for reading
        content = fo.read()  # Read in content of the entire field
    words = content.split("B141", "B135")  # Make list of individual words

for word in words:
        word = word.upper()  # Make the word all caps
    # Compute the word's length
    size = len(word)
    groups[size].add(word)
    # Show the groups
for size, group in enumerate(groups):
        print(size, ':', group

csc_217_Separated()
