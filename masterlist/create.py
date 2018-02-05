#!/usr/bin/env python

import sys
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, OWL
import csv

import os
import glob
from xlsxwriter.workbook import Workbook



outputName = "masterlist"

# -------------------------------------------

csvfileName = "./%s.csv" % outputName
xlsfileName = "./%s.xlsx" % outputName


# kdfs = URIRef("http://ontologies.mfn-berlin.de/ikon")

g = Graph()
# g.load('https://raw.githubusercontent.com/FUB-HCC/IKON-ontology/master/prod.owl')
g.parse('../prod.owl')

print '%s triples' % len(g)

rows = []
header = []

qres = g.query(
    """
    SELECT DISTINCT ?s ?type ?parent ?version ?description ?domain ?range
    WHERE {
        ?s rdf:type ?type .
        OPTIONAL {
            ?s <http://purl.org/dc/terms/hasVersion> ?version .
            ?s <http://purl.org/dc/terms/description> ?description .
            ?s rdfs:range ?range .
            ?s rdfs:domain ?domain .
        }
        OPTIONAL {
            ?s rdfs:subClassOf ?parent .
        }
    }
    """)




with open(csvfileName, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['Subject', 'Type', 'Parent', 'Version', 'Description', 'Domain', 'Range', 'Status', 'Notizen'])
    for row in qres:
        writer.writerow([unicode(r).encode("utf-8") for r in row])


# write Excel file
with Workbook(xlsfileName) as workbook:
	worksheet = workbook.add_worksheet()
	# with open(csvfile, 'rt', encoding='utf8') as f:
	with open(csvfileName, 'rt') as f:
	    reader = csv.reader(f)
	    for r, row in enumerate(reader):
	        for c, col in enumerate(row):
	            worksheet.write(r, c, col)
# workbook.close()



