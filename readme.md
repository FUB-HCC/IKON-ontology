IKON Ontology
===================

| Files/Folders | Description                                    |
| ------------- |:----------------------------------------------:|
| dev.owl       | Development version of ontology (with imports) |
| prod.owl      | Production version of ontology                 |
| docs/         | Documentation of production ontology           |


Basis
-----

* [Kerndatensatz Forschung - Basis](http://kerndatensatz-forschung.de/version1/technisches_datenmodell/owl/Basis)
* [Kerndatensatz Forschung - Meta](http://kerndatensatz-forschung.de/owl/Meta)


Associated Ontologies
---------------------

* [DFG Fachsystematik](https://joetm.github.io/dfg-fachsystematik/index-en.html)
* Getty TGN [TODO]


Includes concepts from:
-----------------------

* [Kerndatensatz Forschung (Basis)](http://kerndatensatz-forschung.de/version1/technisches_datenmodell/owl/Basis)
* [Kerndatensatz Forschung (Meta)](http://kerndatensatz-forschung.de/owl/Meta)
* [Dublin Core Elements](http://purl.org/dc/elements/1.1/) - Dublin Core Metadata Initiative (DCMI)
* [Dublin Core Terms](http://purl.org/dc/terms/) - Dublin Core Metadata Initiative (DCMI)
* [Integrated Authority File (GND)](https://d-nb.info/standards/elementset/gnd#) - Deutsche Nationalbibliothek
* [Friend of a Friend (FOAF)](http://xmlns.com/foaf/0.1/)
* [Vcard](http://www.w3.org/2006/vcard/ns)
* [Funding, Research Administration and Projects Ontology (FRAPO)](http://purl.org/cerif/frapo)
* [SemWeb Vocab Status Ontology](http://www.w3.org/2003/06/sw-vocab-status/ns#)
* [Simple Knowledge Organization System (SKOS Core)](http://www.w3.org/2004/02/skos/core)
* [DFG-Fachsystematik](https://github.com/joetm/dfg-fachsystematik/raw/master/dfg-fachsystematik.owl)
* [Integrated Authority File (GND)](http://d-nb.info/standards/elementset/gnd) - Deutsche Nationalbibliothek
* [Time ontology](http://www.w3.org/2006/time) - W3C
* [Vann](http://purl.org/vocab/vann/)
* [SemWeb Vocab Status ontology](http://www.w3.org/2003/06/sw-vocab-status/ns)


Viewing the Documentation
-------------------------

Online: [https://fub-hcc.github.io/IKON-ontology/docs/index-en.html](https://fub-hcc.github.io/IKON-ontology/docs/index-en.html)

Locally:
```
cd ./docs/
php -S localhost:8080
Go to http://localhost:8080/index-en.html
```

Building the Documentation
--------------------------

`make docs`

Requires widoco .jar file, e.g. ../tools/WIDOCO/jar/widoco-1.4.1-jar-with-dependencies.jar

See [Makefile](https://github.com/FUB-HCC/IKON-ontology/blob/master/Makefile) for more commands.

