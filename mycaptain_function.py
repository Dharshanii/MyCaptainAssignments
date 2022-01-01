def most_frequent(word):
  frequency= {}
  for i in word:
      if i in frequency:
        frequency[i] += 1
      else:
        frequency[i] = 1
  print(frequency)
s=input('Enter the word: ')
most_frequent(s)