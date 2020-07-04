import random

def primary(n_quotes):
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = 13
    for i in range(0, n_quotes):
        rnd = random.randint(0, last)
        print(quotes[rnd].strip())

if __name__== "__main__":
    primary(2)
