import shlex
import subprocess
import os
import logging

from django.core.management.base import BaseCommand
from django.utils import autoreload

logger = logging.getLogger()

def restart_celery():
    cmd = 'pkill -9 celery'
    subprocess.call(shlex.split(cmd))

    env = os.environ.copy()
    env.update({"C_FORCE_ROOT": "1"})

    cmd = 'celery -A sample_project worker'
    subprocess.call(shlex.split(cmd), env=env)


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info('Start Celery Worker with Auto Restart...')
        autoreload.run_with_reloader(restart_celery)
