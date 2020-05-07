from random import randint
def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()  
  randomQuote = randint(0,(len(quotes)-1))
  print(quotes[randomQuote])

if __name__== "__main__":
  primary()
