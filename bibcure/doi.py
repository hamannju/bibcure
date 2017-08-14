from __future__ import print_function
from builtins import input
from doitobib.crossref import get_bib_from_doi
import bibtexparser


def update_bib(bib):
    if "doi" in bib:
            found, bib_string = get_bib_from_doi(bib["doi"])
            if found:
                bib = bibtexparser.loads(bib_string).entries[0]
    return bib


def update_bibs_from_doi(bibs):
    action = input("Update bibs from doi?y(yes)/n(do nothing)")

    if action not in ("y", "n"):
        return update_bibs_from_doi(bibs)

    if action == "n":
        return bibs

    for i, bib in enumerate(bibs):
        bibs[i] = update_bib(bib)

    return bibs
