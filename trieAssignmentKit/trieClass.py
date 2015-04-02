#LastName:
#FirstName:
#Email:
#Comments:

from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
	isWordEnd = False # is this node a word ending node
	isRoot = False # is this a root node
	count = 0 # frequency count
	nextl = {} # Dictionary mappng each character from a-z to the child node

	def __init__(self, isRootNode):
		self.isRoot = isRootNode
		self.isWordEnd = False
		self.count = 0
		self.nextl = {}


	def addWord(self,w):
		assert(len(w) > 0)

        # YOUR CODE HERE
        # If you want to create helper/auxiliary functions, please do so.
		first = w[0]
		if (self.nextl.get(first)):
			if (len(w) == 1):
				self.nextl.get(first).count += 1
				self.nextl.get(first).isWordEnd = True
			else:
				self.nextl.get(first).addWord(w[1:len(w)])
		else:
			node = MyTrieNode(False)
			self.nextl[first] = node
			if (len(w) == 1):
				node.count += 1
				node.isWordEnd = True
			else:
				node.addWord(w[1:len(w)])
        
		return

	def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.

        # YOUR CODE HERE
		if (len(w) == 0):
			if (self.isWordEnd):
				return self.count
			else:
				return 0
		else:
			first = w[0]
			if (self.nextl.get(first)):
				return self.nextl.get(first).lookupWord(w[1:len(w)])
			else:
				return 0
        
		return 0 # TODO: change this line, please
    

	def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j

        #YOUR CODE HERE
		return self.autoCompleteHelp(w, 0)
	
	def autoCompleteHelp(self, word, index):
		if (index == len(word)):
			return self.autoFind(word)
		else:
			if (self.nextl.get(word[index])):
				return self.nextl.get(word[index]).autoCompleteHelp(word, index + 1)
			else:
				return []
		
	def autoFind(self,word):
		myKeys = self.nextl.keys()
		completions = []
		if (self.isWordEnd):
			completions.append((word, self.count))
		for i in myKeys:
			completions += self.nextl.get(i).autoFind(word + i)
		return completions
		
    
            

if (__name__ == '__main__'):
	t= MyTrieNode(True)
	lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

	for w in lst1:
		t.addWord(w)

	j = t.lookupWord('testy') # should return 0
	j2 = t.lookupWord('telltale') # should return 0
	j3 = t.lookupWord ('testing') # should return 2
	lst3 = t.autoComplete('pi')
	print('Completions for \"pi\" are : ')
	print(lst3)
    
	lst4 = t.autoComplete('tes')
	print('Completions for \"tes\" are : ')
	print(lst4)
 
    
    
     
