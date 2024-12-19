def catHatCount(str,word1,word2):
  words=str.split()
  count1=words.count(word1)
  count2=words.count(word2)
  if(count1==count2):
    return True
  else:
    return False

str=input("enter a string: ")
#word1="cat"
#word2="hat"
word1=input("enter some string1")
word2=input("enter some word2")
catHatCount(str,word1,word2)
