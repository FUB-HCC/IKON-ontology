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

print('prod.owl contains %s triples' % len(g))

rows = []
header = []

# einige Attribute in der prod.owl heißen anders als gegeben ()

qres = g.query(
   """
   SELECT DISTINCT ?s ?type ?parent ?label ?description ?domain ?range ?version ?status ?notes
   WHERE {
       ?s a ?type .
       
       OPTIONAL {
           ?s terms:hasVersion ?version .
       }
       OPTIONAL {
           ?s rdfs:comment ?description .
       }
       OPTIONAL {
           ?s rdfs:range ?range .
       }
       OPTIONAL {
           ?s rdfs:domain ?domain .
       }
       OPTIONAL {
           ?s skos:scopeNote ?notes
       }
       OPTIONAL {
           ?s ns:term_status ?status .
       }
       OPTIONAL {
           ?s rdfs:subClassOf ?parent .
       }
       OPTIONAL {
           ?s rdfs:label ?label .
           FILTER (lang(?label) = "de")
       }
       
   }
   """)




with open(csvfileName, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['Subject', 'Type', 'Parent', 'Label', 'Description', 'Domain', 'Range', 'Version', 'Status', 'Notizen'])
    for row in qres:
        writer.writerow([r if r is not None else '' for r in row])


# write Excel file
#with Workbook(xlsfileName) as workbook:
#	worksheet = workbook.add_worksheet()
#	# with open(csvfile, 'rt', encoding='utf8') as f:
#	with open(csvfileName, 'rt') as f:
#		reader = csv.reader(f)
#		for r, row in enumerate(reader):
#			for c, col in enumerate(row):
#               worksheet.write(r, c, col)
#
# workbook.close()
