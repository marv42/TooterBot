#!/bin/bash

# TODO https://stackoverflow.com/a/246128
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR
source $DIR/venv/bin/activate
$DIR/venv/bin/python3 $DIR/WasGeschahBot.py
