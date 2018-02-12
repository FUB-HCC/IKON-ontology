#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
header = ['Subject', 'Type', 'Parent', 'Label', 'Definition', 'Domain', 'Range', 'Version', 'Status', 'Notizen']

# einige Attribute in der prod.owl heißen anders als gegeben ()

qres = g.query(
   """
   SELECT DISTINCT ?s ?type ?parent ?label ?definition ?domain ?range ?version ?status ?notes
   WHERE {
       ?s a ?type .
       
       OPTIONAL {
           ?s terms:hasVersion ?version .
       }
       OPTIONAL {
           ?s skos:definition ?definition .
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
       FILTER (!isBlank(?s))
   }
   """)



with open(csvfileName, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(header)
    for row in qres:
        writer.writerow(r if r is not None else '' for r in row)



# write Excel file
with Workbook(xlsfileName) as workbook:
    worksheet = workbook.add_worksheet()
    worksheet.autofilter(0,0,0,len(header)-1)
    #define column header style
    header_style = workbook.add_format({'bold': True, 'bg_color':'yellow' })
    for i, column in enumerate(header):
        worksheet.write(0,i,column, header_style)
    for i, row in enumerate(qres):
        for j, column in enumerate(row):
            worksheet.write(i+1, j, column)

workbook.close()

