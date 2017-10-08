# VSCode, Code Runner: Run with CTRL+ALT+N
# https://www.youtube.com/watch?v=k9TUPpGqYTo&index=2&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
# Corey Schafer Python Tutorial

# message = 'John\'s dog started talking. It said: "Sup Dawg"'
# multiline_message="""Wow what a multi line message.
# It's multiline-age is over 9000!!!
# """
# print(multiline_message)

####### SLICING #######

message ="Hello World"

# print(len(message)) #len(str) gives length of str >>>11
# print(message[0]) #index starts at 0, can access indiv letters of string >>>H
# print(message[0:5]) #[start index(inclusive) : end index (exclusive)] >>>Hello
# print(message[:5]) #[start index[default] : end index (exclusive)] >>>Hello
# print(message[6:]) #[start index(inclusive) : end index [default]] >>>World

#can also use negative indices
# print(message[-1]) #>>>d
# print(message[-5:]) #>>>World
# print(message[:11:2]) # list[start:end:step] can also do neg step >>HloWrd
# print(message[::-1]) #will step through in reverse - reversing the string

# print(message.upper()) #capitalizes ; lower() makes undercase
# print(message.count('Hello')) #returns the amount of times 'Hello' appears in str >>>1
# print(message.find('Wor')) #gives index where 'Wor' begins or -1 if not found >>6

# new_message = message.replace('World','Universe')
# print(new_message)

greeting = 'Hello'
name = "John"
# message = greeting + ', ' + name

##### Formatted String
# message = '{}, {}. Welcome!'.format(greeting, name)
# message = f'{greeting}, {name.upper()}. Welcome!' #only works in python 3.5 and above
# print(message)
# print(dir(name)) #>>>methods/attributes available on name variable
# print(help(str)) #>>>methods/attributes available on str types
# print(help(str.lower)) #specifically what lower does on str

