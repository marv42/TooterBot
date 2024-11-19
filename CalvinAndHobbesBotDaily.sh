#!/usr/bin/env bash

# cf. https://stackoverflow.com/a/246128
DIR=$(dirname "$(readlink -f "$0")")
# echo $DIR

LOG_FILE=$DIR/CalvinAndHobbesBotDaily.log

date >$LOG_FILE
whoami >> $LOG_FILE
echo $DIR >> $LOG_FILE

cd $DIR
venv/bin/python -V >> $LOG_FILE 2>&1
venv/bin/python -m pip list >> $LOG_FILE 2>&1
venv/bin/python ./CalvinAndHobbesBot.py >> $LOG_FILE 2>&1
