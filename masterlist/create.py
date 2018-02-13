#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, OWL
import csv

import re

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


header = ['Subject', 'Type', 'Parent', 'Label (DE)', 'Label (EN)', 'Definition (DE)', 'Definition (EN)', 'Domain', 'Range', 'Version', 'Status', 'Notizen']

# einige Attribute in der prod.owl heißen anders als gegeben ()


#    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#    prefix meta: <http://kerndatensatz-forschung.de/owl/Meta#>
#    prefix dct: <http://purl.org/dc/terms/>
#    prefix owl: <http://www.w3.org/2002/07/owl#>
#    prefix status: <http://www.w3.org/2003/06/sw-vocab-status/ns#>
#    prefix skos: <http://www.w3.org/2004/02/skos/core#>
#    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#    prefix dce: <http://purl.org/dc/elements/1.1/>
qres = g.query("""
    SELECT DISTINCT ?subject ?type ?parent ?labelDE ?labelEN ?definitionDE ?definitionEN ?domain ?range ?version ?status ?notes
    WHERE {
       ?subject a ?type .
       
       OPTIONAL {
           ?subject terms:hasVersion ?version .
       }
       OPTIONAL {
           ?subject skos:definition ?definitionDE .
           FILTER (lang(?definitionDE) = "de")
       }
       OPTIONAL {
           ?subject skos:definition ?definitionEN .
           FILTER (lang(?definitionEN) = "en")
       }
       OPTIONAL {
           ?subject rdfs:range ?range .
       }
       OPTIONAL {
           ?subject rdfs:domain ?domain .
       }
       OPTIONAL {
           ?subject skos:scopeNote ?notes
       }
       OPTIONAL {
           ?subject ns:term_status ?status .
       }
       OPTIONAL {
           ?subject rdfs:subClassOf ?parent .
       }
       OPTIONAL {
           ?subject rdfs:label ?labelDE .
           FILTER (lang(?labelDE) = "de")
       }
       OPTIONAL {
           ?subject rdfs:label ?labelEN .
           FILTER (lang(?labelEN) = "en")
       }
       FILTER (!isBlank(?subject))
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

