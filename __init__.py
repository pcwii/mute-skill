from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.util.log import getLogger
from mycroft.skills.context import adds_context, removes_context

_author__ = 'PCWii'
# Release - 20180723

LOGGER = getLogger(__name__)


class MuteSkill(MycroftSkill):
    """
    A Skill to control playback on a Kodi instance via the json-rpc interface.
    """
    def __init__(self):
        super(MuteSkill, self).__init__(name="MuteSkill")
        self.mute = False
        self.current_volume = 0

    def initialize(self):
        self.load_data_files(dirname(__file__))

    @intent_handler(IntentBuilder('MuteIntent').require("MuteKeyword").build())
    def handle_mute_intent(self, message):
        self.current_volume = self.mixer.getvolume()[0]
        self.mixer.setvolume(0)
        self.mute = True

    @intent_handler(IntentBuilder('UnMuteIntent').require("UnMuteKeyword").build())
    def handle_un_mute_intent(self, message):
        if self.mute:
            self.mixer.setvolume(self.current_volume)
            self.mute = False

    def stop(self):
        pass


def create_skill():
    return MuteSkill()
