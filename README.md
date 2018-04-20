# BibFile_CleanUp
Removes unwanted entries from your .bib file

Bibtex files are ridiculously messy, and especially if you use automatically generating bibfile software like Mendeley, you end up with a lot of entries in your .bib-file that you don't want.
I'm using Latex to generate my articles/papers/documents and my knowledge in Latex is too limited to figure out how I properly adjust my bibliographystyle so that unwanted sections are not shown.
Yes, I know, there are the 
```
\AtEveryBibitem{\clearfield{xxx}} 
\AtEveryCitekey{\clearfield{yyy}}
```
commands to clear the field conditionally for selected type and I tried, spend couple of hours figuring it out, it didn't do anything at all and got annoyed. So the brute-force solution is to just remove the unwanted entries from the .bib-file.

So, why U not use Python to remove unwanted entries from your bib-file? The python-script presented here does exactly this. No worries, a new bib-file is created and the old one will remain unchanged.

## Requires:
First, this code runs on Python 2.7, so make sure you have it.
Second, install the bibtexparser package, you can just use pip:
```python
pip install bibtexparser
```

## Adjustments:
Next, adjust the input file and the output file:

```python
input_file = "library.bib"
output = "cleaned_library.bib"
```
Also, for some reasons not every bibliographystyle keeps the capitalizations of letters. This is annoying. I especially want the uppercase letters kept in "title". If you want the letters to be capitalized, change

```python
captialization = True
```
if not, change it to False. The script will replace the letters (eg. "A", "B"...) with ({A}, {B}...). The brackets force the letters to be capitalized.

    
The function customization defines the unwanted sections. Just adjust the list with the elements you want to remove.
```python
unwanted = ["pages","keywords", "doi", "url", "abstract", "file",...]
```

Run the code et voila, the generated outputfile looks less messy now.

I wish I could write a python script that lets my apartment look less messy too...
