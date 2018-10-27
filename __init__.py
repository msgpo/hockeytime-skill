from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.util.log import getLogger
from mycroft.skills.context import adds_context, removes_context
from mycroft.util import play_mp3

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

    @intent_handler(IntentBuilder("WatchHockeyIntent").require("WatchKeyword").require("HockeyKeyword").
                    build())
    def handle_watch_hockey_intent(self, message):
        self.speak_dialog('context', data={"result": "I am Groot!"}, expect_response=True)

    @intent_handler(IntentBuilder('GameOverIntent').require('HockeyKeyword').require('EndedKeyword').build())
    def handle_game_over_intent(self, message):
        self.speak_dialog('context', data={"result": "I am Groot"}, expect_response=True)

    def stop(self):
        pass


def create_skill():
    return HockeyTimeSkill()
