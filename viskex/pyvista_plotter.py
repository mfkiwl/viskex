# Copyright (C) 2023 by the viskex authors
#
# This file is part of viskex.
#
# SPDX-License-Identifier: MIT
"""viskex plotter interfacing pyvista."""

import os
import typing

import numpy as np
import numpy.typing
import panel.pane.vtk.vtk
import pyvista.trame.jupyter

from viskex.base_plotter import BasePlotter


class PyvistaPlotter(BasePlotter):
    """viskex plotter interfacing pyvista."""

    try:
        import google.colab  # noqa: F401
    except ImportError:
        _jupyter_backend = os.getenv("VISKEX_PYVISTA_BACKEND", "client")
    else:
        _jupyter_backend = "panel"
    assert _jupyter_backend in (
        "client", "server", "trame", # trame backends
        "panel" # panel backends
    )

    def plot_mesh(self, mesh: pyvista.UnstructuredGrid, dim: typing.Optional[int] = None) -> typing.Union[
            panel.pane.vtk.vtk.VTKRenderWindowSynchronized, pyvista.trame.jupyter.Widget]:
        """
        Plot a 2D or 3D mesh, stored in a pyvista.UnstructuredGrid.

        Parameters
        ----------
        pyvista
            A pyvista unstructured grid to be plotted.
        dim
            Plot entities associated to this dimension. If not provided, the topological dimension is used.

        Returns
        -------
        :
            A pyvista widget representing a plot of the 2D or 3D mesh.
        """
        assert dim is None
        plotter = pyvista.Plotter(notebook=True)  # type: ignore[no-untyped-call]
        plotter.background_color = "white"
        plotter.add_mesh(mesh, color="red", edge_color="black", show_edges=True)  # type: ignore[no-untyped-call]
        plotter.add_axes()
        return plotter.show(  # type: ignore[no-any-return, no-untyped-call]
            jupyter_backend=self._jupyter_backend, return_viewer=True)

    def plot_mesh_entities(self, mesh, dim: int, entities) -> None:
        """Plot a mesh, highlighting the provided `dim`-dimensional entities."""
        pass  # pragma: no cover

    def plot_scalar_field(
        self, scalar_field, name: str, warp_factor: float = 0.0, part: str = "real"
    ) -> None:
        """Plot a scalar field."""
        pass  # pragma: no cover

    def plot_vector_field(
        self, vector_field, name: str, glyph_factor: float = 0.0, warp_factor: float = 0.0,
        part: str = "real"
    ) -> None:
        """Plot a vector field."""
        pass  # pragma: no cover
