def longest(string):
    #print(string)
    string = string.split()
    #print(string)
    count = 0
    second = ''
    for i in string:
        if i.isalpha() == True:
            if len(i) > len(second):
                second = i
        else:
            for j in i:
                if j.isalpha() == True:
                    j.re
    return second

def main():

    print(longest("abcd! jdifjd djijfid uiu"))
if __name__ == '__main__':
    main()

