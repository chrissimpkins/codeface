#!/bin/bash
set -e

find . -name "data.json" -print0 | while IFS= read -r -d $'\0' line; do
	echo "validating $line"
	json validate --schema-file=schema.json --document-file=$line
done

echo "all ok"
