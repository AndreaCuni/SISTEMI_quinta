import socket as sck
import conf as cnf #library where you can find g e N

def main():
    c = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    c.connect(('localhost',6000))
    while(True):
        a = int(input("Insert a value for a:\t"))
        if(a < cnf.N):
            break
        print(f"a must be < {cnf.N}, try again, you'll be luckyer")

    A = (cnf.g^a) % cnf.N 
    c.sendall(str(A).encode()) 
    
    B = (c.recv(4096)).decode()                 #receive B = (cnf.G ^ b) % cnf.N
    print(f"Number = {(int(B)^a) % cnf.N}")    #print number = (B ^ a) % cnf.N
    c.close()

if __name__ == "__main__":
    main()
