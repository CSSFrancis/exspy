import numpy as np
import math

from hyperspy.misc.elements import elements as elements_db


def _get_element_and_line(Xray_line):
    lim = Xray_line.find('_')
    return Xray_line[:lim], Xray_line[lim + 1:]


def _get_energy_xray_line(xray_line):
    energy, line = _get_element_and_line(xray_line)
    return elements_db[energy]['Atomic_properties']['Xray_lines'][
        line]['energy (keV)']


def get_FWHM_at_Energy(energy_resolution_MnKa, E):
    """Calculates the FWHM of a peak at energy E.

    Parameters
    ----------
    energy_resolution_MnKa : float
        Energy resolution of Mn Ka in eV
    E : float
        Energy of the peak in keV

    Returns
    -------
    float : FWHM of the peak in keV

    Notes
    -----
    From the textbook of Goldstein et al., Plenum publisher,
    third edition p 315

    """
    FWHM_ref = energy_resolution_MnKa
    E_ref = _get_energy_xray_line('Mn_Ka')

    FWHM_e = 2.5 * (E - E_ref) * 1000 + FWHM_ref * FWHM_ref

    return math.sqrt(FWHM_e) / 1000  # In mrad


def xray_range(xray_line, beam_energy, density='auto'):
    '''Return the Anderson-Hasler X-ray range.

    Return the maximum range of X-ray generation in a pure bulk material.

    Parameters
    ----------
    xray_line: str
        The X-ray line, e.g. 'Al_Ka'
    beam_energy: float
        The energy of the beam in kV.
    density: {float, 'auto'}
        The density of the material in g/cm3. If 'auto', the density
        of the pure element is used.

    Returns
    -------
    X-ray range in micrometer.

    Notes
    -----
    From Anderson, C.A. and M.F. Hasler (1966). In proceedings of the
    4th international conference on X-ray optics and microanalysis.

    See also the textbook of Goldstein et al., Plenum publisher,
    third edition p 286

    '''

    element, line = _get_element_and_line(xray_line)
    if density == 'auto':
        density = elements_db[
            element][
            'Physical_properties'][
            'density (g/cm^3)']
    Xray_energy = _get_energy_xray_line(xray_line)

    return 0.064 / density * (np.power(beam_energy, 1.68) -
                              np.power(Xray_energy, 1.68))


def electron_range(element, beam_energy, density='auto', tilt=0):
    '''Return the Kanaya-Okayama electron range.

    Return the maximum electron range in a pure bulk material.

    Parameters
    ----------
    element: str
        The element symbol, e.g. 'Al'.
    beam_energy: float
        The energy of the beam in keV.
    density: {float, 'auto'}
        The density of the material in g/cm3. If 'auto', the density of
        the pure element is used.
    tilt: float.
        The tilt of the sample in degrees.

    Returns
    -------
    Electron range in micrometers.

    Notes
    -----
    From Kanaya, K. and S. Okayama (1972). J. Phys. D. Appl. Phys. 5, p43

    See also the textbook of Goldstein et al., Plenum publisher,
    third edition p 72.

    '''

    if density == 'auto':
        density = elements_db[
            element]['Physical_properties']['density (g/cm^3)']
    Z = elements_db[element]['General_properties']['Z']
    A = elements_db[element]['General_properties']['atomic_weight']

    return (0.0276 * A / np.power(Z, 0.89) / density *
            np.power(beam_energy, 1.67) * math.cos(math.radians(tilt)))


def take_off_angle(tilt_stage,
                   azimuth_angle,
                   elevation_angle):
    """Calculate the take-off-angle (TOA).

    TOA is the angle with which the X-rays leave the surface towards
    the detector.

    Parameters
    ----------
    tilt_stage: float
        The tilt of the stage in degrees. The sample is facing the detector when
        positively tilted.
    azimuth_angle: float
        The azimuth of the detector in degrees. 0 is perpendicular to the tilt
        axis.
    elevation_angle: float
        The elevation of the detector in degrees.

    Returns
    -------
    take_off_angle: float.
        In degrees.

    Notes
    -----
    Defined by M. Schaffer et al., Ultramicroscopy 107(8), pp 587-597 (2007)

    """

    a = math.radians(90 + tilt_stage)
    b = math.radians(azimuth_angle)
    c = math.radians(elevation_angle)

    return math.degrees(np.arcsin(-math.cos(a) * math.cos(b) * math.cos(c)
                                  + math.sin(a) * math.sin(c)))


def xray_lines_model(elements=['Al', 'Zn'],
                     beam_energy=200,
                     weight_percents=[50, 50],
                     energy_resolution_MnKa=130,
                     energy_axis={'name': 'E', 'scale': 0.01, 'units': 'keV',
                                  'offset': -0.1, 'size': 1024}
                     ):
    """
    Generate a model of X-ray lines using a Gaussian epr x-ray lines.

    The area under a main peak (alpha) is equal to 1 and weighted by the
    composition.

    Parameters
    ----------
    elements : list of strings
        A list of chemical element symbols.
    beam_energy: float
        The energy of the beam in keV.
    weight_percents: list of float
        The composition in weight percent.
    energy_resolution_MnKa: float
        The energy resolution of the detector in eV
    energy_axis: dic
        The dictionary for the energy axis. It must contains 'size' and the
        units must be 'eV' of 'keV'.

    Example
    -------
    >>> s = utils_eds.simulate_model(['Cu', 'Fe'], beam_energy=30)
    >>> s.plot()
    """
    from hyperspy._signals.eds_tem import EDSTEMSpectrum
    from hyperspy.model import Model
    from hyperspy import components
    s = EDSTEMSpectrum(np.zeros(energy_axis['size']), axes=[energy_axis])
    s.set_microscope_parameters(
        beam_energy=beam_energy,
        energy_resolution_MnKa=energy_resolution_MnKa)
    s.add_elements(elements)
    counts_rate = 1.
    live_time = 1.
    if weight_percents is None:
        weight_percents = [100] * len(elements)
    m = Model(s)
    for i, (element, weight_percent) in enumerate(zip(
            elements, weight_percents)):
        for line in elements_db[
                element]['Atomic_properties']['Xray_lines'].keys():
            line_energy = elements_db[element]['Atomic_properties'][
                'Xray_lines'][line]['energy (keV)']
            ratio_line = elements_db[element]['Atomic_properties'][
                'Xray_lines'][line]['weight']
            if s._get_xray_lines_in_spectral_range(
                    [element+'_'+line])[1] == []:
                g = components.Gaussian()
                g.centre.value = line_energy
                g.sigma.value = get_FWHM_at_Energy(
                    energy_resolution_MnKa, line_energy) / 2.355
                g.A.value = live_time * counts_rate * \
                    weight_percent / 100 * ratio_line
                m.append(g)
    s.data = m.as_signal().data
    # s.add_poissonian_noise()
    return s
