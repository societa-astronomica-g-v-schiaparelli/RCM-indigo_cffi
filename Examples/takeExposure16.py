#!/usr/bin/env python

# This file is part of indigo_cffi.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import indigo
import time
import sys

if __name__ == "__main__":

    # Start up the indigo instanc
    
    indpy = indigo.indigoPy('takeExposure')

    indpy.start()

    time.sleep(5)  # wait for server to deliver all the properties from the camera

    indigoDevName = 'ZWO ASI1600MM Pro #0'

    if len(sys.argv) > 1:
        expTime = sys.argv[1]
    else:
        expTime = '1'

    # sequence of commands

    indpy.sendCommand(indigoDevName, 'CONNECTION', {'DISCONNECTED':'Off', 'CONNECTED':'On'})
    
    indpy.sendCommand(indigoDevName, 'CCD_UPLOAD_MODE', {'CLIENT':'Off', 'LOCAL':'On', 'BOTH':'Off', 'PREVIEW':'Off', 'PREVIEW_LOCAL':'Off'})

    indpy.sendCommand(indigoDevName, 'CCD_MODE', {'RAW 8 1x1':'Off', 'RAW 16 1x1':'On'})
    
    indpy.sendCommand(indigoDevName, 'PIXEL_FORMAT', {'RAW 8':'Off', 'RAW 16':'On'})
    
    indpy.sendCommand(indigoDevName, 'ASI_ADVANCED', {'BandWidth':'50'})

    indpy.sendCommand(indigoDevName, 'CCD_EXPOSURE', {'EXPOSURE':expTime})

    # Disconnect server

    time.sleep(5)  # wait for server to clean up

    indpy.printProperties()

    indpy.stop()
