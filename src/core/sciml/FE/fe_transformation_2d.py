# Copyright (c) 2024 Zenteiq Aitech Innovations Private Limited and 
# AiREX Lab, Indian Institute of Science, Bangalore.
# All rights reserved.
#
# This file is part of SciREX
# (Scientific Research and Engineering eXcellence Platform).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# For any clarifications or special considerations,
# please contact: contact@scirex.org
"""
This module provides an interface for the transformation methods used in the
2D finite element analysis. The transformation is essential for mapping
element geometry in the reference domain to the actual physical domain.
The primary functionalities encapsulated within this class include:
    1. set_cell() - To set the physical coordinates of the cell. These coordinates are essential for subsequent computations involving Jacobians and transformations.
    2. get_original_from_ref(xi, eta) - Given reference coordinates (xi, eta), this method returns the corresponding coordinates in the physical domain.
    3. get_jacobian(xi, eta) - For a given point in the reference domain, represented by (xi, eta), this method calculates and returns the Jacobian of the transformation, which provides information about the local stretching, rotation, and skewing of the element. Further implementations of this class for specific element types (like quad and triangular elements) can incorporate more detailed and element-specific transformation techniques.

Author: Thivin Anandh D

Date:   20/Sep/2023

History: First version -  20/Sep/2023 - Thivin Anandh
"""

from abc import abstractmethod


class FETransforamtion2D:
    """
    This class represents a 2D finite element transformation.
    """

    def __init__(self):
        """
        Constructor for the FETransforamtion2D class.
        """

    @abstractmethod
    def set_cell(self):
        """
        Set the cell coordinates, which will be used to calculate the Jacobian and actual values.

        :return: None
        """

    @abstractmethod
    def get_original_from_ref(self, xi, eta):
        """
        This method returns the original coordinates from the reference coordinates.

        :param xi: The xi coordinate in the reference space.
        :type xi: float
        :param eta: The eta coordinate in the reference space.
        :type eta: float
        :return: The original coordinates (x, y) corresponding to the given reference coordinates.
        :rtype: tuple
        """

    @abstractmethod
    def get_original_from_ref(self, xi, eta):
        """
        This method returns the original coordinates from the reference coordinates.

        :param xi: The xi value of the reference coordinates.
        :type xi: float
        :param eta: The eta value of the reference coordinates.
        :type eta: float
        :return: The original coordinates corresponding to the given reference coordinates.
        :rtype: tuple
        """

    @abstractmethod
    def get_jacobian(self, xi, eta):
        """
        This method returns the Jacobian of the transformation.

        :param xi: The xi coordinate.
        :type xi: float
        :param eta: The eta coordinate.
        :type eta: float
        :return: The Jacobian matrix.
        :rtype: numpy.ndarray
        """


## Mandatory, Import all the basis functions here (Quad element Transformations)
from .quad_affine import *
from .quad_bilinear import *
