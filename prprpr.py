from collections import Counter

sentence = "Amidst the bustling streets of the city, there lies a quaint little café known for its aromatic coffee and freshly baked pastries. The warm ambiance and the soft murmur of conversation create a welcoming haven for both the weary traveler and the busy local. As patrons sip on their steaming beverages, they often find themselves lost in the café's enchanting world, where time seems to slow down and the worries of the day melt away. It's a place where every cup of coffee tells a story, and every visit leaves a lasting memory."

words = sentence.split()
print(words)
word = dict(Counter(words))
print(word)
