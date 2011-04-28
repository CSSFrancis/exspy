# -*- coding: utf-8 -*-
# Copyright © 2011 Michael Sarahan
#
# This file is part of EELSLab.
#
# EELSLab is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# EELSLab is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EELSLab; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  
# USA
from IPython import ipapi
from eelslab import Release

def main():
    ip=ipapi.get()
    o=ip.options
    
    ip.ex("import eelslab.Release as Release")
    ip.ex("import eelslab.components as components")

    ip.ex("from eelslab.experiments import Experiments")
    ip.ex("from eelslab.signal import Signal")
    ip.ex("from eelslab.model import Model")
    ip.ex("from eelslab.file_io import load")
    ip.ex("from eelslab.edges_db import edges_dict")
    #from microscope import microscope
    ip.ex("from eelslab.defaults_parser import defaults")
    ip.ex("import eelslab.utils as utils")
    ip.ex("import eelslab.tests as tests")

    #Matplotlib imports
    ip.ex("import pylab")
    ip.ex("pylab.ion()")
    ip.ex("import matplotlib.pyplot as plt")

    # Numpy import
    ip.ex('import numpy as np')

    ip.ex("__version__ = Release.version")
    ip.ex("__revision__ = Release.revision")
    o.banner=Release.info

main()
