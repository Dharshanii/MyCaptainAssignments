import operator
def most_frequent(word):
  frequency= {}
  for i in word:
      if i in frequency:
        frequency[i] += 1
      else:
        frequency[i] = 1
  print(dict( sorted(frequency.items(), key=operator.itemgetter(1),reverse=True))
)
s=input('Enter the word: ')
most_frequent(s)