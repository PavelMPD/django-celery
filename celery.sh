#!/bin/sh

. ./.venv/bin/activate

ps auxww | grep  'dc worker' | awk '{print $2}' | xargs kill -9

LOG_FOLDER="$(pwd)/logs";

if ! [ -d "$LOG_FOLDER" ]; then
  mkdir "$LOG_FOLDER"
fi

celery -A dc worker -l info -n worker.word -Q word_queue 2> "$LOG_FOLDER/word_queue.log" &
celery -A dc worker -l info --beat -n worker.beat -Q beat_queue  --concurrency=1 2> "$LOG_FOLDER/beat_queue.log" &

deactivate
