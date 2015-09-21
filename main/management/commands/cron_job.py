from django.core.management.base import BaseCommand

# This Django management command needs to go and find
# wherever you have your models and your settings
# once you run ./manage.py cron_job.
# For this setup, it would be:
import os, sys

sys.path.append("../../..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import ModelTweet


# Django looks for the handle method on this precise command to
# run anything. You can add more methods that do more things 
#and then have handle call them, but to automate a simple app
# all you need is the call here.
class Command(BaseCommand):

    def handle(self, *args, **options):
        help = "Makes a new tweet for CmonSister."

        ModelTweet.your_method_name()
        