"""
Created on Fri May 18 16:10:01 2018
@author:    Andreas Spielhofer
            Ph.D. Candidate
            Physics Departement
            McGill University
            Montreal, Canada
@contact:   andreas.spielhofer@mail.mcgill.ca
"""

import datetime
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.customization import *
import re

'''
Adjust input_file, output_file and capitalization to your needs:
'''
input_file = "library.bib"
output_file = "libraryclean.bib"
capitalization = True


now = datetime.datetime.now()
print("{0} Cleaning duff bib records from {1} into {2}".format(now, input_file, output_file))

# Let's define a function to customize our entries.
# It takes a record and return this record.
def customizations(record, capitalization=capitalization):
    record = type(record)
    record = page_double_hyphen(record)
    record = convert_to_unicode(record)
    ## delete the following keys.
    unwanted = ["keywords", "doi", "url", "abstract", "file", "isbn", "link", "keyword", "mendeley-tags", "annote", "pmid", "chapter", "institution", "issn", "month"]
    
    for val in unwanted:
        record.pop(val, None)

    if capitalization == True:
        for element in record['title']:
            for i in element:
                if i.isupper():
                    string = "{"+str(i)+"}"
                    i.replace(i,string)
       
    return record


bib_database = None
with open(input_file) as bibtex_file:
    parser = BibTexParser()
    parser.customization = customizations
    parser.ignore_nonstandard_types = False
    bib_database = bibtexparser.load(bibtex_file, parser=parser)

if bib_database :
    now = datetime.datetime.now()
    success = "{0} Loaded {1} found {2} entries".format(now, input_file, len(bib_database.entries))
    print(success)
else :
    now = datetime.datetime.now()
    errs = "{0} Failed to read {1}".format(now, input_file)
    print(errs)
    sys.exit(errs)

bibtex_str = None

if bib_database:
    writer = BibTexWriter()
    writer.order_entries_by = ('author', 'year', 'type')
    bibtex_str = bibtexparser.dumps(bib_database, writer)    
    with open(output_file, "w") as f:
        f.write(bibtex_str.encode('utf-8'))

if bibtex_str:
    now = datetime.datetime.now()
    success = "{0} Wrote to {1} with len {2}".format(now, output_file, len(bibtex_str))
    print(success)
else:
    now = datetime.datetime.now()
    errs = "{0} Failed to write {1}".format(now, output_file)
    print(errs)
    sys.exit(errs)
