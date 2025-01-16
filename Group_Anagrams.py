#Challenge: Group Anagrams
#This challenge is about finding the anagrams in a list.
#Given a list of strings that contains anagrams, write a function to print pairs of those anagrams.

def anagrams(lst):
  dictionary = {}
  result = []
    
  for strings in lst:
    key = ''.join(sorted(strings))
    
    if key in dictionary.keys():
      dictionary[key].append(strings)
    else:
      dictionary[key]=[]
      dictionary[key].append(strings)
  for key, value in dictionary.items():
    if len(value)>=2:
      result.append(value)
  return sorted(result)
