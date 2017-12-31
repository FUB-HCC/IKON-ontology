IKON Ontology
===================

| Files/Folders | Description                                    |
| ------------- |:----------------------------------------------:|
| dev.owl       | Development version of ontology (with imports) |
| prod.owl      | Production version of ontology                 |
| docs/         | Documentation of ontology                      |

Viewing the Documentation
-------------------------

```
cd ./docs/
php -S localhost:8080
Go to http://localhost:8080/index-en.html
```

Building the Documentation
--------------------------

`./createDocumentation.sh`

Requires widoco .jar file, e.g. ../tools/WIDOCO/jar/widoco-1.4.1-jar-with-dependencies.jar
