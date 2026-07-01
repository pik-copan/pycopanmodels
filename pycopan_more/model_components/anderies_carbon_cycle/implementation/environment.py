"""Environment process taxon mixing class.
"""

# This file is part of pycopancore.
#
# Copyright (C) 2016-2017 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
# Contact: core@pik-potsdam.de
# License: BSD 2-clause license

from .. import interface as I
from pycopancore.data_model.master_data_model.dimensions_and_units import DimensionsAndUnits as D


class Environment (I.Environment):
    """Environment process taxon mixin implementation class."""

    # standard methods:

    def __init__(self,
                 *,  # TODO: uncomment when adding named args behind here
                 ocean_atmosphere_diffusion_coefficient=0.05 / D.years,  # Anderies
                 carbon_solubility_in_sea_water=1,  # Anderies
                 basic_photosynthesis_productivity=26.4 / D.years / \
                     (D.gigatonnes_carbon /
                      D.square_kilometers)**.5,  # see Nitzbon 2016
                 photosynthesis_sensitivity_on_atmospheric_carbon=0 \
                 #                    1.1e6 \
                 / D.years / (D.gigatonnes_carbon / D.square_kilometers)**.5
                 / D.kelvins,  # see Nitzbon 2016
                 terrestrial_carbon_capacity_per_area=5000 / 1.5e8 * \
                     D.gigatonnes_carbon / D.square_kilometers,  # ca. 2 times current value
                 basic_respiration_rate=0.0298 / D.years,  # see Nitzbon 2016
                 respiration_sensitivity_on_atmospheric_carbon=0 \
                 #                    3200 \
                 / D.years / (D.gigatonnes_carbon / D.square_kilometers),  # see Nitzbon 2016
                 temperature_offset=0.2 * D.kelvins,  # Anderies
                 temperature_sensitivity_on_atmospheric_carbon=0.8 * \
                     D.kelvins / D.gigatonnes_carbon,  # Anderies
                 scaling_factor_temperature_respiration=110,  # Anderies
                 exponent_for_increase_in_respiration_low_T=4,  # Anderies
                 exponent_for_increase_in_respiration_high_T=5,  # Anderies
                 strength_of_fertilization_effect=1.5,  # Anderies
                 rapidity_of_fertilization_saturation=0.3,  # Anderies
                 scaling_factor_temperature_photosynthesis=220,  # Anderies
                 exponent_for_increase_in_photosynthesis_low_T=3,  # Anderies
                 exponent_for_increase_in_photosynthesis_high_T=7,  # Anderies
                 ecosystem_dependent_conversion_factor=2.5,
                 terrestrial_carbon_carrying_capacity=0.7,
                 **kwargs):
        """Initialize the unique instance of Environment."""
        super().__init__(**kwargs)  # must be the first line

        self.ocean_atmosphere_diffusion_coefficient = \
            ocean_atmosphere_diffusion_coefficient
        self.carbon_solubility_in_sea_water = carbon_solubility_in_sea_water
        self.basic_photosynthesis_productivity = \
            basic_photosynthesis_productivity
        self.photosynthesis_sensitivity_on_atmospheric_carbon = \
            photosynthesis_sensitivity_on_atmospheric_carbon
        self.terrestrial_carbon_capacity_per_area = \
            terrestrial_carbon_capacity_per_area
        self.basic_respiration_rate = basic_respiration_rate
        self.respiration_sensitivity_on_atmospheric_carbon = \
            respiration_sensitivity_on_atmospheric_carbon
        self.temperature_offset = temperature_offset
        self.temperature_sensitivity_on_atmospheric_carbon = \
            temperature_sensitivity_on_atmospheric_carbon
# Anderies:
        self.scaling_factor_temperature_respiration = \
            scaling_factor_temperature_respiration
        self.exponent_for_increase_in_respiration_low_T = \
            exponent_for_increase_in_respiration_low_T
        self.exponent_for_increase_in_respiration_high_T = \
            exponent_for_increase_in_respiration_high_T
        self.strength_of_fertilization_effect = \
            strength_of_fertilization_effect
        self.rapidity_of_fertilization_saturation = \
            rapidity_of_fertilization_saturation
        self.scaling_factor_temperature_photosynthesis = \
            scaling_factor_temperature_photosynthesis
        self.exponent_for_increase_in_photosynthesis_low_T = \
            exponent_for_increase_in_photosynthesis_low_T
        self.exponent_for_increase_in_photosynthesis_high_T = \
            exponent_for_increase_in_photosynthesis_high_T
        self.ecosystem_dependent_conversion_factor = \
            ecosystem_dependent_conversion_factor
        self.terrestrial_carbon_carrying_capacity = \
            terrestrial_carbon_carrying_capacity

    # process-related methods:

    # TODO: add some if needed...

    processes = []  # TODO: instantiate and list process objects here
