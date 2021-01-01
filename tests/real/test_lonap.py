# Copyright (C) 2017-2021 Pier Carlo Chiodi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .base import *


class TestRealConfigs_LONAP(object):

    IXP = "LONAP"
    CLIENTS_FILE = "lonap.yml"

class TestRealConfigs_LONAP_BIRD(TestRealConfigs_LONAP,
                                 TestRealConfigs_BIRD):
    __test__ = True

class TestRealConfigs_LONAP_OpenBGPD64(TestRealConfigs_LONAP,
                                       TestRealConfigs_OpenBGPD64):
    __test__ = True
