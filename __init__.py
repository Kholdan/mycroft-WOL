# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from mycroft import intent_handler

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Kholdan'

LOGGER = getLogger(__name__)


class WOLSkill(MycroftSkill):
    def __init__(self):
        super(WOLSkill, self).__init__(name="WOLSkill")
        
    @intent_handler(IntentBuilder("WOL_Intent").require("WOLKeyword").require("TargetKeyword"))
    def handle_WOL_intent(self, message):
        LOGGER.debug('WOL intent loaded')
        #TODO Create config file and initalize list of MAC addresses from file
        
        target = message.data.get("TargetKeyword")
        

        if target = "office":
            self.speak_dialog("starting")
            #TODO Add logic to send WOL packet to Specific MAC address on network
        else:
            self.speak_dialog("unable")

    def stop(self):
        pass


def create_skill():
    return WOLSkill()
