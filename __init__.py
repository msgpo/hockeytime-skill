from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.util.log import getLogger
from mycroft.util.log import LOG
from websocket import create_connection, WebSocket
from time import sleep
import random

_author__ = 'PCWii'
# Release - 20181027

LOGGER = getLogger(__name__)


class HockeyTimeSkill(MycroftSkill):
    def __init__(self):
        super(HockeyTimeSkill, self).__init__(name="HockeyTimeSkill")
        self.process = None

    def initialize(self):
        self.load_data_files(dirname(__file__))

    def sendMycroftUtt(self, msg):
        uri = 'ws://localhost:8181/core'
        ws = create_connection(uri)
        utt = '{"context": null, "type": "recognizer_loop:utterance", "data": {"lang": "' \
              + self.lang + '", "utterances": ["' + msg + '"]}}'
        ws.send(utt)
        ws.close()

    @intent_handler(IntentBuilder("WatchHockeyIntent").require("WatchKeyword").require("HockeyKeyword").
                    build())
    def handle_watch_hockey_intent(self, message):
        LOG.info('watch hockey intent')
        # self.sendMycroftUtt('turn the room lights off silently')
        # sleep(0.75)
        self.sendMycroftUtt('turn the tv lights on silently')
        sleep(0.75)
        self.sendMycroftUtt('turn the wall lights on silently')
        sleep(0.75)
        self.sendMycroftUtt('turn the nanoleaf on silently')
        sleep(0.75)
        self.sendMycroftUtt('set the tv lights to blue silently')
        sleep(0.75)
        self.sendMycroftUtt('set the wall lights to blue silently')
        sleep(0.75)
        self.sendMycroftUtt('set the nanoleaf to toronto hockey game silently')
        sleep(0.75)
        self.sendMycroftUtt('set the nanoleaf to 15%')

    @intent_handler(IntentBuilder("AllLightsOffIntent").require("TurnKeyword").
                    require("AllKeyword").require("LightsKeyword").require("OffKeyword").build())
    def handle_all_lights_off_intent(self, message):
        LOG.info('turn off lights intent')
        self.sendMycroftUtt('turn the room lights off silently')
        sleep(0.75)
        self.sendMycroftUtt('turn the tv lights off silently')
        sleep(0.75)
        self.sendMycroftUtt('turn the wall lights off silently')
        sleep(0.75)
        self.sendMycroftUtt('turn the nanoleaf off silently')

    @intent_handler(IntentBuilder("SomeLightsOnIntent").require("TurnKeyword").
                    require("SomeKeyword").require("LightsKeyword").require("OnKeyword").build())
    def handle_some_lights_on_intent(self, message):
        LOG.info('turn some lights on intent')
        light_selection = random.randint(1, 3)
        if (light_selection == 1) or (light_selection == 3):
            self.sendMycroftUtt('turn the room lights on silently')
        if (light_selection == 2) or (light_selection == 3):
            self.sendMycroftUtt('turn the wall lights on silently')

    def stop(self):
        pass


def create_skill():
    return HockeyTimeSkill()
