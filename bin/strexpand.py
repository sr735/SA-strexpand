#!/usr/bin/env python

from splunklib.searchcommands import dispatch, StreamingCommand, Configuration, Option, validators
import splunklib.results as results
import splunklib.client as client
from splunk.appserver.mrsparkle.lib.util import make_splunkhome_path
import logging
import ConfigParser
import sys
import json
import time


@Configuration()
class strexpandCommand(StreamingCommand):
    def __init__(self):
        super(StreamingCommand, self).__init__()


    @staticmethod
    def _setup_logger(level, filename):
        log = logging.getLogger('splunk.appserver.customsearch.strexpand.' + filename)
        log.setLevel(level)

        handler = logging.handlers.RotatingFileHandler(make_splunkhome_path(['var', 'log', 'splunk', filename]), maxBytes=25000000, backupCount=5)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        log.addHandler(handler)

        return log

    def _validate(self):
        character, number = sys.argv[2:4]

        try:
            number = int(number)
        except ValueError as verr:
            logger.error(verr)

        if type(character) is not str:
            character = None
        if type(number) is not int:
            number = None

        return character, number


    def stream(self, records):
        character, number = self._validate()
        result = None
        for record in records:
            if character and number:
                result = character * number
            record['result'] = result
            yield record

if __name__ == "__main__":
    logger = strexpandCommand._setup_logger(logging.DEBUG, 'strexpand.log')
    dispatch(strexpandCommand, sys.argv, sys.stdin, sys.stdout, __name__)
