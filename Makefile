.PHONY: docs tests masterlist prod deploy check

default:
	##
	##  Makefile for IKON Ontology
	##
	##   make tests			code style and formatting checks
	##   make docs			build the documentation
	##   make docs-fresh	build the documentation from scratch
	##   make docs-refresh	build only the variable part of the documentation
	##   make clean-docs	remove docs
	##   make check  		check satisfyability
	##   make prod  		produce the production ontology from dev.owl
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
	cp ./docs/index-en.html ./docs/index.html

docs-refresh:
	# subsequent builds
	java -jar ../tools/WIDOCO/jar/widoco-1.4.1-jar-with-dependencies.jar -ontFile ./prod.owl -outFolder ./docs -getOntologyMetadata -oops -rewriteAll -confFile ./widocoConfigFile -includeImportedOntologies -htaccess -webVowl -licensius -crossRef
	cp src/docs/sections/* ./docs/sections
	cp ./readme.md ./docs/readme.md
	cp ./docs/index-en.html ./docs/index.html

docs-rebuild: docs-fresh
	# produce ontology documentation

docs: docs-refresh
	# refresh ontology documentation

clean-docs:
	# remove ontology documentation
	rm -rf docs/

check:
	java -jar ./bin/HermiT/HermiT.jar --no-prefixes --no-prefixes --consistency dev.owl

deploy:
	# push to github
	git add -A
	git commit
	git push

masterlist:
	./masterlist/create.py
