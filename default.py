# -*- coding: UTF-8 -*-
#/*
# *      Copyright (C) 2013 Libor Zoubek
# *
# *
# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with this program; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *
# */
import os
sys.path.append( os.path.join ( os.path.dirname(__file__),'resources','lib') )

import re
import xbmcaddon
import util,xbmcprovider,xbmcutil
import tvsosac

__scriptid__   = 'plugin.video.tv.sosac.ph'
__scriptname__ = 'tv.sosac.ph'
__addon__      = xbmcaddon.Addon(id=__scriptid__)
__language__   = __addon__.getLocalizedString
__set          = __addon__.getSetting

settings = {'downloads':__set('downloads'),'quality':__set('quality'),'subs':__set('subs') == 'true'}

reverse_eps = __set('order-episodes') == '0'

params = util.params()
if params=={}:
	xbmcutil.init_usage_reporting( __scriptid__)
xbmcprovider.XBMCMultiResolverContentProvider(tvsosac.TVSosacContentProvider(reverse_eps=reverse_eps),settings,__addon__).run(params)


