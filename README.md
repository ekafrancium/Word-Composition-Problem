## Trie-based Compounded Word Finder

## Overview
This Python script is designed to identify the longest and second-longest compounded words within a list using a trie data structure. The program reads a list of words from a file, sorts them by length in descending order, and iterates through the sorted list to find compounded words.

## How to Execute
1. Clone the GitHub repository containing the code.
2. Ensure you have Python installed on your system.
3. Run the script by executing the command: `python Longest_compound_words.py`. Replace `Longest_compound_words.py` with the actual name of the Python script.

## Design Decisions
- The program utilizes a trie data structure to efficiently store and search for words.
- Words are sorted in descending order of length to prioritize longer words during the search.
- The script employs a recursive approach to check for compounded words, iterating through the trie and considering the current word's prefixes.

## Sample Usage
'''cmd
python Longest_compound_words.py


## Output
The program prints the longest and second-longest compounded words found in the input files, along with the time taken to process each file.

## File Structure
- `Longest_compound_words.py`: Main Python script.
- `Input_01.txt`, `Input_02.txt`: Sample input files containing lists of words.

Feel free to customize the input files or integrate the script into your project. For any issues or improvements, please open an [issue](link-to-issues) or submit a [pull request](link-to-pull-requests).
