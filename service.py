#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2014 KODeKarnage
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import xbmc
import xbmcaddon


__addon__        = xbmcaddon.Addon('service.native.tongue')
__addonid__      = __addon__.getAddonInfo('id')
__setting__      = __addon__.getSetting
script_path      = __addon__.getAddonInfo('path')
addon_path       = xbmc.translatePath('special://home/addons')
__setting__      = __addon__.getSetting

check_audio = False

def log(msg, label=''):

    if label:
        combined_message = 'service.native.tongue ::-:: ' + str(label) + ' = ' + str(msg)
    else:
        combined_message = 'service.native.tongue ::-:: ' + str(msg)

    xbmc.log(msg=combined_message)



class myPlayer(xbmc.Player):

    def __init__(self, *args, **kwargs):
        self.language_string = kwargs.get('language_string', 'eng')
        self.check_audio = kwargs.(get'check_audio', False)
        self.setting = kwargs.get(__setting__, '')


    def onPlayBackStarted(self):
        # get the language setting
        self.language_string = self.setting('language_string').lower()
        self.check_audio = True
        


def Main(__setting__):

    language_string = ''
    check_audio = False # until challenged

    tongue_player = myPlayer(language_string, check_audio, __setting__)

    while not xbmc.abortRequested:

        xbmc.sleep(500)

        if check_audio:

            tongue_player.showSubtitles(False)

            check_audio = False
            
            streams = tongue_player.getAvailableAudioStreams()

            if streams:
                if language_string in streams:
                    log('changing audio stream')
                    stream_number = streams.index(language_string)
                    tongue_player.setAudioStream(stream_number)
                else:
                    log('activating subtitles')
                    tongue_player.showSubtitles(True)



if __name__ == "__main__":
    Main(__setting__)
