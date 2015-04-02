import trieClass as tc

def primeDict(myTrie):
	diction = open("/usr/share/dict/words", 'r')
	for line in diction:
		word = line.split("\n")
		myTrie.addWord(word[0])
	print("Trie is primed!")
	return myTrie
