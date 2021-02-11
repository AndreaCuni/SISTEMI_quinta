import math

def is_primo(n):
    
    bruteforce_numbers = []
    for i in range (2,int(math.sqrt(n) + 1)):
        bruteforce_numbers.append(i)
    
    for number in bruteforce_numbers:
        if n != number and n % number == 0:
            return 0

    return 1


def scomposizione(n):

    if is_primo(n):

        print(f"il numero {n} è un numero primo")
        return [n]

    fattori = []    
    corrente = n

    for i in range(2,int(n/2)+1):
        switch = 1
        
        while switch:
            if (corrente % i) == 0:
                fattori.append(i)
                corrente = corrente / i
            else:
                switch = 0

    return fattori


def main():
    print(scomposizione(42))

if __name__ == "__main__":
    main()