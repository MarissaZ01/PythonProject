sentence=input('Type Sentence : ')
count={i:0 for i in'aiueoAIUEO'}

for char in sentence :
    if char in count :
        count[char]+=1
for k,v in count.items():
    print(k,v)
    
    