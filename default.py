# ------------------------------------------------------------
# Kan videos addon
# (c) 2017 - Dvir Cohen
# Based on code from Simple TechNerd
# ------------------------------------------------------------

import os
import sys
import plugintools
import xbmc, xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.kan'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

# Get the data from youtube about both channels
channellist = [
    ("Kan Videos", "channel/UCDJ6HHS5wkNaSREumdJRYhg",
     'https://yt3.ggpht.com/-HUhAZjlXb_I/AAAAAAAAAAI/AAAAAAAAAAA/YPSbNUJ4Bb8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
    ("Kan and Now", "channel/UC_HwfTAcjBESKZRJq6BTCpg",
     'https://yt3.ggpht.com/-xJR87H-pJUo/AAAAAAAAAAI/AAAAAAAAAAA/jNlcdjfPeJY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')
]

for name, id, icon in channellist:
    plugintools.add_item(title=name, url="plugin://plugin.video.youtube/{}/".format(id), thumbnail=icon, folder=True)


# Entry point
def run():
    plugintools.log("kan.run")

    # Get params
    params = plugintools.get_params()

    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action + "(params)"

    plugintools.close_item_list()


# Main menu
def main_list(params):
    plugintools.log("kan.main_list " + repr(params))


run()
