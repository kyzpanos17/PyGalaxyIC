# tests/test_core.py
from PyGalaxyIC.core import kinetic_energy

def test_kinetic_energy():
    assert kinetic_energy(2, 3) == 9