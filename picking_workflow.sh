#!/usr/bin/env bash
[ -z "$1" ] && echo "You must provide a database name" && exit 1
# $1 is the database name
./base create_products -d "$1" -p
./base create_so -d "$1" -p
./base confirm_so -d "$1" -p
./base validate_picking -d "$1"
