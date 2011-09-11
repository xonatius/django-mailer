import logging

from django.conf import settings
from django.core.management.base import NoArgsCommand

from mailer.engine import send_all
from time import sleep

# allow a sysadmin to pause the sending of mail temporarily.
PAUSE_SEND = getattr(settings, "MAILER_PAUSE_SEND", False)

class Command(NoArgsCommand):
    help = 'Passing through the mail queue, attempting to send all mail.'
    
    def handle_noargs(self, **options):
        delay = float(options.get('delay', 3))
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        logging.info("-" * 72)
        # if PAUSE_SEND is turned on don't do anything.
        while True:
            if not PAUSE_SEND:
                send_all()
            else:
                logging.info("sending is paused, quitting.")
            logging.info("waiting %.2f seconds to send next." % delay)
            sleep(delay)
