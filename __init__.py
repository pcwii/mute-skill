from os.path import dirname
import time

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.util.log import getLogger
from mycroft.skills.context import adds_context, removes_context

_author__ = 'PCWii'
# Release - 20180713

LOGGER = getLogger(__name__)


class MuteSkill(MycroftSkill):
    """
    A Skill to control playback on a Kodi instance via the json-rpc interface.
    """
    def __init__(self):
        super(MuteSkill, self).__init__(name="MuteSkill")
        self.mute = False
        self.current_volume

    def initialize(self):
        self.load_data_files(dirname(__file__))

        #  Check and then monitor for credential changes

    @intent_handler(IntentBuilder('BeSilentIntent').require("MuteKeyword").build())
    def handle_be_silent_intent(self, message):