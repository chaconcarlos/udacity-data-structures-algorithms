#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[15]:


from collections import defaultdict 

## Represents a single node in the Trie   
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = defaultdict(TrieNode)
    
    def insert(self, char):
        ## Add a child node in this Trie
        return self.children[char]
    
    def find(self, prefix_char):
        ## Find the Trie node that represents this prefix
        result = self.children[prefix_char]
        
        if result.is_word == False and len(result.children) == 0:
            result = None
            
        return result
    
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        if word:         
            current_node = self.root

            for char in word:
                current_node = current_node.insert(char)
            
            current_node.is_word = True
                
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        
        if prefix:
            for char in prefix:
                current_node = current_node.find(char)

                if current_node is None:
                    current_node = None
                    break
        else:
            current_node = None
            
        return current_node


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[16]:


from collections import defaultdict 

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = defaultdict(TrieNode)
    
    def insert(self, char):
        ## Add a child node in this Trie
        return self.children[char]
    
    def find(self, prefix_char):
        ## Find the Trie node that represents this prefix
        result = self.children[prefix_char]
        
        if result.is_word == False and len(result.children) == 0:
            result = None
            
        return result
      
    def suffixes(self):
        suffix_list = []
        
        for char in self.children.keys():
            child_node = self.children[char]
            
            if child_node.is_word:
                suffix_list.append(char)
                
            child_suffixes = child_node.suffixes()
            
            for suffix in child_suffixes:
                suffix_list.append(char + suffix)
        
        return suffix_list


# # Testing the trie
# Now the code is complete and can get suffixes, let's run some testing.

# In[23]:


word_trie = Trie()

word_list = [
    "ant", "ad", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod",
    "super"
]

for word in word_list:
    word_trie.insert(word)

# Find a regular prefix, one letter.
# Output: ['nt', 'nthology', 'ntagonist', 'ntonym', 'd']
prefix = 'a'
prefix_node = word_trie.find(prefix)
print(prefix_node.suffixes())

# Find a regular prefix, big input.
# Output: ['y']
prefix = 'trigonometr'
prefix_node = word_trie.find(prefix)
print(prefix_node.suffixes())

# Find a whole word as a prefix, big input.
# Output: []
prefix = 'trigonometry'
prefix_node = word_trie.find(prefix)
print(prefix_node.suffixes())

# Find a prefix that only has one word.
# Output: ['per']
prefix = 'su'
prefix_node = word_trie.find(prefix)
print(prefix_node.suffixes())

# Find a prefix that is not in the trie.
# Output: None
prefix = 'wrong'
prefix_node = word_trie.find(prefix)
print(prefix_node)

# Empty prefix parameter.
# Output: None
prefix = ''
prefix_node = word_trie.find(prefix)
print(prefix_node)

# None prefix.
# Output: None
prefix = None
prefix_node = word_trie.find(prefix)
print(prefix_node)


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[4]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[5]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:





# In[ ]:




