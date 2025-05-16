#commacode

print("K.trisha,USN:1AY24AI051,SEC:M")

def list_to_string(items):
  if not items:
     return
  elif len(items)==1:
     return items[0]
  elif len(items)==2:
     return f'{items[0]} and {items[1]}'
  else:
     return ', '. join(items[:-1]) + 'and' + items[-1]
items = ['apples','bananas','tofu','cats']
print(list_to_string(items))