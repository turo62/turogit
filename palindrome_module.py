def palindrome(str):
    str = str.replace(" ","")
    str = str.lower()
    str2 = str[::-1]
    print(str2)
    if str == str2:
        return True
    else:
        return False
    

def main():
    string = input("Enter a text with no punctuation mark: ")
    palindrome(string)


if __name__ == '__main__':
    main()
