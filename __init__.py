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

import re
import struct
import socket

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'kholdan'
LOG = getLogger(__name__)

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class WOLSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(WOLSkill, self).__init__(name="WOLSkill")
        
        # Initialize working variables used within the skill.
        self.count = 0

    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/World.voc
    # In this example that means it would match on utterances like:
    #   'Hello world'
    #   'Howdy you great big world'
    #   'Greetings planet earth'
    
    
    
    @intent_handler(IntentBuilder("").require("WOL").require("Target"))
    def handle_WOL_intent(self, message):
        # In this case, respond by simply speaking a canned response.
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/hello.world.dialog
        
        utterance = message.data.get('utterance')
        repeat = re.sub('^.*?' + message.data['WOL'], '', utterance)
        target = repeat.strip()
        
        if message.data["Target"] == "office":
            self.speak_dialog("starting", data={"Target": target})
            LOG.debug("Office code running")
        elif message.data["Target"] == "game server":
            self.speak_dialog("starting", data={"Target": target})
            LOG.debug("Game server code running")
        elif message.data["Target"] == "storage server":
            wakeonlan('00:23:7d:60:cd:24')
            self.speak_dialog("starting", data={"Target": target})
        else:
            self.speak_dialog("unable")

    #@intent_handler(IntentBuilder("").require("Count").require("Dir"))
    #def handle_count_intent(self, message):
    #    if message.data["Dir"] == "up":
    #        self.count += 1
    #    else:  # assume "down"
    #        self.count -= 1
    #    self.speak_dialog("count.is.now", data={"count": self.count})

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    def stop(self):
        return True

def wakeonlan(ethernet_address):
    addr_byte = ethernet_address.split(':')
    hw_addr = struct.pack('BBBBBB',
        int(addr_byte[0], 16),
        int(addr_byte[1], 16),
        int(addr_byte[2], 16),
        int(addr_byte[3], 16),
        int(addr_byte[4], 16),
        int(addr_byte[5], 16))
    
    msg = ''.join(['FFFFFFFFFFFF', hw_addr *20])
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(msg, ('broadcast', 9))
    s.close()

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return WOLSkill()
