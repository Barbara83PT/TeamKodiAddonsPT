# -*- coding: utf-8 -*-

import threading
from resources.lib.modules import control,log_utils

control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))

try:
    AddonVersion = control.addon('plugin.video.mirror').getAddonInfo('version')
    ModuleVersion = control.addon('plugin.video.mirror').getAddonInfo('version')
    RepoVersion = control.addon('repository.mirror').getAddonInfo('version')
    log_utils.log('===-[AddonVersion: %s]-' % str(AddonVersion) + '-[ModuleVersion: %s]-' % str(ModuleVersion) + '-[RepoVersion: %s]-' % str(RepoVersion), log_utils.LOGNOTICE)
except:
    log_utils.log('===-[Error Oppps...', log_utils.LOGNOTICE)
    log_utils.log('===-[Had Trouble Getting Version Info. Make Sure You Have the Cy4Repo.', log_utils.LOGNOTICE)

def syncTraktLibrary():
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.mirror/?action=tvshowsToLibrarySilent&url=traktcollection')
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.mirror/?action=moviesToLibrarySilent&url=traktcollection')

if control.setting('autoTraktOnStart') == 'true':
    syncTraktLibrary()

"""if int(control.setting('schedTraktTime')) > 0:
    log_utils.log('===-[Starting Trakt Scheduling.', log_utils.LOGNOTICE)
    log_utils.log('===-[Scheduled Time Frame '+ control.setting('schedTraktTime')  + ' Hours.', log_utils.LOGNOTICE)
    timeout = 3600 * int(control.setting('schedTraktTime'))
    schedTrakt = threading.Timer(timeout, syncTraktLibrary)
    schedTrakt.start()
"""
