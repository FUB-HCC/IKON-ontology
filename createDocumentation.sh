#!/bin/bash

# initial build
# java -jar ../tools/WIDOCO/jar/widoco-1.4.1-jar-with-dependencies.jar -ontFile ./prod.owl -outFolder ./docs -getOntologyMetadata -oops -rewriteAll -saveConfig ./widocoConfigFile -includeImportedOntologies -htaccess -webVowl -licensius

# subsequent builds
java -jar ../tools/WIDOCO/jar/widoco-1.4.1-jar-with-dependencies.jar -ontFile ./prod.owl -outFolder ./docs -getOntologyMetadata -oops -rewriteAll -saveConfig ./widocoConfigFile -includeImportedOntologies -htaccess -webVowl -licensius -crossRef
