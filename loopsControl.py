

def  main():
    word = "python"
    word2 = ""
    for letter in word:
        if(letter=="p" or letter == "t"):
            continue
        elif(letter == "o"):
            break
        word2 = word2 + letter
    print(word2)
if __name__ == '__main__':main()

