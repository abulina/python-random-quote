f = open("quotes.txt", "r")

for q in f:
    quotes = q.strip('[]')
    print(quotes)

f.close()


