import logging

from django.conf import settings
from django.core.management.base import BaseCommand

from mailer.engine import send_all
from time import sleep, time

# allow a sysadmin to pause the sending of mail temporarily.
PAUSE_SEND = getattr(settings, "MAILER_PAUSE_SEND", False)

class Command(BaseCommand):
    help = 'Passing through the mail queue, attempting to send all mail.'
    
    def handle(self, **options):
        delay = float(options.get('delay', 3))
        max_time = float(options.get('max_time', 60))
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        logging.info("-" * 72)
        # if PAUSE_SEND is turned on don't do anything.
        start = time()
        while True:
            if not PAUSE_SEND:
                send_all()
            else:
                logging.info("sending is paused, quitting.")
            if time() - start > max_time - delay:
                logging.info("done, leave...")
                break
            logging.info("waiting %.2f seconds to send next." % delay)
            sleep(delay)
