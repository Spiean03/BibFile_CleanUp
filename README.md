# BibFile_CleanUp
Removes unwanted entries from your .bib file

Bibtex files are ridiculously messy, and especially if you use self-generating bibfile software like Mendeley, you end up with a lot of entries that you don't want.
I'm using Latex to generate my articles/papers/documents and my knowledge in Latex is too limited to figure out how I properly adjust my bibliographystyle so that unwanted sections are not shown.
Yes, I know, there are the 
```python
"\AtEveryBibitem{\clearfield{xxx}}" 
```
and 
```python
"\AtEveryCitekey{\clearfield{yyy}}"
```
commands to clear the field conditionally for selected type and I tried, spend couple of hours figuring it out, it didn't do anything at all and got annoyed.

Here is a script that removes unwanted entries from your .bib file. No worries, a new file is created and the old one will still exist.

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
    
The function customization defines the unwanted sections. Just adjust the list with the elements you want to remove.
```python
unwanted = ["pages","keywords", "doi", "url", "abstract", "file",...]
```

Run the code et voila, the generated outputfile looks less messy now.
