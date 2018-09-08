from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.util.log import getLogger
from mycroft.skills.context import adds_context, removes_context
from mycroft.util.log import LOG

from alsaaudio import Mixer

_author__ = 'PCWii'
# Release - 20180723

LOGGER = getLogger(__name__)


class MuteSkill(MycroftSkill):
    """
    A Skill to control playback on a Kodi instance via the json-rpc interface.
    """
    def __init__(self):
        super(MuteSkill, self).__init__(name="MuteSkill")
        self.last_volume = 11
        self.default_volume = 11

    def initialize(self):
        self.load_data_files(dirname(__file__))
        self.mixer = Mixer()

    @intent_handler(IntentBuilder('MuteIntent').require("MuteKeyword").build())
    def handle_mute_intent(self, message):
        temp_volume = self.mixer.getvolume()[0]
        if temp_volume > 0:
            self.last_volume = temp_volume
        LOG.info(self.last_volume)
        self.mixer.setvolume(0)

    @intent_handler(IntentBuilder('UnMuteIntent').require("UnMuteKeyword").build())
    def handle_un_mute_intent(self, message):
        if self.last_volume == 0:
            self.last_volume = self.default_volume
        self.mixer.setvolume(self.last_volume)

    def stop(self):
        pass


def create_skill():
    return MuteSkill()
