def romanToInt( s: str) -> int:
    if len(s) <= 15 and len(s) >= 1  :
        symbols = { "I" : 1 ,\
                    "V" : 5 ,\
                    "X" : 10,\
                    "L" : 50,\
                    "C" : 100,\
                    "D" : 500,\
                    "M" : 1000}
        count = 0 ; 
        i = 0 ;
        while ( i <= len(s) - 1 ) : 
            if ( i + 1 ) <= (len(s) - 1): 
                if symbols.get(s[i+1]) > symbols.get(s[i])  : 
                    count += symbols.get(s[i+1]) - symbols.get(s[i])
                    i += 1 
                else :
                    count += symbols[s[i]]
                i += 1 
            else :
                count += symbols[s[i]]
                i += 1 
        return count 


def main(): 
    print(romanToInt("III"))


if __name__ == "__main__" :main()

