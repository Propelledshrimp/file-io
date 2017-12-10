with open('words_alpha.txt', 'r') as f:
    words = f.read().splitlines()

#total words
print(len(words))

#5 letter words
count = 0
for w in words:
    if len(w) == 5:
        count += 1

print(count)

#words with more than 7 letters
count = 0
for w in words:
    if len(w) > 7:
        count += 1

print(count) 

#total characters used in all words
count = 0
for w in words:
    count += len(w)

print(count)

#Does not contain "e" 
count = 0
for w in words:
    if 'e' not in w:
        count +=1

print(count)

#begin and end with the same letter
count = 0
for w in words:
    if w[0] == w[-1]:
        count += 1
        
print(count) 

#contains 3 As 
count = 0
for w in words:
    if w.count('a') == 3:
        count += 1
        
print(count) 

# Q not followed by U
count = 0
for w in words:
    if 'q' in w and 'qu' not in w:
        count += 1

print(count) 
 
