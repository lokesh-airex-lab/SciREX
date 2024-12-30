# Copyright (c) 2024 Zenteiq Aitech Innovations Private Limited and AiREX Lab,
# Indian Institute of Science, Bangalore.
# All rights reserved.
#
# This file is part of SciREX
# (Scientific Research and Engineering eXcellence Platform),
# developed jointly by Zenteiq Aitech Innovations and AiREX Lab
# under the guidance of Prof. Sashikumaar Ganesan.
#
# SciREX is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SciREX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with SciREX. If not, see <https://www.gnu.org/licenses/>.
#
# For any clarifications or special considerations,
# please contact <scirex@zenteiq.ai>
# Author : Thivin Anandh. D
# Added test cases for validating Dirichlet boundary routines
# Routines, provide a value to the boundary points and check if the value is set correctly.

import pytest
import numpy as np
from pathlib import Path
import shutil
from scirex.core.sciml.geometry.geometry_2d import Geometry_2D
from scirex.core.sciml.fe.fespace2d import Fespace2D
from scirex.core.sciml.fastvpinns.data.datahandler2d import DataHandler2D


@pytest.mark.parametrize("mesh_generation_method", ["internal", "external"])
@pytest.mark.parametrize("mesh_type", ["quadrilateral"])
def test_mesh_and_mesh_gen_type(mesh_generation_method, mesh_type):
    """
    Test case for checking the mesh generation type.
    """
    Path("tests/dump").mkdir(parents=True, exist_ok=True)

    # Define the geometry
    domain = Geometry_2D("quadrilateral", mesh_generation_method, 10, 10, "tests/dump")

    # Perform assertions
    assert (
        domain.mesh_type == mesh_type
        and domain.mesh_generation_method == mesh_generation_method
    )

    shutil.rmtree("tests/dump")


@pytest.mark.parametrize("mesh_generation_method", ["orthogonal"])
@pytest.mark.parametrize("mesh_type", ["triangle", "polygon"])
def test_invalid_mesh_and_mesh_gen_type(mesh_generation_method, mesh_type):
    """
    Test case for checking the mesh generation type.
    """
    Path("tests/dump").mkdir(parents=True, exist_ok=True)

    with pytest.raises(ValueError):
        domain = Geometry_2D(mesh_type, mesh_generation_method, 10, 10, "tests/dump")

    shutil.rmtree("tests/dump")


@pytest.mark.parametrize("mesh_generation_method", ["external", "internal"])
def test_plot_adaptive(mesh_generation_method):
    """
    Test the write_vtk method when the number of solution columns and data names do not match.
    """
    Path("tests/dump").mkdir(parents=True, exist_ok=True)

    # Define test inputs
    solution = np.array([[1, 2], [3, 4]])
    output_path = "tests/dump"
    filename = "output.vtk"
    data_names = ["data1", "data2", "data3"]

    # Define the geometry
    domain = Geometry_2D("quadrilateral", mesh_generation_method, 10, 10, "tests/dump")

    if mesh_generation_method == "internal":
        # read internal mesh
        cells, boundary_points = domain.generate_quad_mesh_internal(
            x_limits=[0, 1],
            y_limits=[0, 1],
            n_cells_x=4,
            n_cells_y=4,
            num_boundary_points=100,
        )
    elif mesh_generation_method == "external":
        # read external mesh
        cells, boundary_points = domain.read_mesh(
            mesh_file="tests/support_files/circle_quad.mesh",
            boundary_point_refinement_level=2,
            bd_sampling_method="uniform",
            refinement_level=0,
        )
    else:
        pass

    with pytest.raises(ValueError):
        domain.write_vtk(solution, output_path, filename, data_names)

    shutil.rmtree("tests/dump")