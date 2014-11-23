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
       pass


    def onPlayBackStarted(self):

        global language_string
        global check_audio
        global __setting__
        
        # get the language setting
        language_string = __setting__('language_string')
        check_audio = True

        log('check audio set to True, language string = %s' % language_string)
        


def Main(__setting__):

    global language_string
    global check_audio

    language_string = ''
    check_audio = False # until challenged

    tongue_player = myPlayer()

    log('service started')

    while not xbmc.abortRequested:

        xbmc.sleep(500)

        if check_audio:

            tongue_player.showSubtitles(False)

            check_audio = False
            
            streams = tongue_player.getAvailableAudioStreams()
            log('streams found: %s' % streams)

            if streams:
                for i, stream in enumerate(streams):
                    if language_string in stream:
                        log('changing audio stream')
                        tongue_player.setAudioStream(i)
                        break
                else:
                    log('activating subtitles')
                    tongue_player.showSubtitles(True)
            else:
                log('no audio streams found')



if __name__ == "__main__":
    Main(__setting__)
    log('service exiting')
