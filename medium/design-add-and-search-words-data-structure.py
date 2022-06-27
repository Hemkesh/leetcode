# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Best submission time: 132ms

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordList = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if len(word) not in self.wordList:
            self.wordList[len(word)] = [word]
        else:
            self.wordList[len(word)].append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if len(word) in self.wordList:
            lst = self.wordList[len(word)]
            if "." not in word:
                if word in lst:
                    return True
                else:
                    return False
            else:
                flag = 0
                for x in lst:
                    for i, char in enumerate(x):
                        if word[i] == ".":
                            flag = 1
                        elif char != word[i]:
                            flag = 0
                            break
                        else:
                            flag = 1
                    if flag == 1:
                        return True
        
                return False
                     
        else:
            return False