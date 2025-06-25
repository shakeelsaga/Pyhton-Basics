def count_words(filename):
    try:
        with open(filename, 'r') as file:
            word_count = 0
            lines = file.readlines()
            for line in lines:
                word_count += len(line.split())
            print(f"The file '{filename}' contains {word_count} words.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")

if __name__ == "__main__":
    print("Welcome to the WordCounter script!\n")
    print("This script counts the number of words in a specified text file.")
    print("Please ensure the file is in the same directory as this script or provide the full path.\n(e.g., 'Enter the filename to count words: /Users/robin/essay.txt')\n")
    
    filename = input("Enter the filename to count words: ")
    count_words(filename)
    print("\nThank you for using the WordCounter script!")