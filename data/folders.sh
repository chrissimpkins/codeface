#!/bin/bash
set -e

pushd ../fonts/ >> /dev/null

for FOLDER in */
do
	FOLDER=$(basename "$FOLDER")
	mkdir -p ../data/$FOLDER
done

popd >> /dev/null

pushd ../cjk-fonts/ >> /dev/null

for FOLDER in */
do
	FOLDER=$(basename "$FOLDER")
	mkdir -p ../data/$FOLDER
done

popd >> /dev/null
