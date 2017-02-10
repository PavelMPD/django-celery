import os
import celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dc.settings")

from django.apps import apps  # noqa

app = celery.Celery('dc')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])