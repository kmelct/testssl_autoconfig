#!/bin/bash
args=("$@")

./testssl.sh --quiet --color 0 --debug 0 --jsonfile-pretty=file.json ${args[0]} > log.file

cat file.json