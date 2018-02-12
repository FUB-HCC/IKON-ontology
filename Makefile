.PHONY: docs tests masterlist

default:
	##
	##  Makefile for IKON Ontology
	##
	##   make tests			code style and formatting checks
	##   make docs			build the documentation
	##   make docs-fresh	build the documentation from scratch
	##   make docs-refresh	build only the variable part of the documentation
	##   make clean-docs	remove docs
	##   make deploy		push to github
	##

tests:
	# checking ontology
	# TODO

docs-fresh: clean-docs
	# initial build
	java -jar ../tools/WIDOCO/jar/widoco-1.4.1-jar-with-dependencies.jar -ontFile ./prod.owl -outFolder ./docs -getOntologyMetadata -oops -rewriteAll -saveConfig ./widocoConfigFile -includeImportedOntologies -htaccess -webVowl -licensius
	cp src/docs/sections/* ./docs/sections
	cp ./readme.md ./docs/readme.md

docs-refresh:
	# subsequent builds
	java -jar ../tools/WIDOCO/jar/widoco-1.4.1-jar-with-dependencies.jar -ontFile ./prod.owl -outFolder ./docs -getOntologyMetadata -oops -rewriteAll -confFile ./widocoConfigFile -includeImportedOntologies -htaccess -webVowl -licensius -crossRef

docs-rebuild: docs-fresh
	# produce ontology documentation

docs: docs-refresh
	# refresh ontology documentation

clean-docs:
	# remove ontology documentation
	rm -rf docs/

deploy:
	# push to github
	git add -A
	git commit
	git push

reason:
	java -jar ./bin/HermiT/HermiT.jar --prettyPrint --no-prefixes --consistency dev.owl

masterlist:
	rapper ./prod.owl -o ntriples > ./masterlist/prod.n3
	# --explain
	arq --results=csv --data=./masterlist/prod.n3 --query=./masterlist/query.rq > ./masterlist/masterlist.csv
