# src/PyGalaxyIC/core.py

def kinetic_energy(m, v):
    """
    Compute kinetic energy.

    Parameters
    ----------
    m : float
        Mass in kilograms.
    v : float
        Velocity in meters per second.

    Returns
    -------
    float
        Kinetic energy in joules.
    """
    return 0.5 * m * v**2