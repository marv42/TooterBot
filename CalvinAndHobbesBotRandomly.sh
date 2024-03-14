#!/usr/bin/env bash

# call this from cron.hourly

# cf. https://stackoverflow.com/a/246128
DIR=$(dirname "$(readlink -f "$0")")
echo $DIR

LOG_FILE=/dev/stdout # $DIR/CalvinAndHobbesBotRandomly.log

date >$LOG_FILE
whoami >> $LOG_FILE
echo $DIR >> $LOG_FILE

cd $DIR
venv/bin/python -V >> $LOG_FILE 2>&1
venv/bin/python -m pip list >> $LOG_FILE 2>&1

RANDOM_NUMBER_FROM_0_TO_35=$(echo $((RANDOM % 36)))
[ "$RANDOM_NUMBER_FROM_0_TO_35" -eq 0 ] && venv/bin/python ./CalvinAndHobbesBot.py --random >> $LOG_FILE 2>&1
