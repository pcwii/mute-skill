from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.util.log import getLogger
from mycroft.skills.context import adds_context, removes_context

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
        self.mute_state = False
        self.current_volume = 10
        self.mute_enable = True

    def initialize(self):
        self.load_data_files(dirname(__file__))
        try:
            self.mixer = Mixer()
        except:
            self.mute_enable = False

    @intent_handler(IntentBuilder('MuteIntent').require("MuteKeyword").build())
    def handle_mute_intent(self, message):
        if self.mute_enable:
            self.current_volume = self.mixer.getvolume()[0]
            self.mixer.setvolume(0)
            self.mute_state = True

    @intent_handler(IntentBuilder('UnMuteIntent').require("UnMuteKeyword").build())
    def handle_un_mute_intent(self, message):
        if self.mute_enable:
            if self.mute_state:
                self.mixer.setvolume(10)
                self.mute_state = False

    def stop(self):
        pass


def create_skill():
    return MuteSkill()
