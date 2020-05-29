#def sympa():
#   print("Keep it logically awesome.")
import random
f = open("quotes.txt")
quotes = f.readlines()
f.close()
#Note If you want to add or remove quotes from your text file, you could change the last variable to update automatically:
#last = len(quotes) - 1
last = 13
rnd = random.randint(0, last)
print(quotes[rnd])

#if __name__== "__main__":
#  sympa()
