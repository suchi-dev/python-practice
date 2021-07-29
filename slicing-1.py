word ="supercalifragilisticexpialidocious"
print(word[-2])
print(word[-5])
print(word.index("cali"))
print(word.index("fragi"))
print(word[word.index("cali"): word.index(("fragi"))])
print(word[word.index("docious")::])
print(word[word.index("fragilistic"): word.index("exp")])
