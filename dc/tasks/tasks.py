import celery
import time

from celery.utils.log import get_task_logger
from django.conf import settings

LOG = get_task_logger(__name__)


@celery.task(
    ignore_result=True,
    name='tasks.tasks.add_word',
    time_limit=getattr(settings, 'ADD_WORD_TIME_LIMIT', 60))
def add_word(word):
    LOG.info("Word '{}' was added.".format(word))


@celery.task(
    ignore_result=True,
    name='tasks.tasks.import_words',
    time_limit=getattr(settings, 'IMPORT_WORDS_TIME_LIMIT', 240))
def import_words():
    LOG.info("Start to import words by schedule")
    time.sleep(25)
    LOG.info("Words were imported by schedule")
