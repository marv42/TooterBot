#!/bin/bash

# call this from cron.hourly

# TODO https://stackoverflow.com/a/246128
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

RANDOM_NUMBER_FROM_0_TO_11=$(echo $((RANDOM % 12)))
[ "$RANDOM_NUMBER_FROM_0_TO_11" -eq 0 ] && python3 $DIR/CalvinAndHobbesBot.py --random
