import time

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True

    def is_compounded_word(self, word, start, count):
        node = self.root

        for i in range(start, len(word)):
            c = word[i]

            if c not in node.children:
                return False

            node = node.children[c]

            if node.isEnd:
                if i == len(word) - 1:
                    return count >= 1

                if self.is_compounded_word(word, i + 1, count + 1):
                    return True

        return False

def find_compounded_words(file_name, trie):
    try:
        with open(file_name, 'r') as file:
            words = [line.strip() for line in file]

            words.sort(key=lambda x: len(x), reverse=True)

            start_time = time.time()
            longest_compounded_word = ''
            second_longest_compounded_word = ''

            for word in words:
                if trie.is_compounded_word(word, 0, 0):
                    if not longest_compounded_word:
                        longest_compounded_word = word
                    else:
                        second_longest_compounded_word = word
                        break

            end_time = time.time()
            duration = (end_time - start_time) * 1e6
            print(f"Longest Compound Word: {longest_compounded_word}")
            print(f"Second Longest Compound Word: {second_longest_compounded_word}")
            print(f"Time taken to process file {file_name}: {duration:.2f} microseconds\n")

    except FileNotFoundError:
        print(f"Unable to open file {file_name}")

if __name__ == "__main__":
    trie_instance = Trie()

    find_compounded_words("Input_01.txt", trie_instance)
    find_compounded_words("Input_02.txt", trie_instance)
