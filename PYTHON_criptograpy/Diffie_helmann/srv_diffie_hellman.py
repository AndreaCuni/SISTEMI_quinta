import socket as sck
import conf as cnf #library, g e N are here

def main():
    while(True):
        b = int(input("Insert a value for b:\t")) 
        if(b < cnf.N):
            break
        print(f"b must be < {cnf.N}, try again you'll be luckyer")

    s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    s.bind(('localhost',6000))
    s.listen()

    conn,_ = s.accept()

    A = (conn.recv(4096)).decode()              #receive A = (cnf.g ^ a) % cnf.N
    B = (cnf.g^b) % cnf.N 

    conn.sendall(str(B).encode()) 
    print(f"Number = {(int(A)^b) % cnf.N}")    #print number = (A ^ b) % cnf.N
    s.close()
    conn.close()

if __name__ == "__main__":
    main()
