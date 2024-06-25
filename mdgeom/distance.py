"""
Distance-based analysis
=======================

One of the most fundamental analysis techniques is to quantify the interactions
between different molecules or parts of molecules by calculating distances.

The use of *periodic boundary conditions* (PBC) in MD simulations can make
distance calculations challenging. We are typically interested in distances
that obey the **minimum image convention**, i.e., the shortest distance taking
all periodic images into account. MDAnalysis contains powerful distance
calculation functions that automatically apply the minimum image convention
when supplied with the unit cell dimensions (typically named `box`, i.e., the
lengths of the box :math:`L_x`, :math:`L_y`, and :math:`L_z` and the three
angles :math:`alpha`, :math:`beta`, :math:`gamma`).
"""

import numpy as np

def _check_groups(a, b):
    if a.n_atoms != b.n_atoms:
        raise ValueError("AtomGroups a and b contain different number of atoms")
        
    if a.dimensions is None and b.dimensions is None:
        # it's ok when both AtomGroups have no unitcell
        pass
    elif (a.dimensions is None) != (b.dimensions is None):  # xor
        raise ValueError("One AtomGroup does not have unit cell information")
    elif not np.allclose(a.dimensions, b.dimensions):
        raise ValueError("Unit cell dimensions differ between groups.")