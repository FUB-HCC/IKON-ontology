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
* [Getty TGN]()


Includes concepts from:
-----------------------

* [Dublin Core Elements](http://purl.org/dc/elements/1.1/)
* [Dublin Core Terms](http://purl.org/dc/terms/)
* [GND Ontology](https://d-nb.info/standards/elementset/gnd#)
* [FOAF](http://xmlns.com/foaf/0.1/)
* [FRAPO](http://purl.org/cerif/frapo/)
* [SemWeb Vocab Status Ontology](http://www.w3.org/2003/06/sw-vocab-status/ns#)
* [SKOS Core](http://www.w3.org/2004/02/skos/core)


Viewing the Documentation
-------------------------

Online: [https://fub-hcc.github.io/IKON-ontology/index-en.html](https://fub-hcc.github.io/IKON-ontology/index-en.html)

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

