#
#   Copyright (c) 2013-2014, Scott J Maddox
#
#   This file is part of openbandparams.
#
#   openbandparams is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   openbandparams is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with openbandparams.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
# Make sure we import the local obpds version
import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from obpds import *

AlAs._meff_e_X_DOS = GaAs._meff_e_X_DOS
AlSb._meff_e_X_DOS = GaAs._meff_e_X_DOS

# Layer Structure
ls = LayerStructure([
    OhmicContact(),
    Layer(100*nm, Material(InAs, 1e19/cm3)),
    Layer(2*um, Material(InAs, 1e17/cm3)),
    Layer(6*um, Material(InAs, 1e14/cm3)),
    Layer(1.5*um, Material(InAs,  -1e18/cm3)),
    Layer(0.5*um, Material(InAs,  -2e18/cm3)),
    OhmicContact(),
])

# ls.show_composition() # show the composition vs. depth
# ls.show_doping() # show the doping vs. depth
# ls.show_flatband() # show the flatband profile vs. depth

# Simulate and show the equilibrium band profile using the default method.
ls.show_equilibrium(N=1000)