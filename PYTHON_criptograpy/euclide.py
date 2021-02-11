def main():

    a = int(input("inserisci il numero A"))

    b = int(input("inserisci il numero B"))

    print(euclide(a,b))
    

def euclide(a,b):
    if b > a:
        a, b = b, a

    while True:
        nuovo_a = a % b
        print(f"questo è nuovo_a{nuovo_a}")
        if nuovo_a == 0:
            return b
        else:
            a = b
            b = nuovo_a



if __name__ == "__main__":
    main()