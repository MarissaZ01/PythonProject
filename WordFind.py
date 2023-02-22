word = 'geeks for geeks'

result=word.find('geeks')
print("substring 'geeks' found at index: ", result)

result=word.find('for')
print("substring 'for' found at index: ", result)

if word.find('pawan') !=1:
    print("Contains given substring ")
else :
    print("Doesn't contains given substring ")