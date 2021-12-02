#The goal of this program is to show a random walk simulation
import random
Intial_data = [0,4]

Domain = [0,1]



def print_graph(Intial_data,Domain):
    for i in range(len(Domain)):
        if(Domain[i] >= 0):
            print(" " + str(Domain[i]), end = " ")
            for j in range(Intial_data[i]):
                print("*",end =" " )

            print("")
        else :
            print(Domain[i], end = " ")
            for j in range(Intial_data[i]):
                print("*",end =" " )

            print("")
    print("")


def one_step():
    for i in range(len(Domain)):
        num = Intial_data[i]
        for j in range(num):
            n = random.randrange(2)
            if n == 0:
                if i != 0:
                    Intial_data[i-1] = Intial_data[i-1] + 1
                    Intial_data[i] = Intial_data[i] - 1
            else:
                if i != 1:
                    Intial_data[i + 1] = Intial_data[i + 1] + 1
                    Intial_data[i] = Intial_data[i] - 1

for i in range(10):
    one_step()
    print_graph(Intial_data, Domain)